# Threads 公開帳號抽樣與 Meta 官方規則查核

- 查核日期：2026-10-06（觀察時間戳一律為 UTC；台北時間 = UTC+8）
- 範圍：Part A 是公開 Threads 帳號抽樣，Part B 是 Meta 官方規則查核，C 到 E 是推論、風險與未確認事項
- 證據編號：Threads 樣本為 EV-T01～EV-T25，Meta 官方來源為 EV-M01～EV-M34，完整清單見 `research/EVIDENCE_INDEX.md` 附錄
- 本研究沒有建立帳號、沒有登入，也沒有按讚、留言、追蹤、私訊或付費
- **公開互動數（讚、留言、轉發、分享、瀏覽）不能證明網站點擊、轉換或營收。** 本文所有互動數只代表查核當下頁面上顯示的數字。

---

## 0 方法與限制

### 0.1 工具與實際結果

| 方法 | 結果（原始訊息） | 處理方式 |
|---|---|---|
| WebSearch `site:threads.com 星座 運勢`、`site:threads.com 啦啦隊 中職 女孩` 等 | 沒有回傳任何 threads.com 網址，只回傳新聞或其他網站 | 改用 Threads 站內搜尋（未登入） |
| `curl https://www.threads.com/@zuck` | HTTP 200，但 HTML 只有外殼（`<title>Threads</title>`），沒有個人頁資料 | 改用 Playwright 無頭 Chromium |
| Playwright 開啟 `https://www.threads.com/@{handle}`（未登入） | 可以讀到顯示名稱、簡介、粉絲數、簡介連結，以及約 4～11 個貼文容器（含讚、留言、轉發、分享數）；往下捲 16 次仍維持約 8 個容器 | 抽樣窗口就是「未登入可見的最近 4～11 個貼文容器」 |
| Playwright 開啟貼文頁 `/@{handle}/post/{id}` | 可以看到「N 次瀏覽」和部分留言，之後顯示「登入即可查看更多回覆。」 | 每個帳號挑 2～3 篇開貼文頁記錄瀏覽數 |
| 影片貼文 | 無頭瀏覽器顯示「很抱歉，播放此影片時發生問題。」 | 只記錄格式是影片，沒有看內容 |
| Threads 搜尋 `https://www.threads.com/search?q=…`（未登入） | 多數關鍵字有結果；「虛擬網紅」「人像攝影師」「攝影師接案」回「查無結果。」 | 拿來找候選帳號（EV-T14） |
| @ettoday、@tvbsnews、@mirrormedia.mg、@4gamers_tw、@horo.ariestw、@horo.scorpiotw | 轉到 `https://www.threads.com/login/?next=…`，og:title 為「Threads • 登入」 | 無法判斷是帳號不存在還是登入牆，列為失敗（EV-T17） |
| `curl https://www.instagram.com/1212laowu/` | HTTP 429，轉到 `…/accounts/login/?next=…&is_from_rle` | IG 落地頁無法觀察（EV-T25） |
| `curl https://ig.me/j/…` | HTTP 400，標題「Error」 | 落地頁未確認 |
| `curl https://transparency.meta.com/...sexual-solicitation/` | HTTP 400，回應內容只有「Error」 | 改用 Playwright 渲染官方頁面 |
| help.instagram.com/1666837803804595 | 「This information isn't available in your area.」 | 這一條列為未確認（EV-M15） |
| help.instagram.com/788669719351544（About Threads） | 轉到 Threads 政策分類頁 280495901606863 | 改用「Create a profile on Threads」等子頁（EV-M12） |

### 0.2 抽樣規則

1. 先用未登入搜尋「星座」「兩性」「cosplay」「健身穿搭」「梗圖」「迷因」「手遊課金」「AI工具」「啦啦隊」「NBA」「中職」「味全龍」「人像攝影」「外拍」「爆料」「AI網紅」等關鍵字找候選帳號，再開個人頁確認。
2. 排除條件：有露骨性內容；看起來是未成年人或無法確認是否成年；內容主要是幼兒（例如 @wengxying 近期主要是嬰兒日常）；帳號剛建立、沒有粉絲（開啟過但排除的帳號列在 EV-T16）。
3. 每個帳號記錄未登入可見的完整窗口（4～11 個容器），再挑 2～3 篇開貼文頁。挑選原則是「1 篇釘選或高峰文」加上「1～2 篇一般文」，並逐篇標註類型，避免只挑爆紅文。
4. 粉絲數以頁首顯示為準，meta 描述的數字不同時並列（例如 @isaac.startup 頁首寫 6 萬，meta 描述寫 6.8 萬）。

### 0.3 限制

- 只看了一個時間點：剛發不久的貼文（@setnews、@i.love.meowstars）瀏覽數一定偏低。
- 官方說明 Threads 的讚、回覆、轉發、引用、瀏覽等指標「still in development」（EV-M27），所以這些數字只能當作約略值。
- 私訊（DM）、洞察報告、連結點擊都看不到，因此所有「導流成效」都無法驗證。
- **自動化存取聲明**：這次用無頭瀏覽器開了約 33 個帳號頁、35 個貼文頁、36 次搜尋頁，都是公開頁面、量少，而且沒有登入或互動。但《Threads 使用條款》禁止用「robot, spider, crawlers, scraper…」蒐集資料（EV-M09），IG 條款也禁止未經許可的自動化蒐集，「regardless of whether…logged-in」（EV-M10）。之後如果要持續監測，建議改用人工，或只用官方 API 管理自己的帳號（標準權限無法查詢他人帳號，見 EV-M32）。

---

## A 帳號樣本

### A.1 樣本總表（12 個主樣本；觀察日期均為 2026-10-06）

