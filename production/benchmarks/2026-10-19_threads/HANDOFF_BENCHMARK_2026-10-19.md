# 交接：Threads 對標工作（2026-10-19）

給下一個 session 的 Claude。製作師：Vincent Chiu。分支：`producer/modeling-r1`。
**這份工作要在製作師的本機 Claude Code 執行**（需要用製作師的瀏覽器登入 Threads），雲端 session 做不到。

## 0. 先讀

1. `CLAUDE.md`、`README.md`「Repo 規則」。
2. `production/benchmarks/2026-10-19_threads/BENCHMARK_mina_eiko_2026-10-19.md`（mina、eiko 分析與對我們的啟示）。
3. `production/benchmarks/2026-10-19_threads/CANDIDATE_SEARCH_2026-10-19.md`（找擦邊更重帳號的第一輪結果）。
4. 同資料夾四個 `*_posts_2026-10-19.tsv`（欄位：code、utc、taiwan、likes、replies、reposts、media、text）。

## 1. 已知事實

- 未登入讀 Threads：每個分頁（主頁、回覆、媒體）只給最近 15 篇，`page_info.has_next_page=false`。
- 公開頁的貼文資料在 `<script type="application/json">` 內嵌 JSON；貼文物件有 `code`、`taken_at`、`caption.text`、`like_count`、`text_post_app_info.direct_reply_count`、`repost_count`、`carousel_media`、`video_versions`、`image_versions2`。
- 分頁查詢叫 `BarcelonaProfileThreadsTabRefetchableDirectQuery`（root field `xdt_api__v1__text_feed__user_id__profile__connection`，變數 `userID`、`first`、`after`）。登入後捲動頁面時，瀏覽器會打 `/graphql/query` 拿下一批，回應裡就是同樣的貼文物件。
- 帳號 user id：mina_ya2002 = 34647226617；eiko.smiles = 77687763392。

## 2. 任務

### 任務 A：本機自動抓取工具（先做）

在 `production/benchmarks/tools/` 新增：
- `threads_scrape.py`（Python＋Playwright）：
  - 用持久化瀏覽器設定檔（例如 `~/.luscena_threads_profile`，**不放進 repo**），第一次執行開出有畫面的 Chromium，等製作師手動登入 Threads 副帳號後按 Enter 繼續。
  - 參數：帳號名（可多個）、最多篇數（預設 100）、最早日期（預設 90 天前）。
  - 打開 `https://www.threads.com/@<帳號>`，監聽 `/graphql/query` 與頁面內嵌 JSON，慢慢往下捲（每次間隔 2–4 秒隨機），收到足夠篇數或到最早日期就停。
  - 輸出到 repo 外的資料夾（例如 `~/luscena_benchmarks/<日期>/<帳號>/`）：`posts.tsv`（與現有 TSV 同欄位）、`profile.json`、圖片縮圖表 `contact.jpg`。圖片只存本機。
- `README.md`：安裝（`pip install playwright pillow`、`playwright install chromium`）、第一次登入、指令範例、風險說明。
- 風險說明要寫清楚：違反 Meta 使用條款的可能、要用副帳號、慢速、一次少量。

### 任務 B：用工具抓四個帳號

- `mina_ya2002`、`eiko.smiles`、`yuan.ruoting`、`arielanailife`，各抓到 100 篇或 90 天。
- 把 TSV（只有文字與數字，不含圖片）複製進 `production/benchmarks/<日期>_threads/`。
- 更新統計：發文時段、媒體比例、讚／回覆分布、爆款共通點；寫成新報告，舊報告不改。

### 任務 C：找擦邊更重的 AI 帳號

- 用登入狀態搜尋絲襪、美腿、OL、AI 寫真、「AI生成」等話題與投稿串；每輪看 50–100 個帳號。
- 判斷 AI 的依據：自介揭露、或圖片明顯生成（五官過度一致、背景文字錯亂、手指異常）；寫明判斷依據。
- 找到 1–3 個後照任務 B 的格式分析，補成三角比較。也可以直接用製作師提供的帳號名。

### 任務 D（之後，看製作師）

- 把對標結論寫進十人的語氣與題目文件（新檔案，不改 `content_pack_v1/`）。

## 3. 規則

- 只新增檔案；不改 `persona_pack_v1/`、`review/`、既有報告；不 force push、不改寫歷史；推送前先 `git fetch` 並 rebase 到最新的 `origin/producer/modeling-r1`（雲端 session 也在推這個分支）。
- 對方的圖片、登入資料、瀏覽器設定檔一律不進 repo。
- 不用製作師的主帳號抓取；不碰私訊、不按讚、不留言、不追蹤。
- 每輪結束 commit＋push，報告存 GitHub、不貼聊天。
