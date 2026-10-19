"""Threads 對標帳號抓取工具（本機執行，需登入副帳號）。

用法見同資料夾 README.md。重點：
- 瀏覽器設定檔放 repo 外（預設 ~/.luscena_threads_profile），輸出也放 repo 外（預設 ~/luscena_benchmarks/<帳號>/）。
- 只讀：不按讚、不留言、不追蹤、不開私訊。只捲動主頁並記錄頁面收到的貼文資料。
- 預設不設篇數上限，一路捲到帳號的第一篇；可中斷，重跑時跳過已抓過的 code。
"""

import argparse
import csv
import json
import random
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

DEFAULT_ACCOUNTS = ["yuan.ruoting", "mina_ya2002", "eiko.smiles", "arielanailife"]
COLUMNS = [
    "code", "utc", "taiwan", "likes", "replies", "reposts", "media", "text",
    "carousel_count", "has_video", "link_count", "hashtag_count", "caption_length",
    "reply_to",
]
TW = timezone(timedelta(hours=8))
URL_RE = re.compile(r"(https?://\S+|www\.\S+)")
TAG_RE = re.compile(r"#[^\s#]+")


def log(msg):
    print(f"[{datetime.now():%H:%M:%S}] {msg}", flush=True)


# ---------- 解析 ----------

def walk(obj):
    """遞迴走過 JSON，逐一產出 dict。"""
    stack = [obj]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            yield cur
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)


def parse_json_text(text):
    """GraphQL 回應可能有 for (;;); 前綴或多行 JSON。"""
    text = text.strip()
    if text.startswith("for (;;);"):
        text = text[len("for (;;);"):]
    try:
        return [json.loads(text)]
    except ValueError:
        out = []
        for line in text.splitlines():
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except ValueError:
                    pass
        return out


def is_post(d):
    return (
        isinstance(d.get("code"), str)
        and "taken_at" in d
        and isinstance(d.get("user"), dict)
        and ("caption" in d or "like_count" in d)
    )


def caption_of(p):
    cap = p.get("caption")
    if isinstance(cap, dict) and cap.get("text"):
        return cap["text"]
    info = p.get("text_post_app_info") or {}
    frags = ((info.get("text_fragments") or {}).get("fragments")) or []
    return "".join(f.get("plaintext") or "" for f in frags if isinstance(f, dict))


def post_row(p):
    info = p.get("text_post_app_info") or {}
    text = caption_of(p)
    carousel = p.get("carousel_media") or []
    has_video = bool(p.get("video_versions")) or any(
        isinstance(c, dict) and c.get("video_versions") for c in carousel
    )
    if carousel:
        media, count = f"image x{len(carousel)}", len(carousel)
    elif p.get("video_versions"):
        media, count = "video", 1
    elif (p.get("image_versions2") or {}).get("candidates"):
        media, count = "image x1", 1
    else:
        media, count = "text", 0

    links = len(URL_RE.findall(text))
    if info.get("link_preview_attachment") and links == 0:
        links = 1
    frags = ((info.get("text_fragments") or {}).get("fragments")) or []
    tag_frags = sum(1 for f in frags if isinstance(f, dict) and f.get("fragment_type") == "hashtag")
    tags = max(len(TAG_RE.findall(text)), tag_frags)

    reply_to = ""
    rta = info.get("reply_to_author")
    if isinstance(rta, dict):
        reply_to = rta.get("username") or ""

    ts = datetime.fromtimestamp(int(p["taken_at"]), tz=timezone.utc)
    flat = text.replace("\t", " ").replace("\r", "").replace("\n", " / ")
    return {
        "code": p["code"],
        "utc": ts.strftime("%Y-%m-%d %H:%M"),
        "taiwan": ts.astimezone(TW).strftime("%Y-%m-%d %H:%M"),
        "likes": p.get("like_count") or 0,
        "replies": info.get("direct_reply_count") or 0,
        "reposts": info.get("repost_count") or p.get("repost_count") or 0,
        "media": media,
        "text": flat,
        "carousel_count": count,
        "has_video": int(has_video),
        "link_count": links,
        "hashtag_count": tags,
        "caption_length": len(text),
        "reply_to": reply_to,
    }