| # | 帳號 | 方向（對應本案） | 粉絲（級距） | 選入理由 | EV |
|---|---|---|---|---|---|
| 1 | @1212laowu 那個老吳 | 兩性（A） | 1.0 萬（1萬～10萬） | 台灣兩性帳號，用私訊關鍵字導流 | EV-T01 |
| 2 | @guguhola1110 翔影 Cosplay | Cosplay（B） | 2.3 萬（1萬～10萬） | 台灣資深 Coser，內容不露骨，簡介寫明業配聯絡方式 | EV-T02 |
| 3 | @__9ann__ Joann Wu | 健身穿搭、性感網美定位（C） | 5,756（<1萬） | 自我定位「性感型健身網美」，同時做代購導購 | EV-T03 |
| 4 | @horo.taurustw 金牛座 | 星座（T1） | 4.6 萬（1萬～10萬） | 星座帳號系列，連到內容站和 App | EV-T04、T13 |
| 5 | @i.love.meowstars 喵星知我心 | 星座品牌角色（T1、角色導流） | 235（<1萬） | 品牌自營的擬人角色，導向品牌 App | EV-T05 |
| 6 | @classic.meme.daily 每日經典迷因 | 迷因（T2） | 3.8 萬（1萬～10萬） | 每日系列，固定格式 | EV-T06 |
| 7 | @littleveera1201 迷路的小薇菈 | 手遊（T3） | 5.6 萬（1萬～10萬） | 用插畫角色當形象的遊戲情報帳號 | EV-T07 |
| 8 | @isaac.startup Isaac Wong | AI 科技（T4） | 6萬～6.8萬（1萬～10萬） | AI 工具教學，導向電子報和付費產品 | EV-T08 |
| 9 | @tgsa999 YY叔叔 | 中職／運動（T5） | 53（<1萬） | 極小帳號卻有高瀏覽貼文 | EV-T09 |
| 10 | @jo_photos0777 酒安 | 外拍人像攝影（T6） | 1.0 萬（1萬～10萬） | 台北女攝影師，把溝通導到 IG | EV-T10 |
| 11 | @setnews 三立新聞網 | 時事新聞（T7） | 19 萬（>10萬） | 高頻發文，自己加短網址和 UTM | EV-T11 |
| 12 | @lilmiquela Miquela | 揭露身分的虛擬人物 | 35 萬（>10萬） | 簡介自稱「Robot」，外連音樂導購頁 | EV-T12 |

補充觀察（不算在主樣本內）：@imma.gram（7.6 萬，簡介寫「バーチャルヒューマン」）、@95fck_20（6,412，「每日一篇迷因 Day752」）、@don_design520（3,656，AI 行銷課程），見 EV-T15。

### A.2 逐帳號觀察

> 表格中的互動數順序為「讚／留言／轉發／分享」。這個順序已用貼文頁按鈕的 SVG title（讚、留言、轉發、分享）核對過。

#### A.2.1 @1212laowu（EV-T01）
- 網址：https://www.threads.com/@1212laowu ，觀察時間 07:03 UTC（個人頁）、07:19 UTC（貼文頁）
- 抽樣窗口：11 個容器，包含釘選的 4 段自串（2026-03-14），以及 2026-10-03 到 10-05 三組自串

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 釘選、高峰 | https://www.threads.com/@1212laowu/post/DV3GEzHDf9i | 2026-03-14 | 純文字，4 段自串 | 2.1萬/1,055/1,396/2,449 | 53萬 |
| CTA 段 | https://www.threads.com/@1212laowu/post/DeEYPzlE2x9 | 2026-10-04 | 純文字，3 段自串，最後一段是 CTA | 主文 388/42/35/45；CTA 段 11/0/0/0 | 3,066（不確定是單段還是整串） |
| 一般 | https://www.threads.com/@1212laowu/post/DeBzc-oj_SP | 2026-10-03 | 純文字，2 段 | 431/10/54/60 | 1.6萬 |

- 系列與語氣：用第二人稱「你」，描寫具體情境（LINE 很安靜、交友軟體只回「嗨」），自稱「老吳想跟你說」；主題標籤用「兩性相處」「單身」。觀察到的 4 天（3/14、10/3、10/4、10/5）都在台北 18:05 左右發文，推論可能有排程，但沒有證實。
- 連結與 CTA：簡介寫「1對1線上情感諮詢｜戀愛顧問…有問題歡迎私訊📩」，簡介連結是 instagram.com/1212laowu。串的最後一段寫：「私訊老吳「升級」我會傳一堂免費課程給你」，也就是私訊關鍵字換免費課程。私訊後的流程看不到。
- 落地頁：IG 回 HTTP 429，無法觀察。

#### A.2.2 @guguhola1110（EV-T02）
- 網址：https://www.threads.com/@guguhola1110 ，觀察時間 07:09 UTC。抽樣窗口只有 4 篇（09-24 到 10-04）。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 窗口內最高 | https://www.threads.com/@guguhola1110/post/DeEcGbtk44O | 2026-10-04 | 單圖加文字（外拍約兒，文末標註攝影師） | 908/44/6/17 | 7,627 |
| 一般 | https://www.threads.com/@guguhola1110/post/Dd8d2YOk9y9 | 2026-10-01 | 多圖（頁面偵測到 5 張，花火制服版） | 310/9/2/3 | 2,964 |
| 一般（生活） | https://www.threads.com/@guguhola1110/post/DdyY8ZoE6ji | 2026-09-27 | 2 張圖 | 116/17/0/1 | 2,102 |

- 語氣：自嘲、會玩角色梗（「純屬好玩請不要認真🙏」），作品文和家庭日常交錯發。09-24 有一篇回應 AI 生成 80 年代照片的風潮，寫「就不AI了，直接放1986年幼稚園照片」（255 讚），強調自己是真人。
- 連結與 CTA：簡介寫「業配宣傳、活動出席(全台可)請私訊❤️」「臉書活躍可互動，IG只是照片倉庫」，連結 IG（另有 1 個沒有展開）；窗口內沒有貼文附連結。

#### A.2.3 @__9ann__（EV-T03）
- 網址：https://www.threads.com/@__9ann__ ，觀察時間 07:14 UTC。抽樣窗口 6 篇。簡介寫「立志成爲性感型健身網美😳」「生活都在IG喲🤍」。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 釘選 CTA | https://www.threads.com/@__9ann__/post/DeCTpKAidPF | 2026-10-03 | 純文字加 ig.me/j/ 連結（「有開韓國健身服飾代購」） | 沒有顯示 | 344 |
| 窗口內最高 | https://www.threads.com/@__9ann__/post/DeGd6v7Cb3T | 2026-10-05 | 單圖，台股話題「國巨寶寶」 | 134/40/0/6 | 2.0萬 |
| 導購 | https://www.threads.com/@__9ann__/post/DeE2KEyiaD7 | 2026-10-04 | 純文字「商品在留言處」，再由作者自留言放商品圖和商店連結 | 11/26/0/0 | 1,897 |

- 觀察：主題混合健身、股票和代購；問句型或話題型貼文的留言數相對較高。導購連結放在釘選文和自留言裡，不放在主文。

