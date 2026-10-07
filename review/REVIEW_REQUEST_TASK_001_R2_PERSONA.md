# 人設覆核請求：TASK-001 R2（人設優先）

- 請求日期：2026-10-06
- 請求人：執行者（Claude）
- 審閱人：Penny（owner，選定角色）、ChatGPT（規劃主管，覆核人設品質）
- Repo：https://github.com/pennyhuang-oss/luscena-KOL（private）
- 分支：`claude/luscena-kol-initial-draft-et17t8`
- 內容 commit：`ed974038685b37be4ca31b1f4c3f37d1e2a8b958`（人設審閱包、範圍調整紀錄、內部核查）
- 本檔在內容 commit 之後的下一個 commit 加入。最終 HEAD SHA 見 owner 轉貼的覆核 prompt。

---

## 1. 本輪的範圍（Penny 2026-10-06 指示）

- **唯一的核心目標**：先把 10 個人設規劃清楚，讓 Penny 看得懂、能比較、能選定，再交給 AIGC 製作師評估人物形象。
- **延後另案**：導流與網站轉換，等角色建立、帳號創建、實際每日經營之後才討論。延後的問題**不是**人設規劃的阻擋條件。
- 範圍調整紀錄：`review/SCOPE_CHANGE_TASK_001_2026-10-06.md`。
- R1 的主管覆核文件完整保留，沒有改寫。R1「中期導流 BLOCK」的判定不變，本輪不討論。
- 本輪沒做：
  - 導流、落地頁、網站事件、轉換 KPI、完整營運成本；
  - 生圖、付費、訓練人物、開帳號、發布；
  - 修改客戶網站或參考 repo。
- 全部設定都是 **PROPOSED**，未經 Penny 或客戶核准。

## 2. 必讀

1. `persona_pack_v1/00_OVERVIEW.md`：十角色總覽、外型差異地圖、性感程度光譜、角色宇宙
2. `persona_pack_v1/L02.md`：重做，恢復「性感、大尺度 Cos、幻想感」
3. `persona_pack_v1/L08.md`：重做，列出運動賽事／啦啦隊的 A／B／C／D 四個定位
4. `persona_pack_v1/PENNY_CHOICES.md`：Penny 要決定的事
5. `persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md`：給製作師的 OK／NG 參考需求
6. `review/INTERNAL_QA_TASK_001_R2_PERSONA.md`：核查方法、結果、未解問題

**補充**：
- `persona_pack_v1/L01.md`、`L03.md`～`L07.md`、`L09.md`、`L10.md`
- `review/SCOPE_CHANGE_TASK_001_2026-10-06.md`
- 客戶原文：`brief/CLIENT_IMAGE_TRANSCRIPT.md`

## 3. 本輪重點

1. **L02**：定位改回「每週一位性感幻想角色登場」，例如兔女郎領班、潮汐祭司（泳裝）、第七機動隊長（貼身戰鬥服）、霧港老闆娘（高衩旗袍）。新增「夜城」角色宇宙連載。做道具降為出戲日常。尺度（1／2）與 IP（原創／同人）交給 Penny 選。
2. **L08**：v0 把啦啦隊縮成應援文化。改成四個選項：
   - A 女球迷；
   - B 啦啦隊舞者兼死忠球迷（執行者建議）；
   - C 男球迷「啦啦隊迷」；
   - D 場邊主持。
   A、B 有完整提案，C、D 是精簡草案。
3. **L03**：恢復性感身材與穿搭的核心，用具體的剪裁、姿態、光線描述；尺度交給 Penny 選。
4. **全部角色**：
   - 刪除否認商業關係的回覆；
   - 事實型內容用【】佔位，例如抽卡、實測、比賽數據、新聞來源、抽牌；
   - 故事改用相對週次；
   - 刪除營運比例與過時待辦。
5. **製作師參考需求**：臉部、妝髮、服裝、光線、構圖、場景的 OK／NG 欄位全部標為待選，另設來源與權利欄；身分測試、形象照、公開素材分開；列出高風險撞臉配對與請製作師回覆的問題。

## 4. 請覆核（每題給 PASS／REVISE／BLOCK＋理由＋要改的地方）

| # | 問題 | 請看 |
|---|---|---|
| P1 | 10 個人設是否符合客戶的 3＋7 結構與原文？核心有沒有被稀釋，特別是 L02 的大尺度 Cos、L03 的性感身材、L08 的啦啦隊？ | 各檔「一眼看懂」、§10；`brief/CLIENT_IMAGE_TRANSCRIPT.md` |
| P2 | 10 個角色在題材、語氣、外型上是否有實質區隔？最容易混淆的配對有沒有處理？ | 總覽的差異地圖；各檔 §8；`PRODUCER_REFERENCE_NEEDS.md` §4 |
| P3 | 角色設定和事實型內容是否分清楚？還有沒有假親歷、假實測、否認商業關係的句子？ | 各檔 §3、§10、§11 |
| P4 | Penny 選擇清單是否抓到真正需要決定的事？建議是否合理？L08 建議 B 是否成立？ | `PENNY_CHOICES.md`；`L08.md` §0 |
| P5 | 製作師參考需求是否足以讓製作師做可行性與估價評估？還缺什麼？ | `PRODUCER_REFERENCE_NEEDS.md` |
| P6 | v0 的矛盾、週次、比例、過時待辦是否已修正？有沒有新的不一致？ | `review/INTERNAL_QA_TASK_001_R2_PERSONA.md` |
| P7 | 範圍調整紀錄是否忠實反映 Penny 的指示，而且沒有改寫 R1 的覆核？ | `review/SCOPE_CHANGE_TASK_001_2026-10-06.md` |

## 5. 已知未解問題（詳見內部核查 §6）

- 跨帳號的故事週次，要等上線時程確定後再對。
- v0 規格（矩陣 §2、VISUAL_BRIEF §5.2）只加了「已被取代」的標示，沒有逐條改寫。
- L08 的 C、D 只有精簡草案。
- 名字與 handle 都還沒查核。
- 外型只有文字設計，沒有參考圖，也沒有撞臉實測。

## 6. 回寫方式

1. 請把覆核結果寫成 `review/REVIEW_RESPONSE_TASK_001_R2_PERSONA.md`，內容包括：
   - 覆核依據的 commit SHA；
   - P1–P7 的判定與理由；
   - 要改的地方（標出檔案與章節）；
   - 對 L02、L08 定位的意見。
2. commit 回同一個分支，不要 force push，也不要改寫既有 commit。
3. 如果無法直接 commit，請輸出完整的 Markdown，由 owner 貼回 repo。

Penny 的選擇（`PENNY_CHOICES.md`）由 Penny 自己填，或請 Penny 另外提供。主管覆核不代替 Penny 選角。

提交後執行者停在這個階段，不進入製作或發布。