# ---------- 儲存 ----------

def load_codes(tsv):
    if not tsv.exists():
        return set()
    with tsv.open(encoding="utf-8", newline="") as f:
        return {r["code"] for r in csv.DictReader(f, delimiter="\t")}


def append_rows(tsv, rows):
    new_file = not tsv.exists()
    with tsv.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, delimiter="\t",
                           quoting=csv.QUOTE_NONE, escapechar="\\")
        if new_file:
            w.writeheader()
        w.writerows(rows)


# ---------- 抓取 ----------

class Collector:
    def __init__(self, account):
        self.account = account
        self.posts = {}          # code -> row（本次 session 看到的）
        self.profile = None
        self.has_next = None     # 最後一次分頁回應的 has_next_page
        self.rate_limited = False

    def feed(self, obj, from_graphql=False):
        for d in walk(obj):
            if is_post(d) and (d["user"].get("username") or "").lower() == self.account.lower():
                code = d["code"]
                if code not in self.posts:
                    try:
                        self.posts[code] = post_row(d)
                    except Exception as e:  # 單篇解析失敗不影響整體
                        log(f"  解析 {code} 失敗：{e}")
            elif (
                (d.get("username") or "").lower() == self.account.lower()
                and "follower_count" in d
            ):
                keep = {k: d.get(k) for k in (
                    "username", "full_name", "pk", "id", "biography", "follower_count",
                    "is_verified", "bio_links", "text_post_app_is_private",
                )}
                if self.profile is None or len(json.dumps(keep, default=str)) > len(json.dumps(self.profile, default=str)):
                    self.profile = keep
            if from_graphql and "has_next_page" in d and "edges" not in d:
                # 分頁回應的 page_info 物件（內嵌 JSON 的不算，避免誤判到底）
                self.has_next = bool(d.get("has_next_page"))


def human_pause(lo, hi):
    time.sleep(random.uniform(lo, hi))


def logged_in(context):
    return any(c["name"] == "sessionid" and c["value"] for c in context.cookies("https://www.threads.com"))