#### A.2.4 @horo.taurustw（EV-T04），附 @horo.leotw（EV-T13）
- 網址：https://www.threads.com/@horo.taurustw ，觀察時間 07:10 UTC。顯示名稱是「金牛座（04/20～05/20）」，不是人名。抽樣窗口 6 篇。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 一般（純文字加自留言連結） | https://www.threads.com/@horo.taurustw/post/DeIqS2yE3Ki | 2026-10-06 10:00 台北 | 純文字；1 分鐘後作者自留言貼 horofriend88.com | 23/1/1/0 | 710 |
| 一般 | https://www.threads.com/@horo.taurustw/post/Dd-XINdk-Y8 | 2026-10-02 10:00 台北 | 純文字，同樣自留言貼連結 | 37/2/0/1 | 1,383 |
| 窗口內最高 | https://www.threads.com/@horo.taurustw/post/Dd_M82bG-1P | 2026-10-02 | 單張梗圖 | 134/5/2/12 | 2,120 |

- 連結與 CTA：簡介沒有文字，只有一個連結（agent.cfd888.info/r/msend/…），落地頁標題「Mivoo - 幫您每日運勢提升 36%」，內文「正在為您跳轉至App…」（EV-T18）。自留言的連結是「星座好朋友」的文章（EV-T19）。
- 同一系列：@horo.leotw（獅子座，4.4 萬粉絲）格式相同，也連到 horofriend88.com（EV-T13）。推論是同一經營者的星座帳號系列，把流量導到同一個內容站和 App，但經營者是誰未確認。

#### A.2.5 @i.love.meowstars（EV-T05）
- 網址：https://www.threads.com/@i.love.meowstars ，觀察時間 07:05 UTC。抽樣窗口 8 個容器，是 4 組「運勢主文加連結自留言」，每小時一組（台北 11:06 到 14:03）。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 窗口內最高 | https://www.threads.com/@i.love.meowstars/post/DeI5ZK-E0Kq | 2026-10-06 | 圖文（水瓶座運勢），結尾問「今天你把哪一段舊帳收起來了？喵～」 | 12/2/0/0 | 717 |
| 一般 | https://www.threads.com/@i.love.meowstars/post/DeJGJEblGjP | 2026-10-06 | 圖文（牡羊座運勢） | 6/1/1/0 | 327 |

- 角色設定：貓姥姥口吻（「老身幫你排喵～」）。落地頁是品牌 App「喵星知我心 貓咪星座命盤」活動頁，頁面寫「星座內容僅供娛樂與文化體驗」（EV-T20）。這是一個「品牌公開經營的角色帳號，導向自家產品」的例子，粉絲少，但每篇仍有數百次瀏覽。

#### A.2.6 @classic.meme.daily（EV-T06）
- 網址：https://www.threads.com/@classic.meme.daily ，觀察時間 07:04 UTC。抽樣窗口 8 個容器（4 組影片主文加出處自留言）。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 窗口內最高 | https://www.threads.com/@classic.meme.daily/post/DeCPkwfATrT | 2026-10-03 | 影片，倒數 Day92《斯斯》 | 981/31/89/174 | 1.9萬 |
| 一般 | https://www.threads.com/@classic.meme.daily/post/DeE2YYQgTQW | 2026-10-04 | 影片，Day91 | 799/4/41/182 | 2.1萬 |
| 偏低 | https://www.threads.com/@classic.meme.daily/post/Dd9C2c0gbwR | 2026-10-01 | 影片，Day93 | 103/2/3/0 | 2,788 |

- 系列：「每日一則經典迷因直到2027」，倒數天數，每晚台北 21:40 到 22:30 之間發。作者會自留言「影片來源：youtu.be/…」標註出處。分享數相對讚數偏高（182/799）。
- 連結與 CTA：簡介寫「追蹤ig以觀看相同內容」，連結 IG，等於把 Threads 當成 IG 的分流入口。

#### A.2.7 @littleveera1201（EV-T07）
- 網址：https://www.threads.com/@littleveera1201 ，觀察時間 07:14 UTC。抽樣窗口 8 篇。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 高峰 | https://www.threads.com/@littleveera1201/post/DeG8vAFj6J- | 2026-10-05 | 單圖，新造型情報 | 4,121/115/106/2,829 | 8.8萬 |
| 一般 | https://www.threads.com/@littleveera1201/post/DeGThEtD4Z1 | 2026-10-05 | 單圖，版本數據分析 | 364/16/2/100 | 2.3萬 |
| 釘選 | https://www.threads.com/@littleveera1201/post/DdgIR-7j5fQ | 2026-09-20 | 單圖，防詐公告加自串補充 | 750/39/13/30 | 10萬 |

- 角色設定：用遊戲角色延伸的插畫形象（lit.link 上有角色設定文，並註明「圖委來源」），不是擬真人像。簡介寫「嚴禁亂發邀請碼…請認清藍勾勾，小心詐騙」。
- 落地頁：lit.link 連結頁，連到 Discord、TikTok、IG、7-11 賣貨便週邊賣場和合作信箱（EV-T21）。
- 推論：這類遊戲受眾可能包含未成年人，但官方沒有公開受眾年齡資料。

#### A.2.8 @isaac.startup（EV-T08）
- 網址：https://www.threads.com/@isaac.startup ，觀察時間 07:09 UTC。抽樣窗口 7 篇。推論是香港帳號（Podcast 用廣東話，網站寫港幣），不是台灣帳號。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 釘選 | https://www.threads.com/@isaac.startup/post/Ddl9smiDCL0 | 2026-09-22 | 純文字，7 段自串（每段一個 prompt） | 主文 73/21/9/86；後續各段 1～5 讚 | 1.0萬 |
| 窗口內最高 | https://www.threads.com/@isaac.startup/post/Dd6ogVBDDrG | 2026-09-30 | 純文字清單「三個 AI 工具」，隔天自留言附工具連結 | 188/14/17/81 | 4.7萬 |
| 偏低 | https://www.threads.com/@isaac.startup/post/DeGx32xkYB6 | 2026-10-05 | 純文字觀點 | 2/0/0/0 | 1,963 |

- 連結與 CTA：簡介寫「在 2026 開始你的AI一人創業 👇」，連結 isaac.mba，另有 Podcast。落地頁是電子報加付費產品「SoloPath…一次付費永久擁有」（EV-T22）。清單或 prompt 類貼文的分享數常和讚數差不多或更高。

