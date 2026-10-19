# Threads 對標抓取工具

本資料夾有兩種抓法，2026-10-19 實際用的是 **B. Chrome 版**（製作師要用自己已登入的 Chrome，不另開瀏覽器）。

| 檔案 | 用途 |
|---|---|
| `threads_scrape.py` | A. Playwright 版：另開一個 Chromium、用獨立設定檔登入（第 1–6 節） |
| `threads_chrome_collect.js` | B. Chrome 版：在已登入 Threads 的 Chrome 分頁裡執行的收集腳本（第 7 節） |
| `read_chrome_localstorage.py` | B. Chrome 版：從 Chrome 的 Local Storage 檔案讀出收集結果（第 7 節） |
| `analyze_threads.py` | 分析：同期中位數倍數、前 10% 高流量、各特徵比例 |

## A. Playwright 版

`threads_scrape.py`：在製作師本機，用登入的 Threads **副帳號**打開對標帳號主頁，慢慢往下捲，記錄頁面收到的貼文資料（文字與數字），一路抓到該帳號的第一篇。

- 只讀：不按讚、不留言、不追蹤、不開私訊、不下載圖片。
- 瀏覽器設定檔（含登入狀態）與輸出都放在 repo 外；只有分析用的 TSV（文字與數字）之後會複製進 `production/benchmarks/<日期>_threads/`。

## 1. 安裝（一次）

需要 Python 3.10 以上。PowerShell：

```
python -m pip install playwright
python -m playwright install chromium
```

不需要 pillow（工具不處理圖片）。

## 2. 第一次登入

```
python production/benchmarks/tools/threads_scrape.py --login
```

1. 會開出一個有畫面的 Chromium，停在 Threads 登入頁。
2. 在那個視窗登入 **副帳號**（不要用主帳號）。可以用 Instagram 帳號登入。
3. 看到 Threads 首頁後，回到終端機按 Enter。登入狀態存在 `~/.luscena_threads_profile`，之後不用再登入。

帳密由製作師自己輸入，工具不讀、不存帳密。

## 3. 抓取

依預設順序（yuan.ruoting → mina_ya2002 → eiko.smiles → arielanailife），每個帳號不設上限、一路抓到第一篇：

```
python production/benchmarks/tools/threads_scrape.py
```

只抓指定帳號：

```
python production/benchmarks/tools/threads_scrape.py yuan.ruoting
```

測試（每個帳號本次只新增 20 篇）：

```
python production/benchmarks/tools/threads_scrape.py yuan.ruoting --max 20
```

其他參數：`--out`（輸出資料夾，預設 `~/luscena_benchmarks`）、`--profile`（設定檔位置）、`--min-delay`／`--max-delay`（每次捲動間隔，預設 2–4 秒隨機）、`--idle-rounds`（連續幾次捲動沒新貼文就視為到底，預設 8）、`--account-gap`（帳號之間休息秒數，預設 60）。

執行時請讓瀏覽器視窗留著，不要手動操作它；終端機會顯示每批新增篇數與目前看到最早的日期。

## 4. 停止條件與續抓

- 停止：分頁回報 `has_next_page=false`（已到第一篇，且之後連續 3 次捲動沒新貼文）、連續 8 次捲動沒有新貼文、到達 `--max`、或收到 429 限速。
- 每抓到一批就立刻寫進 `posts.tsv`；中斷（Ctrl+C、關視窗、被限速）後重跑同一指令，已有的 `code` 會跳過。
- 續抓時仍要從頁首往下捲過已抓的部分，只是不會重複寫入。舊貼文的讚數是「第一次抓到時」的數字。
- 被限速時工具會停下並存檔；請隔幾小時或隔天再跑。

## 5. 輸出

`~/luscena_benchmarks/<帳號>/`

- `posts.tsv`：欄位 `code, utc, taiwan, likes, replies, reposts, media, text`（與 repo 既有 TSV 相同；換行改成 ` / `），另加：
  - `carousel_count`：圖片／影片張數（純文字 0）
  - `has_video`：0／1（輪播內有影片也算 1）
  - `link_count`：文案中的連結數（有連結預覽卡也算 1）
  - `hashtag_count`：文案中的 hashtag 數
  - `caption_length`：文案字數
  - `reply_to`：若是回覆串中的貼文，回覆對象的帳號名（自己接自己的串會是自己的帳號）
- `profile.json`：帳號名、名稱、自介、追蹤數、外連、抓取時間、TSV 篇數。

## 6. 風險（請先讀）

- **違反 Meta 使用條款的可能**：Threads 條款禁止未經許可的自動化收集資料。用這個工具有被限速、要求驗證、或帳號被停用的可能。
- **一律用副帳號**：不要用製作師主帳號或客戶帳號；副帳號被停不影響正式帳號。
- **慢速、一次少量**：每次捲動間隔 2–4 秒隨機、每 25 次休息 12–25 秒、帳號之間休息 60 秒。不要調快。第一次建議先跑 `--max 20` 看是否正常。一天內不要反覆重跑；被限速就隔天再接著抓。
- **只讀**：工具不按讚、不留言、不追蹤、不開私訊；捲動期間請不要用這個視窗做其他事。
- **資料處理**：設定檔（含登入 cookie）與對方圖片一律不進 repo；進 repo 的只有文字與數字的 TSV 與分析報告。
- 介面改版：Threads 改版可能讓工具抓不到資料（每批新增 0 篇、很快停止）。遇到時告訴執行者修。

## 7. B. Chrome 版（2026-10-19 實際使用）

由 Claude 透過 Claude in Chrome 在製作師已登入 Threads 的 Chrome 分頁執行。2026-10-19 用的帳號是製作師指定的 @zhangqinfeng61（製作師確認接受風險）。

1. 打開 `https://www.threads.com/`（首頁），在該分頁執行 `threads_chrome_collect.js` 全文。腳本會攔截頁面的 `/graphql` 回應（只讀副本）。
2. **用頁內切換進入對方主頁**：`history.pushState` 到 `/@帳號` 再觸發 `popstate`。不要直接重新載入主頁：重新載入時，第一批約 10 篇會在腳本裝好之前就載完而漏抓（2026-10-19 第一輪就漏了這段，後來用頁內切換補回）。
3. `__lusStart('<帳號>', 0)` 開始捲動（2–4 秒隨機，每 25 次休息 12–25 秒），抓到 `has_next_page=false` 為止。`__lusStatus()` 看進度。
4. 結束時結果存進 threads.com 的 localStorage（`__lus_<帳號>`），換頁不會遺失。
5. 取出：Chrome 會擋同一網站的第二次自動下載，頁面回傳的文字也有長度上限，所以改從硬碟讀：
   ```
   python -I read_chrome_localstorage.py "<Chrome 設定檔>\Local Storage\leveldb 的複本資料夾" <輸出資料夾>
   ```
   先把 `leveldb` 裡的 `.ldb`、`.log` 複製到另一個資料夾再讀。Chrome 寫入硬碟會延遲幾分鐘，剛抓完可能還讀不到。
6. 用完請清掉 localStorage 裡的 `__lus_*`、`__lustag_*`。

收集欄位多了 `topic_tag`（貼文掛的 Threads 話題／社群標籤，來自 `text_post_app_info.tag_header.display_name`）。
