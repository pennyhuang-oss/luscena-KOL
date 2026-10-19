# 交接：Threads 對標工作（2026-10-19；同日更新：加 yuan.ruoting 為最優先、抓全部歷史、只要文字結論）

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
  - 參數：帳號名（可多個）；**預設不設篇數上限，一路捲到帳號的第一篇**（連續數次捲動沒有新貼文、或已看到最早一篇時才停）；可選 `--max` 只在測試時用。
  - 打開 `https://www.threads.com/@<帳號>`，監聽 `/graphql/query` 與頁面內嵌 JSON，慢慢往下捲（每次間隔 2–4 秒隨機）。
  - **可中斷續抓**：每抓到一批就寫入本機的 `posts.tsv`，重跑時跳過已有的 `code`；被限制或中斷時隔天接著抓。
  - 輸出到 repo 外的資料夾（例如 `~/luscena_benchmarks/<帳號>/`）：`posts.tsv`（與現有 TSV 同欄位，另加 `carousel_count`、`has_video`、`link_count`、`hashtag_count`、`caption_length`）、`profile.json`。圖片不用下載；若要判斷圖片內容，只在本機看，不進 repo、不貼給製作師。
- `README.md`：安裝（`pip install playwright pillow`、`playwright install chromium`）、第一次登入、指令範例、風險說明。
- 風險說明要寫清楚：違反 Meta 使用條款的可能、要用副帳號、慢速、一次少量。

### 任務 B：用工具抓全部歷史貼文，找出高流量公式

- 帳號（依優先順序）：**`yuan.ruoting`（製作師 2026-10-19 指定，最優先）**、`mina_ya2002`、`eiko.smiles`、`arielanailife`。累計篇數約 186／225／355／222。
- **不設上限，一路抓到每個帳號的第一篇，越多越好。**
- 把 TSV（只有文字與數字）複製進 `production/benchmarks/<日期>_threads/`。
- 分析與報告（寫成新報告，舊報告不改）：
  1. 每篇分類：主題（美食／景點／廟宇信仰／節日／穿搭／運動／動物／工作／自拍日常…）、場景（在地地名或店名有無）、格式（單圖／輪播張數／影片）、文案長度與句型（問句、自嘲、對話、長日記）、擦邊程度（無／輕／中）、發文時段、星期。
  2. 互動指標：讚、回覆、轉發；用「該帳號同期中位數」做基準，算每篇的倍數，標出前 10% 為高流量。
  3. 找共通點：高流量貼文在上述欄位的比例 vs 全部貼文的比例；看帳號成長期（早期 vs 近期）公式有沒有變。
  4. **結論寫成文字，不附圖片**：每個帳號「哪幾類貼文流量最高」、「高流量公式」（例：在地地名＋節日＋長文案＋單圖＋早上 7 點）、「我們十個帳號可以怎麼模仿」（對應到先鋒四人與其餘角色），以及「不要學的」。
- 給製作師的回報只要文字敘述與數字，不貼圖片。

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