#### A.2.9 @tgsa999（EV-T09）
- 網址：https://www.threads.com/@tgsa999 ，觀察時間 07:11 UTC。只有 53 位粉絲，抽樣窗口 5 篇，簡介沒有連結。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 高峰 | https://www.threads.com/@tgsa999/post/DeErP0qDOr7 | 2026-10-04 | 影片（撞球世錦賽） | 1.2萬/204/139/360 | 22萬 |
| 高 | https://www.threads.com/@tgsa999/post/DeI3GPumhZZ | 2026-10-06 | 單圖（主題標籤：味全龍） | 907/119/1/261 | 8.3萬 |
| 一般 | https://www.threads.com/@tgsa999/post/Dd_pZmFGpUT | 2026-10-02 | 單圖（主題標籤：富邦悍將） | 37/0/0/1 | 958 |

- 觀察：粉絲極少，但單篇可以拿到數十萬次瀏覽，符合官方「Feed 由追蹤內容加推薦內容組成」的說明（EV-M21）。不過同一帳號的另一篇只有 958 次瀏覽，**沒辦法預測哪篇會被推薦**。

#### A.2.10 @jo_photos0777（EV-T10）
- 網址：https://www.threads.com/@jo_photos0777 ，觀察時間 07:16 UTC。抽樣窗口 6 篇。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 釘選、高峰 | https://www.threads.com/@jo_photos0777/post/DUztoMFks0J | 2026-02-16 | 多圖（7 張），作品集 | 2萬/241/365/505 | 35萬 |
| 一般 | https://www.threads.com/@jo_photos0777/post/DeG-5eFo70E | 2026-10-05 | 多圖（10 張），外拍景點，自己標「(非業配)」 | 70/9/1/1 | 1,371 |
| 互動型 | https://www.threads.com/@jo_photos0777/post/DeHgqEsI0Mn | 2026-10-05 | 純文字提問 | 72/52/0/4 | 3,810 |

- 連結與 CTA：簡介寫「互惠請看IG注意事項‼️」「脆不回覆訊息，麻煩私訊IG」。也就是 Threads 只負責曝光，溝通和成交都在 IG。景點地圖連結放在自留言（例如 /post/Dd_GL-hj5L1）。

#### A.2.11 @setnews（EV-T11）
- 網址：https://www.threads.com/@setnews ，觀察時間 07:12 UTC。19 萬粉絲、3.3 萬則串文；窗口 8 個容器都是 41 分鐘內發的。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 一般 | https://www.threads.com/@setnews/post/DeJJO2sDSiq | 2026-10-06 14:30 台北 | 單圖加標題加「披薩邊:」小編短評，再自留言放短網址 | 9/1/0/0 | 289 |
| 一般 | https://www.threads.com/@setnews/post/DeJK-XJDCs4 | 2026-10-06 14:45 台北 | 純文字加自留言短網址 | 4/1/0/0 | 399 |

- 連結：短網址 setnsocial.pse.is 會轉到 `setn.com/news/…?utm_source=threads&utm_medium=setnt`，是發文方自己做的追蹤（EV-T23）。簡介連結 portaly.cc/setnews。
- 限制：查核時貼文發出不到 1 小時，瀏覽數一定還會增加，不能拿來推論新聞帳號的平均表現。

#### A.2.12 @lilmiquela（EV-T12）
- 網址：https://www.threads.com/@lilmiquela ，觀察時間 07:11 UTC。簡介寫「22 ❤️‍🔥 LA 🌎 Robot 🦾」，自己揭露是機器人。抽樣窗口 4 篇。

| 類型 | 貼文 | 日期 | 格式 | 互動 | 瀏覽 |
|---|---|---|---|---|---|
| 窗口內最高 | https://www.threads.com/@lilmiquela/post/Dd__QxqjueP | 2026-10-02 | 多圖 | 13/0/0/0 | 515 |
| 一般 | https://www.threads.com/@lilmiquela/post/DdUAAunAq3P | 2026-09-15 | 圖加影片 | 5/3/2/0 | 443 |

- 觀察：35 萬粉絲，但單篇只有數百次瀏覽，**粉絲數不等於觸及**。留言者也接受她的機器人設定（例如「you are a robot going to concerts now」）。簡介連結是音樂串流導購頁（EV-T24）。
- AI 標示：未登入檢視時，沒有在可見貼文上看到「AI 資訊」標籤文字。App 內或登入後是否有標籤，未確認。

### A.3 跨樣本觀察：連結與 CTA 放在哪裡

| 做法 | 例子 | 備註 |
|---|---|---|
| 簡介連結（單一連結或連結頁） | @isaac.startup、@littleveera1201（lit.link）、@setnews（portaly）、@imma.gram（beacons） | 官方允許簡介放最多 5 個連結（EV-M26） |
| 簡介連結到不透明的轉址或下載頁 | @horo.taurustw → App 跳轉頁 | 參見 Spam 政策中關於轉址的條文（EV-M06） |
| 主文發出後，作者自留言放連結 | @horo.taurustw、@i.love.meowstars、@classic.meme.daily、@setnews、@__9ann__、@jo_photos0777 | 很常見，但**看不到這樣做對觸及或點擊的影響**（見 C） |
| 私訊關鍵字 | @1212laowu（私訊「升級」） | DM 後的流程看不到 |
| 把溝通導到 IG | @jo_photos0777、@guguhola1110、@classic.meme.daily | 只把 Threads 當曝光入口 |
| 釘選文放 CTA | @__9ann__、@littleveera1201（防詐公告） | 釘選文的數字通常是窗口內最高，有偏差 |

- 外連都會經過 `l.threads.com` 轉址。在未登入網頁版上，部分目標網址被加上 `utm_id=97760_v0_s00_e0_tv3_…` 或 `…_tv4` 參數（見 @lilmiquela、@setnews、@__9ann__）。**這是本次觀察到的現象，不是官方文件的說明**，App 內或登入狀態下是否相同未確認。
- 未登入搜尋「AI網紅」時，看到有使用者要求 AI 網紅自我揭露，例如「很多都不會標示自己是AI…分享一些偽裝真人的AI網紅讓我避雷」（EV-T14）。但這些貼文互動很低（個位數讚），只能當作一個訊號，不能代表整體使用者態度。

### A.4 選樣偏差與限制

