"""Threads 對標貼文分析：讀 posts.tsv，標記主題／格式／句型／時段，算同期中位數倍數，比較高流量（前 10%）與全部的比例。

用法：python analyze_threads.py <posts.tsv> [<posts.tsv> ...] [--md out.md]
主題與句型是關鍵字規則（粗分），擦邊程度需看圖，不在此判斷。
"""

import argparse
import csv
import re
import statistics
from collections import Counter
from datetime import datetime
from pathlib import Path

TOPICS = [  # (主題, 關鍵字)；一篇可多個主題
    ("AI自揭", r"\bai\b|AI|人工智慧|生成|虛擬"),
    ("廟宇信仰", r"廟|宮|媽祖|聖母|進香|遶境|拜拜|月老|王爺|土地公|觀音|佛|神明|求籤|祈福|平安符|香火|三太子|關公|城隍|天后"),
    ("節日", r"節|中秋|端午|重陽|七夕|國慶|雙十|元宵|過年|新年|春節|聖誕|萬聖|跨年|情人節|母親節|父親節|教師節|連假|生日"),
    ("美食", r"吃|美食|餐|飯|麵|包子|便當|咖啡|奶茶|飲料|甜點|蛋糕|早餐|午餐|晚餐|宵夜|小吃|火鍋|燒肉|拉麵|夜市|好吃|滷|湯|茶|豆花|冰|喝"),
    ("景點戶外", r"步道|山|海|溪|橋|湖|公園|老街|景|風景|夕陽|日出|花|櫻|楓|旅行|旅遊|出遊|散步|走走|爬山|露營|沙灘|海邊|看海|瀑布|森林|天空"),
    ("穿搭", r"穿|衣|褲|裙|搭|OOTD|ootd|外套|洋裝|絲襪|黑絲|白絲|小可愛|背心|制服|泳|比基尼|內衣"),
    ("運動", r"運動|跑|健身|瑜伽|球|游泳|騎|重訓|伸展|晨跑|夜跑|籃球|棒球|羽球|網球"),
    ("動物", r"狗|貓|柯基|寵物|毛孩|鳥|兔|鴨|魚|喵|汪|牠"),
    ("工作上班", r"上班|下班|工作|同事|老闆|主管|辦公|加班|開會|薪水|請假|OL|office"),
    ("長輩家人", r"阿嬤|阿公|奶奶|爺爺|媽媽|爸爸|老爸|老媽|家人|長輩|婆婆|姊姊|妹妹|弟弟|哥哥|親戚"),
    ("遊戲童年", r"遊戲|機台|快打|夾娃娃|電玩|童年|小時候|以前|懷舊|回憶"),
    ("天氣季節", r"天氣|冷|熱|下雨|颱風|秋天|冬天|夏天|春天|太陽|陽光"),
    ("早安問候", r"早安|晚安|午安|星期一|週一|禮拜一|新的一週|大家好"),
]
PLACE_RE = re.compile(
    r"台北|臺北|新北|桃園|台中|臺中|台南|臺南|高雄|基隆|新竹|苗栗|彰化|南投|雲林|嘉義|屏東|宜蘭|花蓮|台東|臺東|澎湖|金門|馬祖|"
    r"[一-鿿]{1,4}(?:區|鄉|鎮|站|夜市|老街|步道|山|溪|橋|湖|港|宮|廟|寺|公園|商圈|本舖|本店|店)"
)
QUESTION_RE = re.compile(r"[?？]|嗎|呢|有沒有|誰|哪|什麼|舉手|你們|大家.{0,6}(?:覺得|會|有)")
SELFMOCK_RE = re.compile(r"🤣|😂|哈哈|笑死|我靠|崩潰|傻眼|欸|累|懶|不想|爆炸|慘")
DIALOGUE_RE = re.compile(r"「|」|說[:：]|[:：]\s*\S|問我|跟我說|說我")
WEEK = "一二三四五六日"