def scrape_account(page, account, out_root, args):
    out_dir = out_root / account
    out_dir.mkdir(parents=True, exist_ok=True)
    tsv = out_dir / "posts.tsv"
    known = load_codes(tsv)
    log(f"== @{account}：已有 {len(known)} 篇，開始捲動")

    col = Collector(account)

    def on_response(resp):
        url = resp.url
        if "/graphql" not in url and "/api/" not in url:
            return
        if resp.status == 429:
            col.rate_limited = True
            return
        try:
            ctype = resp.headers.get("content-type", "")
            if "json" not in ctype and "javascript" not in ctype and "text" not in ctype:
                return
            for obj in parse_json_text(resp.text()):
                col.feed(obj, from_graphql="/graphql" in url)
        except Exception:
            pass

    page.on("response", on_response)
    try:
        page.goto(f"https://www.threads.com/@{account}", wait_until="domcontentloaded", timeout=60000)
        human_pause(4, 6)
        # 頁面內嵌 JSON（前 15 篇與個人資料）
        for raw in page.eval_on_selector_all(
            'script[type="application/json"]', "els => els.map(e => e.textContent)"
        ):
            for obj in parse_json_text(raw or ""):
                col.feed(obj)

        written = 0
        idle = 0
        last_total = -1
        scrolls = 0
        while True:
            fresh = [r for c, r in col.posts.items() if c not in known]
            if fresh:
                fresh.sort(key=lambda r: r["utc"], reverse=True)
                append_rows(tsv, fresh)
                known.update(r["code"] for r in fresh)
                written += len(fresh)
                oldest = min(r["taiwan"] for r in col.posts.values())
                log(f"  +{len(fresh)} 篇（本次共新增 {written}，檔案共 {len(known)}；目前看到最早 {oldest}）")

            if args.max and written >= args.max:
                log(f"  到達 --max {args.max}，停止")
                break
            if col.rate_limited:
                log("  ⚠ 收到 429（被限速）。已存檔，請隔幾小時或隔天再跑，會從斷點接著抓。")
                break

            total = len(col.posts)
            if total == last_total:
                idle += 1
            else:
                idle = 0
                last_total = total
            if col.has_next is False and idle >= 3:
                log("  分頁回報 has_next_page=false：已到帳號第一篇")
                break
            if idle >= args.idle_rounds:
                log(f"  連續 {idle} 次捲動沒有新貼文，視為到底")
                break

            page.mouse.wheel(0, random.randint(1400, 2600))
            scrolls += 1
            human_pause(args.min_delay, args.max_delay)
            if idle >= 3:
                # 卡住時往回一點再往下，觸發載入
                page.mouse.wheel(0, -random.randint(300, 600))
                human_pause(1, 2)
                page.keyboard.press("End")
                human_pause(args.min_delay, args.max_delay)
            if scrolls % 25 == 0:
                log("  休息一下（降低被限速機率）")
                human_pause(12, 25)
    finally:
        page.remove_listener("response", on_response)

    if col.profile:
        prof = dict(col.profile)
        prof["scraped_at_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
        prof["posts_in_tsv"] = len(known)
        (out_dir / "profile.json").write_text(
            json.dumps(prof, ensure_ascii=False, indent=2, default=str), encoding="utf-8"
        )
    log(f"== @{account} 完成：本次新增 {written} 篇，檔案共 {len(known)} 篇 → {tsv}")
    return not col.rate_limited


def main():
    ap = argparse.ArgumentParser(description="抓 Threads 帳號全部歷史貼文（文字與數字）")
    ap.add_argument("accounts", nargs="*", help=f"帳號名（不含 @），預設：{' '.join(DEFAULT_ACCOUNTS)}")
    ap.add_argument("--out", default=str(Path.home() / "luscena_benchmarks"), help="輸出資料夾（repo 外）")
    ap.add_argument("--profile", default=str(Path.home() / ".luscena_threads_profile"), help="瀏覽器設定檔（repo 外）")
    ap.add_argument("--login", action="store_true", help="只開瀏覽器讓你登入，登入後按 Enter 結束")
    ap.add_argument("--max", type=int, default=0, help="每個帳號本次最多新增幾篇（測試用；0＝不設上限）")
    ap.add_argument("--idle-rounds", type=int, default=8, help="連續幾次捲動沒新貼文就視為到底")
    ap.add_argument("--min-delay", type=float, default=2.0)
    ap.add_argument("--max-delay", type=float, default=4.0)
    ap.add_argument("--account-gap", type=float, default=60.0, help="帳號之間休息秒數")
    args = ap.parse_args()

    accounts = [a.lstrip("@") for a in (args.accounts or DEFAULT_ACCOUNTS)]
    out_root = Path(args.out).expanduser()
    out_root.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        ctx = pw.chromium.launch_persistent_context(
            str(Path(args.profile).expanduser()),
            headless=False,
            viewport={"width": 1280, "height": 900},
            locale="zh-TW",
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        if args.login or not logged_in(ctx):
            page.goto("https://www.threads.com/login", wait_until="domcontentloaded")
            print("\n請在開出來的瀏覽器視窗登入 Threads『副帳號』（不要用主帳號）。")
            input("登入完成、看得到首頁後，回到這裡按 Enter 繼續… ")
            if not logged_in(ctx):
                print("偵測不到登入狀態（沒有 sessionid cookie）。請確認已登入再重跑。")
                ctx.close()
                sys.exit(1)
            if args.login:
                print("登入狀態已存在設定檔，之後執行不用再登入。")
                ctx.close()
                return

        for i, acc in enumerate(accounts):
            ok = scrape_account(page, acc, out_root, args)
            if not ok:
                log("被限速，後面的帳號這次不抓。")
                break
            if i < len(accounts) - 1:
                log(f"帳號之間休息 {args.account_gap:.0f} 秒")
                time.sleep(args.account_gap)
        ctx.close()


if __name__ == "__main__":
    main()