1. **平台排序偏差**：候選帳號來自 Threads 搜尋結果，而搜尋結果是平台依互動排序過的，加上關鍵字是研究者挑的，所以樣本偏向本來就比較活躍的帳號。
2. **窗口太小**：未登入只能看到 4～11 個容器，沒辦法隨機抽樣，也看不到較早的貼文分布。
3. **離群值**：釘選文和高峰文（53萬、35萬、22萬、10萬次瀏覽）都是離群值，表格裡已經標註，不能拿來當平均。
4. **時間點偏差**：@setnews、@i.love.meowstars 的貼文剛發不久，數字被低估。
5. **風險類型代表性不足**：依規定排除了有性暗示或露骨內容、可能涉及未成年人的帳號，所以**樣本無法說明「大尺度 Cos、性感身材」內容在 Threads 上的實際表現或被處置的情形**。
6. **部分方向缺漏**：沒有抽到中職啦啦隊員本人或 NBA 帳號（T5 只有一個球迷帳號）；AI 科技樣本是香港帳號；兩個新聞媒體帳號的個人頁轉到登入頁。
7. **數字精確度**：頁首和 meta 描述的粉絲數不一致；官方說明互動指標仍「in development」（EV-M27）。
8. **公開互動數不能證明點擊、轉換或營收**，這次也看不到任何帳號的洞察報告。

### A.5 對本案的可借鏡處（研究推論，非定律）

1. **系列化格式**：@classic.meme.daily 的「倒數 Day」、@i.love.meowstars 的每小時一個星座、@1212laowu 每天固定時段，都讓讀者容易預期內容。這是常見做法，但這次的資料無法證明它造成流量。
2. **虛擬或品牌身分可以公開經營**：@lilmiquela 自稱「Robot」、@imma.gram 自稱「バーチャルヒューマン」、@littleveera1201 用插畫角色、@horo.* 以星座命名、@i.love.meowstars 是品牌角色。這些帳號都公開說明自己的身分。對本案來說，AI 人設可以參考「在簡介裡揭露」的做法，而不是宣稱「本人」（見 B.5、D）。
3. **Threads 端的內容本身要完整，成交放到站外**：例如老吳用私訊換免費課、酒安請人私訊 IG、Isaac 導向電子報。但如果站外是成人平台，這種結構會直接觸及官方的性招攬條文（見 B.2、D），不能照搬。
4. **建立信任與防冒名**：@littleveera1201 的防詐釘選文有 10 萬次瀏覽。如果本案經營多個帳號，可以考慮公開列出「官方帳號清單」，並說明經營關係。
5. **小帳號也可能被大量推薦，但不可預測**：@tgsa999 只有 53 粉絲，卻有 22 萬次瀏覽的貼文，同時也有 958 次瀏覽的貼文。
6. **高頻發文不保證單篇表現**：@setnews 每 8～15 分鐘發一篇，單篇只有數百次瀏覽（查核當下）。
7. **連結放在自留言很常見，但沒有成效證據**：如果要比較，只能用自家洞察報告的「連結造訪」數據做測試（EV-M26、EV-M30）。

---

## B Meta 官方規則查核（全部來源的查核日期：2026-10-06）

### B.1 帳號規則

| 項目 | 官方原文（節錄） | EV | 結論 |
|---|---|---|---|
| 最低年齡 | IG 條款：「You must be at least 13 years old.」；Threads 條款：「any provisions under the Instagram Terms regarding who is able to use Instagram will also apply to your ability to use the Threads Service.」 | EV-M10、EV-M09 | 13 歲（台灣在地另有規定與否：未確認） |
| 未成年預設 | 「If you're under 18, when you create a Threads profile, your profile will be set to Private by default. Teens 16-17 can update their profile privacy setting」 | EV-M13 | Threads 上有青少年用戶，並有 Teen Accounts 與家長監督（EV-M34） |
| 是否綁 IG | 條款：「You will sign up and login to the Threads Service using your Instagram account, Facebook account, or any other account that we may choose to enable in the future.」；說明頁：「you'll need to sign in with your Instagram or Facebook account. You can create one profile on Threads for each Instagram and Facebook account you have.」 | EV-M09、EV-M12 | 目前寫明可用 IG 或 FB 帳號建立 |
| 不用 IG 也能建立？ | 「If you've created a Threads profile with your mobile number or email, you can also edit your name from Threads.」 | EV-M14、EV-M15 | 用手機或 Email 建立的個人檔案確實存在；**台灣能不能用：未確認**（EV-M15 顯示「not available in your area」） |
| 多帳號 | 「You can create multiple profiles for Threads. When you add multiple Threads profiles, you can switch between them.」 | EV-M13 | 可以有多個帳號；**數量上限：未確認**。可以有多帳號，不代表可以用多帳號做不實的協同操作（見 B.2） |
| 適用的社群規範 | 條款：Threads 條款「supplement and amend the Instagram Terms of Use and the Meta Community Standards」；《社群守則》：「what is and isn't allowed on Facebook, Instagram, Messenger and Threads」；2023 年上線時：「we'll enforce Instagram's Community Guidelines」 | EV-M09、EV-M01、EV-M33 | IG Community Guidelines 的連結現在會轉到 Meta《社群守則》（EV-M11） |
| 身分 | 「you may not impersonate someone or something you aren't」「You can't do anything unlawful, misleading, or fraudulent」 | EV-M10 | 和 AI 人設宣稱「本人」直接相關 |
| 商業用途 | Threads 條款：不得「exploit the Threads Service for any commercial purpose」 | EV-M09 | 原文寫在「How You Can't Use」段落，但官方同時提供付費合作工具（EV-M22），這條的適用範圍**未確認** |

### B.2 社群守則（和本案最相關的條文）

**(1) 成人性招攬與露骨性語言**（EV-M02，變更紀錄最新為 2025-05-15）
- 不允許：「Content that asks for, offers or provides methods of contact to acquire pornographic material, or contains usernames or links to pornographic websites.」
- 不允許：以提供、索取或提供聯絡方式的方式招攬性接觸，包括「Sex chats or conversations」「Erotic dancing or stripping」「Sharing of nude imagery」。
- 只限 18 歲以上觀看：「Content that contains usernames, links to or logos of Adult Subscription Websites」「Sexually suggestive language that refers to sexual encounters」。
- 條文沒有定義「pornographic websites」（禁止）和「Adult Subscription Websites」（限 18+）的界線。LUSCENA 屬於哪一類**未確認**，但它的一對一直播和私聊功能，和「sex chats/conversations」條文高度相關（推論）。