def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    for r in rows:
        for k in ("likes", "replies", "reposts", "caption_length", "carousel_count", "has_video", "link_count", "hashtag_count"):
            r[k] = int(r.get(k) or 0)
        r["dt"] = datetime.strptime(r["taiwan"], "%Y-%m-%d %H:%M")
    rows = [r for r in rows if not r.get("reply_to")]  # 串文回覆不算獨立貼文
    rows.sort(key=lambda r: r["dt"])
    return rows


def tag(r):
    t = r["text"]
    r["topics"] = [name for name, pat in TOPICS if re.search(pat, t)] or ["其他"]
    r["place"] = bool(PLACE_RE.search(t))
    n = r["carousel_count"]
    r["format"] = "影片" if r["media"] == "video" else ("純文字" if n == 0 else ("單圖" if n == 1 else ("2張" if n == 2 else "3張以上")))
    L = r["caption_length"]
    r["len"] = "≤20字" if L <= 20 else ("21–60字" if L <= 60 else ("61–120字" if L <= 120 else ">120字"))
    r["question"] = bool(QUESTION_RE.search(t))
    r["selfmock"] = bool(SELFMOCK_RE.search(t))
    r["dialogue"] = bool(DIALOGUE_RE.search(t))
    h = r["dt"].hour
    r["slot"] = "05–08" if 5 <= h < 9 else ("09–11" if h < 12 else ("12–17" if h < 18 else ("18–21" if h < 22 else "22–04")))
    r["weekday"] = "週" + WEEK[r["dt"].weekday()]
    r["tag"] = (r.get("topic_tag") or "").strip()


def baseline(rows, key, half=15):
    """同期基準：前後各 half 篇（含自己）的中位數。"""
    out = []
    for i in range(len(rows)):
        win = [x[key] for x in rows[max(0, i - half): i + half + 1]]
        out.append(max(statistics.median(win), 1))
    return out


def share(rows, pred):
    return 100 * sum(1 for r in rows if pred(r)) / len(rows) if rows else 0


def lift_table(rows, high, feats):
    lines = ["| 特徵 | 值 | 全部 % | 高流量 % | 倍數 |", "|---|---|---|---|---|"]
    for label, values, getter in feats:
        for v in values:
            pa = share(rows, lambda r: getter(r, v))
            ph = share(high, lambda r: getter(r, v))
            if pa == 0 and ph == 0:
                continue
            lift = ph / pa if pa else float("inf")
            lines.append(f"| {label} | {v} | {pa:.0f} | {ph:.0f} | {lift:.2f} |")
    return "\n".join(lines)