**(2) 成人裸露與性行為**（EV-M03，2025-08-28）
- 「we remove … AI- or computer-generated images of nudity and sexual activity, and digital imagery, regardless of whether it looks "photorealistic"」
- 只限 18 歲以上觀看：「Photorealistic/digital imagery of persons where crotch, buttock or female breast(s) are the focus of the image」、只用數位覆蓋或透視衣物遮住的「near nudity」、「Logos, screenshots or video clips of known pornographic websites」。

**(3) 兒少性剝削**（EV-M04，2025-08-01）
- 保護範圍包含「non-real depictions with a human likeness, such as in art, AI-generated content, fictional characters, dolls」。
- 列為「Children with sexual elements」的情況包括「Sexualized costume」「Staged environment (for example, on a bed) or professionally shot」。
- **找不到「成人扮演學生或穿制服」的專門條文**（未確認）。推論：只要角色本身是未成年，或 AI 生成的外觀看起來年幼，再加上性感的 Cos 呈現，就落在高風險區。

**(4) 虛假行為與協同虛假行為（CIB）**（EV-M05，2025-12-11）
- 不允許：「The creation, use, or claimed use of Inauthentic Meta Assets (Accounts, Pages, Groups, etc.) in order to: Deceive Meta or our users about the identity, or origin of an audience or the entity that they represent」。
- CIB 的定義是「particularly sophisticated forms of Inauthentic Behavior where false identities are central to the operation」。

**(5) 垃圾訊息**（EV-M06，2024-06-27）
- 不允許「Posting, sharing, engaging with content or creating accounts … either manually or automatically, at very high frequencies.」；即使頻率較低，若出現「posting repetitive content」或「signals of inauthenticity」，也可能被限制。
- 不允許買賣互動，以及 cloaking、「Misleading Links」、「Deceptive redirect behavior」。
- 不禁止：「Cross promotion that is not triggered by payment to a third party」。

**(6) 帳號完整性**（EV-M07，2026-05-28）
- 可限制或停用以下帳號：「Close linkage with a network of accounts or other entities that violate or evade our policies」、「Coordination within a network of accounts or other entities that persistently or egregiously violate our policies」。
- 「Creating or using an account … through automated means, such as scripting (unless … authorized routes…)」：Meta 可能要求補充資訊。

**(7) 真實身分**（EV-M08，2026-09-11）
- 會限制或停用 Facebook、Instagram、Threads 上「Engage in identity misrepresentation to mislead or deceive others」的帳號，判斷因素包括「Misleading profile information, such as bio details」「Using stock imagery」。
- 「代表虛構角色的帳號」只在 Facebook 規定中寫明，Threads 是否有對應規定**未確認**。

### B.3 品牌內容與付費合作

- Threads 付費合作工具（EV-M22）：「our branded content policies require that you use the paid partnership tool to indicate when a commercial relationship has influenced the post.」「Partnership Ads and Boosting of organic branded posts are not currently supported in Threads.」
- **官方說明頁互相矛盾**：另一頁寫「Unlike Instagram, Threads currently doesn't offer the branded content tool…add text or hashtags」（EV-M23）。實際以 App 選單為準，本次沒有實測。
- 品牌內容政策（EV-M24）禁止推廣「Adult products or services, except for family planning and contraception.」；品牌內容的定義是「a creator or publisher's content that features or is influenced by a business partner for an exchange of value」。
- 推論：如果主帳號是由代理商受 LUSCENA 委託發「官方或廣告」貼文，就屬於品牌內容，推廣成人服務被禁止；如果是 LUSCENA 自營帳號，B.2(1) 的條文仍然適用。

### B.4 推薦與敏感內容

- Threads Feed（EV-M21）：「This feed is composed of content from people you follow and recommended content.」候選內容必須「follow our quality and integrity rules」。
- IG 推薦規範（EV-M20；**能否完整套用到 Threads 未確認**，但 2023 年官方說 Threads 的熱門話題會依「Community Guidelines or Recommendation Guidelines」審查，見 EV-M33）：
  - 不推薦「Content that may be sexually explicit or suggestive, such as pictures of people in see-through clothing」，例子包括「A photo zoomed in on someone's buttocks」。
  - 列為低品質內容：「Long captions unrelated to the underlying content and coordinated comment networks intended to artificially drive engagement and distribution.」
  - 不推薦的帳號：「Repeatedly and/or recently shared content we try not to recommend in the account name, username, profile photo, bio or profile」；「Repeatedly engaged in misleading practices to build followings」；「Repeatedly and recently shared content that prominently features a photorealistic AI-generated person, unless the account has disclosed this by adding the AI-generated profile label.」；「Teens will not be recommended accounts that we've found regularly share age-inappropriate content」。
- 敏感內容控制：「If they choose to see less sensitive content on Instagram, that setting will also be applied on Threads.」（EV-M33，2023-12-12 更新）。Threads 是否有獨立的設定頁**未確認**。

### B.5 AI 內容標示與虛擬人物

- 標示義務（EV-M16）：「Meta requires you to label content you share that has photorealistic video or realistic-sounding audio that has been digitally generated or altered, including with AI.」「Meta does not require you to label images that have been created or modified with AI. Images will still receive a label if Meta's systems detect they were AI-generated.」「There may be penalties if you do not label content as required.」
- Threads 有標示功能：「Tap [選單] and choose Add AI label.」（只有 iPhone 和 Android App，電腦版沒有）。
- 新聞稿（EV-M17）：「we may apply penalties if they fail to do so」；如果內容「particularly high risk of materially deceiving the public」，可能加上更顯眼的標籤。EV-M18：只用 AI 修改過的內容，「AI info」標籤會移到選單中。EV-M19：Threads 上有 AI info 標籤的實際使用數據（2024 年 10 月，超過 73 萬件內容的標籤被看到）。
- 虛擬人物或 AI 網紅：本次**沒有找到 Threads 專門的條文**。相關條文有 IG 條款的冒充規定（EV-M10）、身分不實（EV-M08）、IG 推薦規範中的「AI-generated profile label」（EV-M20）。Threads 有沒有這種個人檔案標籤**未確認**，罰則的具體內容也**未確認**。

### B.6 連結與洞察報告

| 項目 | 官方原文（節錄） | EV | 結論 |
|---|---|---|---|
| 簡介連結數 | 「Now, you can add up to five links to your bio」（2025-05-15 更新） | EV-M26 | 最多 5 個 |
| 貼文連結數 | API：「The number of links is restricted to 5 or fewer.」 | EV-M29 | API 最多 5 個；**App 內上限未確認** |
| 連結預覽卡 | API：沒有指定 link_attachment 時，第一個連結會變成預覽卡，「to make it easier to engage with and click on」 | EV-M29 | 這只說明介面行為，沒有說明觸及差異 |
| 連結成效 | 「You can also see how many people have visited the links you've shared – whether in your bio or in posts.」 | EV-M26 | 有連結造訪數據 |
| API 點擊指標 | 使用者層級的 clicks：「The number of times people clicked on URLs you shared.」 | EV-M30 | 帳號層級有點擊數；**單篇貼文的連結點擊：未確認**（貼文層級指標只列 views、likes、replies、reposts、quotes、shares） |
| 洞察報告內容 | 「views, replies, reposts and quotes…follower count…demographics」；2025-07-22 新增互動細項、7～90 天趨勢、內容在哪裡被看到（包括其他 App） | EV-M25、EV-M26 | — |
| 指標精確度 | 「Certain metrics, such as likes, replies, reposts, quotes and views are still in development.」；API 的 views 和 shares 標註 in development | EV-M27、EV-M30 | 數字要保守解讀 |
| Referrer 或 UTM | 本次查核的官方頁面都沒有說明 | — | **未確認**（A.3 有觀察到 utm_id 參數，但那只是觀察） |

### B.7 發布與自動化（Threads API）

- 原生排程（EV-M25，2024-08）：「schedule them to publish at a later date and time. You can schedule multiple posts a day, multiple days in advance.」這篇講的是網頁版功能，草稿最多存 100 則。**App 內排程：未確認**。
- API 用途（EV-M28）：「You may use the Threads API to enable people to create and publish content on a person's behalf on Threads…」
- API 上限（EV-M28）：「Threads profiles are limited to 250 API-published posts within a 24-hour moving period. Carousels count as a single post.」；回覆「limited to 1,000 replies within a 24-hour moving period」；刪除每 24 小時 100 次；文字上限 500 字；呼叫額度是「4800 * Number of Impressions」。
- 留言管理（EV-M31）：可以隱藏留言，`reply_control` 有 everyone、accounts_you_follow、mentioned_only、parent_post_author_only、followers_only 五種，另有留言審核。
- 個人檔案 API（EV-M32）：只能讀取授權使用者自己的資料；`profile_lookup` 用標準權限只能查 Meta 官方帳號，而且只回傳 100 粉絲以上的公開帳號。所以**不能用官方 API 監測其他帳號**。
- 洞察 API（EV-M30）：`follower_demographics` 需要至少 100 位粉絲。
- 使用 API 的帳號類型要求（例如是否須為專業帳號）：在讀到的頁面中只看到 `threads_basic` 權限要求，**未確認**。
- 自動化規則：IG 條款禁止未經許可以自動化方式建立帳號或蒐集資訊（EV-M10）；Spam 政策禁止手動或自動的極高頻互動（EV-M06）；帳號完整性政策提到用腳本建立帳號（EV-M07）。**API 的上限只是技術額度，不代表發到這個量就合規。**

---

## C 不得寫成定律的說法

以下說法在本次查核的官方來源中**都找不到依據**，不能寫成定律或保證：

1. **「最佳發文時間」**：官方只說 Feed 由 AI 依觀看者的互動訊號預測和排序（EV-M21），沒有指定發文時間。樣本中老吳的 18:05、星座帳號的 10:00 只是這些帳號的習慣，無法證明有效。比較可靠的做法是用自家洞察報告（EV-M25、EV-M26）做測試。
2. **「連結放留言一定比較好」**：官方沒有這樣說。官方只說 API 會把第一個連結做成預覽卡，「to make it easier to engage with and click on」（EV-M29），這是介面說明，不是觸及規則。很多樣本把連結放在自留言（A.3），但點擊和觸及的差異看不到，只能用自家連結造訪數據驗證（EV-M26、EV-M30）。
3. **「每天發幾篇就會有流量」**：官方沒有這樣說。反過來，Spam 政策把「very high frequencies」和「posting repetitive content」列為風險訊號（EV-M06）。樣本中，高頻發文的 @setnews 單篇只有數百次瀏覽（查核當下），低頻的 @tgsa999 卻有 22 萬次瀏覽的貼文。這只是個案，不能推論任何規律。
4. 其他也不能寫成定律的說法：「粉絲多就有觸及」（反例：@lilmiquela 35 萬粉絲，單篇數百次瀏覽）；「hashtag 越多越好」（API 規定每篇只能有 1 個主題標籤，見 EV-M29）；「Threads 不會限制外連」（未確認）；「互動高就代表導流成功」（公開互動數不能證明點擊、轉換或營收）。

---

## D 政策風險初判（研究推論）

> 風險等級是研究者根據官方條文所做的初步判斷，不是 Meta 的判定，也不是法律意見。台灣法規（例如兒少保護與猥褻相關法規）不在本研究範圍內，須另請法務確認。