def analyze(path):
    rows = load(path)
    acc = Path(path).parent.name
    for r in rows:
        tag(r)
    for key in ("likes", "replies"):
        bl = baseline(rows, key)
        for r, b in zip(rows, bl):
            r[f"{key}_x"] = r[key] / b
    # 綜合分數：讚倍數為主，回覆倍數為輔
    for r in rows:
        r["score"] = 0.7 * r["likes_x"] + 0.3 * r["replies_x"]
    ranked = sorted(rows, key=lambda r: r["score"], reverse=True)
    k = max(1, round(len(rows) * 0.10))
    high = ranked[:k]
    high_codes = {r["code"] for r in high}

    out = [f"## {acc}", ""]
    likes = [r["likes"] for r in rows]
    reps = [r["replies"] for r in rows]
    out.append(f"- 獨立貼文 {len(rows)} 篇（{rows[0]['taiwan'][:10]} → {rows[-1]['taiwan'][:10]}）；"
               f"讚 中位 {statistics.median(likes):.0f}／平均 {statistics.mean(likes):.0f}／最高 {max(likes)}；"
               f"回覆 中位 {statistics.median(reps):.0f}；高流量＝綜合倍數前 10%（{k} 篇，門檻 {high[-1]['score']:.2f}x）")
    # 月份走勢
    months = Counter(r["taiwan"][:7] for r in rows)
    trend = []
    for m in sorted(months):
        ms = [r for r in rows if r["taiwan"][:7] == m]
        trend.append(f"{m}: {len(ms)}篇 讚中位{statistics.median([r['likes'] for r in ms]):.0f} 回覆中位{statistics.median([r['replies'] for r in ms]):.0f}")
    out.append("- 月份：" + "；".join(trend))
    out.append("")

    topic_names = [n for n, _ in TOPICS] + ["其他"]
    feats = [
        ("主題", topic_names, lambda r, v: v in r["topics"]),
        ("在地地名店名", [True], lambda r, v: r["place"] == v),
        ("格式", ["單圖", "2張", "3張以上", "影片", "純文字"], lambda r, v: r["format"] == v),
        ("文案長度", ["≤20字", "21–60字", "61–120字", ">120字"], lambda r, v: r["len"] == v),
        ("問句", [True], lambda r, v: r["question"] == v),
        ("自嘲", [True], lambda r, v: r["selfmock"] == v),
        ("對話引述", [True], lambda r, v: r["dialogue"] == v),
        ("hashtag", [True], lambda r, v: (r["hashtag_count"] > 0) == v),
        ("話題標籤", [True], lambda r, v: bool(r["tag"]) == v),
        ("時段", ["05–08", "09–11", "12–17", "18–21", "22–04"], lambda r, v: r["slot"] == v),
        ("星期", ["週" + w for w in WEEK], lambda r, v: r["weekday"] == v),
    ]
    out.append("### 高流量 vs 全部（比例）")
    out.append(lift_table(rows, high, feats))
    out.append("")
    if any(r["tag"] for r in rows):
        allc = Counter(r["tag"] for r in rows if r["tag"])
        out.append("- 話題標籤（全部前 12）：" + "、".join(f"{t}×{n}" for t, n in allc.most_common(12)))
        out.append("- 話題標籤（高流量）：" + "、".join(f"{t}×{n}" for t, n in Counter(r["tag"] for r in high if r["tag"]).most_common(12)))
        tagmed = []
        for t, n in allc.most_common(15):
            if n >= 4:
                tagmed.append(f"{t}（{n}篇，綜合倍數中位 {statistics.median([r['score'] for r in rows if r['tag'] == t]):.2f}）")
        out.append("- 常用標籤的表現：" + "；".join(tagmed))
        out.append("")

    # 早期 vs 近期
    mid = len(rows) // 2
    for label, part in (("前半（早期）", rows[:mid]), ("後半（近期）", rows[mid:])):
        pr = sorted(part, key=lambda r: r["score"], reverse=True)[:max(1, round(len(part) * 0.10))]
        tc = Counter(t for r in pr for t in r["topics"]).most_common(4)
        fc = Counter(r["format"] for r in pr).most_common(2)
        lc = Counter(r["len"] for r in pr).most_common(2)
        out.append(f"- {label} {part[0]['taiwan'][:10]}→{part[-1]['taiwan'][:10]}：讚中位 {statistics.median([r['likes'] for r in part]):.0f}；"
                   f"高流量主題 {tc}；格式 {fc}；長度 {lc}")
    out.append("")

    out.append("### 高流量貼文")
    out.append("| 台灣時間 | 讚 | 回覆 | 讚倍數 | 回覆倍數 | 格式 | 主題 | 文案 |")
    out.append("|---|---|---|---|---|---|---|---|")
    for r in high:
        txt = r["text"].replace("|", "｜")
        txt = txt if len(txt) <= 70 else txt[:70] + "…"
        out.append(f"| {r['taiwan']} | {r['likes']} | {r['replies']} | {r['likes_x']:.1f} | {r['replies_x']:.1f} | "
                   f"{r['format']} | {'、'.join(r['topics'])}{(' #' + r['tag']) if r['tag'] else ''} | {txt} |")
    out.append("")
    out.append("### 最低 10%")
    for r in ranked[-k:]:
        out.append(f"- {r['taiwan']} 讚{r['likes']} 回{r['replies']} {r['format']} {'、'.join(r['topics'])}：{r['text'][:50]}")
    out.append("")
    return "\n".join(out), rows, high_codes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--md")
    args = ap.parse_args()
    parts = [analyze(f)[0] for f in args.files]
    text = "\n\n".join(parts)
    if args.md:
        Path(args.md).write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