| # | 客戶的做法 | 相關官方條文 | 風險 | 理由 | 合規替代方案 |
|---|---|---|---|---|---|
| 1 | 主帳號放 LUSCENA 連結，或發「官方／廣告」貼文 | EV-M02「links to pornographic websites」（禁止），以及 Adult Subscription Websites（限 18+）；EV-M24 品牌內容禁止推廣成人服務；EV-M20 簡介或個人檔案反覆出現不推薦內容的帳號不會被推薦 | **高** | LUSCENA 是 18+ 的露骨直播平台，不論被歸為哪一類，都會被移除或限制；如果是受委託發文，還違反品牌內容政策 | 不在 Threads 放成人站連結或導購。如果品牌一定要在 Threads 出現，只做可公開、非性內容的企業資訊，並先經法務確認。成人站的導流改走允許成人內容、有年齡驗證的管道（不在 Meta 範圍，本研究沒有評估） |
| 2 | 用「私訊我」「看完整版」等暗示，搭配站外連結或聯絡方式 | EV-M02 招攬性聊天、裸照並提供聯絡方式；EV-M06 like-gating、誤導連結 | **高** | 「暗示加聯絡方式或連結」正是條文描述的行為 | 不做任何性方面的暗示招攬；私訊只處理一般問題 |
| 3 | 用短網址或中繼頁把成人站藏起來 | EV-M06 cloaking、「Deceptive redirect behavior」「Misleading Links」 | **高** | 規避審查本身就違反 Spam 政策 | 有連結就顯示真實網域，不做轉址遮蔽 |
| 4 | B 大尺度 Cos、C 性感身材（明確為成人角色、沒有裸露） | EV-M03 胯部、臀部、胸部為焦點的圖像或 near nudity 限 18+；EV-M20 性暗示內容不推薦；EV-M03 AI 生成的裸露一律移除 | **中** | 可能被限 18+ 或不被推薦，觸及會受限；如果是 AI 生成又涉及裸露，會變成高風險 | 改做造型、道具、角色設定、健身訓練等非性暗示內容；接受觸及可能受限；完全不用 AI 生成裸露內容 |
| 5 | Cos 角色是未成年、外觀年幼、穿學生制服，或 AI 生成的年輕外觀 | EV-M04 涵蓋「non-real…AI-generated…fictional characters」，並列「Sexualized costume」 | **高**（成人扮演制服的專門條文：未確認） | 兒少相關政策會停用帳號並通報，後果最嚴重 | 只扮演明確為成年的角色；不用校服或幼態造型；AI 人物避免年輕化外觀 |
| 6 | 7 個不同主題的流量帳號，由同一團隊操作，沒有揭露關係，去留言和轉發主帳號 | EV-M05（Inauthentic Assets 欺騙受眾來源）；EV-M07（網絡關聯與協同）；EV-M06（重複或高頻互動）；EV-M20（「coordinated comment networks」不推薦）；EV-M08（簡介不實） | **高** | 這就是條文描述的「同一團隊控制多帳號、製造互動假象」 | 每個帳號都真實經營，並在簡介揭露同屬一個團隊（例如「XX 工作室旗下」）；不做協同灌留言；交叉推廣維持低頻、不付費、公開關係（EV-M06 不禁止這種推廣） |
| 7 | 用 API 或腳本自動留言、按讚、建立帳號 | EV-M10 自動化建帳號或蒐集資料；EV-M06 高頻互動；EV-M07 腳本；EV-M28 API 上限 | **高**（自動互動、建帳號）／**中**（只用官方 API 發自家文） | API 額度不等於合規 | 只用官方 API 處理自家帳號的發文和留言管理，不做自動互動 |
| 8 | AI 人設宣稱「本人」或真人 | EV-M10「impersonate someone or something you aren't」；EV-M08 身分不實；EV-M16 擬真影片和音訊必須標示，否則可能受罰；EV-M20 擬真 AI 人物帳號沒有揭露就不推薦 | **高** | 宣稱真人會同時觸及冒充、身分不實和標示規定 | 在簡介寫明「AI 虛擬角色，由 XX 團隊創作」；影片和音訊加 AI 標籤；可考慮插畫風格（參考 EV-T07）或自稱機器人（參考 EV-T12） |
| 9 | AI 人設已經揭露（簡介說明加 AI 標籤），內容為全年齡 | EV-M16、EV-M20 | **低～中** | 揭露後主要風險變成內容本身（第 4、5 項） | 同第 8 項，並固定檢查標籤 |
| 10 | 迷因、電玩、星座帳號的受眾可能有未成年人，被導向主帳號或成人站 | EV-M13、EV-M34（Threads 有青少年用戶和保護機制）；EV-M04 與未成年人不當互動；EV-M02 成人內容限 18+；EV-M20 不向青少年推薦不適齡帳號 | **高** | T2、T3、T1 的受眾很可能包含青少年（推論，EV-T07），把他們導向成人平台的後果最嚴重 | 流量帳號完全不導向成人內容；留言和私訊不提成人平台；內容維持全年齡 |
| 11 | 流量帳號本身（非成人主題）真實經營、沒有導向成人內容 | EV-M01 一般社群守則 | **低** | 和一般創作者帳號一樣 | 依各主題的一般規範經營，並揭露 AI 身分 |

**總結（推論）**：「AI 人設加上不同主題流量帳號協同推主帳號，再導向成人站」這個完整結構，在官方條文中至少同時碰到成人招攬（EV-M02）、虛假行為（EV-M05）、帳號網絡關聯（EV-M07）、身分不實（EV-M08）、品牌內容（EV-M24）和不推薦規範（EV-M20）。這個結構無法靠調整發文技巧變成合規。合規的路線只剩：Threads 帳號各自是真實、公開揭露的內容帳號，並且不在 Meta 平台上導流到成人站。

---

## E 未確認事項

1. 台灣用戶能不能不經 IG 或 FB，直接用手機或 Email 建立 Threads 帳號（EV-M14 和 EV-M15 的說法不一致）。
2. 同一人或同一 Meta 帳號可以加入幾個 Threads 個人檔案（官方只說「multiple」）。
3. 在 Meta 的分類裡，LUSCENA 算「pornographic website」還是「Adult Subscription Website」（EV-M02 沒有定義）。
4. 有沒有「成人扮演學生或制服」的專門條文（EV-M04 沒有找到）。
5. IG 推薦規範（包括「AI-generated profile label」）是否完整適用 Threads；Threads 有沒有 AI 生成個人檔案標籤。
6. 違反 AI 標示規定的具體罰則。
7. Threads App 內單篇貼文的連結數上限（API 是 5 個）；外連會不會影響推薦分發。
8. 洞察報告能不能看到「單篇」的連結點擊，以及是否分開統計簡介連結和貼文連結。
9. Threads 網頁外連的 referrer 和 UTM 處理（觀察到 `utm_id=97760_…`，官方沒有說明）。
10. Threads 到底有沒有付費合作工具（EV-M22 和 EV-M23 互相矛盾）。
11. 使用 Threads API 的帳號類型要求（例如是否須為專業帳號）。
12. App 內有沒有排程功能（官方新聞稿只提網頁版）。
13. Threads 條款中「exploit the Threads Service for any commercial purpose」的適用範圍。
14. 敏感內容控制在 Threads 上有沒有獨立的設定頁。
15. @horo.* 系列帳號是否同一經營者、@1212laowu 私訊後的實際流程（推論和不可見部分）。
16. 樣本帳號的真實點擊、轉換和營收（公開資料無法得知）。
17. 台灣法規面的評估（不在本研究範圍，須由法務處理）。
