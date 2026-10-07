# 覆核請求：TASK-002 十角色 AIGC 建模交付包 R1

- 請求日期：2026-10-07
- 請求人：執行者（Claude）
- 審閱人：Penny（owner）、ChatGPT（規劃主管）
- Repo：https://github.com/pennyhuang-oss/luscena-KOL（private）
- 分支：`claude/luscena-kol-initial-draft-et17t8`
- 開工時的基準：來源分支 `8d16cc1644fc2ddf0ca92b0837e21e9415ae07d0`（主管的合併覆核）；遠端 main `2283244aa0c01343361d0100b185732809b617af`（本輪沒有更新 main）
- R1 內容 commit：`3cb0a0c175a3fccf5196ce6482476134fa3745e5`
- 中間的工作存檔 commit：`36f06e2`、`9636657`、`f067a8f`、`7ef4011`、`002703c`
- 本檔與交接 prompt 的 SHA 在內容 commit 之後的下一個 commit 加入；最終 HEAD 見 owner 轉貼的覆核 prompt。
- 看全部改動：`git diff 8d16cc1 3cb0a0c`（32 個檔案）

---

## 1. 本輪範圍（Penny 指示）

- 建立 `production/modeling_pack_v1/`：讓製作師打開就能理解十個角色、需要的參考、可用的工具流程，並能直接把交接 prompt 貼給自己的 Claude。
- 落實 2026-10-07 客戶回饋：
  - 十個帳號是同一團隊這件事先不公開；角色互動與客串照常。
  - AI 揭露方式交由團隊評估，**尚未決定**；被問到時不否認；影片照平台規定。
  - 「其他應該沒問題」記錄為接受整體方向，不推論未回答的選項已選定。
- 更新 README 的目前階段與入口。
- 本輪允許：研究工具、整理建模文件、建議模型與流程、編寫 prompt、提交 GitHub。
- 本輪沒做：生圖、付費、人物訓練、開帳號、發布、聯絡製作師、重開導流；沒有更新 main、沒有 force push、沒有修改任何主管覆核文件。
- 全部仍是 PROPOSED。Penny 不代替客戶選角；未回答不等於同意；主管覆核也不代替選角。

## 2. 必讀

1. `production/modeling_pack_v1/00_START_HERE.md`
2. `production/modeling_pack_v1/CLIENT_FEEDBACK_2026-10-07.md`
3. `production/modeling_pack_v1/L01.md`～`L10.md`（重點：L02、L03、L05、L08）
4. `production/modeling_pack_v1/MODEL_AND_WORKFLOW_OPTIONS.md`
5. `production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md`
6. `production/modeling_pack_v1/PRODUCER_CLAUDE_HANDOFF_PROMPT.md`
7. `review/INTERNAL_QA_TASK_002_MODELING_PACK_R1.md`（核查方法、結果、自查修正、子任務回報的人設來源問題）
8. `review/CHANGELOG_TASK_002_CLIENT_FEEDBACK.md`（人設包與 README 的 35 條修改：原句、新句、驗證）

**補充**：`persona_pack_v1/SHARED_EVENTS.md`（SE-10、SE-12 的不採用標記）、`persona_pack_v1/00_OVERVIEW.md`（全體共通設定新增兩列、角色宇宙）、`persona_pack_v1/PENNY_CHOICES.md`（開頭與 G-6）、`README.md`、`review/qa/check_t2.py`。

## 3. 本輪重點

| 項目 | 做了什麼 |
|---|---|
| 建模頁 L01–L10 | 每份有 A 角色摘要、B 外型規格、C 必須維持／可變／待選、D 撞臉配對與具體差異、E 中性建角照、F 招牌形象照、G 英文 prompt（BASE_IDENTITY、NEUTRAL_CASTING、IDENTITY_CHECK、SIGNATURE_PORTRAIT）附中文解釋、H 使用方式與參考圖分工與限制、I 製作師可替換的方法與要回報的取捨 |
| L02 | 凜本人先建身分（不戴假髮、不戴彩片、不上舞台妝），每套角色服都附同一張身分參考；假髮＋舞台妝另做檢查。主流程是尺度 1、原創，標待選；尺度 2 與同人另列分支，沒有 prompt |
| L03 | 尺度 1 起點標待選；必做全身中性照與體態一致性檢查；尺度 2 另列分支 |
| L05 | 寫實與 Q 版分開交付；Q 版要等寫實身分選定後再做，並列出辨識連續性清單 |
| L08 | 先列 A／B／C／D 狀態：B 是執行者建議優先討論、待選；A、B 共用沛沛的身分；C 是另一個人；D 可沿用沛沛的臉、待選後再寫 |
| 工具研究 | 把「生成候選人物」「參考圖維持身分」「專屬角色訓練」分開；每條能力標「已查證（官方網頁）／已觀察（本 session 的 MCP）／推論／需製作師確認」；三條流程；沒有價格 |
| 驗收 | 參考素材登記與權利；身分測試和形象照分開；審查項目標明哪些只看文字能判斷、哪些必須看圖；不用未校準的數值門檻；生成完成不等於形象核准 |
| 客戶回饋 | 人設包中公開同一團隊的段落標「依客戶回饋不採用」或改字並保留原寫法；十份角色檔開頭加註 AI 揭露待團隊決定；角色互動保留 |

## 4. 請覆核（每題給 PASS／REVISE／BLOCK＋理由＋要改的地方）

| # | 問題 | 請看 |
|---|---|---|
| Q1 | 十份建模頁的名字、年齡、外型是否和人設一致？有沒有改寫成新角色，或把背景故事塞進生圖 prompt？ | 各建模頁 A、B、G-1；`persona_pack_v1/Lxx.md` §1、§4；QA §3 第 1–3 項 |
| Q2 | 英文 prompt 和中文規格是否一致？左右、成年外觀、原創是否寫對？參考圖的用途與「文字不能保證一致」是否說清楚？ | 各建模頁 G、H；QA §4 QA-T2-01 |
| Q3 | 十人是否不只靠髮色、服裝區分？撞臉配對是否和總覽一致？ | 各建模頁 D；`persona_pack_v1/00_OVERVIEW.md` |
| Q4 | 未選定的選項是否保留為待選？L02／L03 尺度與 IP、L05 Q 版、L08 A／B／C／D 的處理是否恰當？ | 各建模頁 C；L02、L03、L05、L08 |
| Q5 | 工具研究是否分清楚已查證、推論、需製作師確認？有沒有憑記憶編造模型、參數或價格？三條流程是否可行？ | `MODEL_AND_WORKFLOW_OPTIONS.md` |
| Q6 | 驗收與參考規則是否可用？是否清楚分開「可以先做」和「要先取得決定或授權」？ | `REFERENCE_AND_ACCEPTANCE.md` |
| Q7 | 交接 prompt 是否讓製作師的 Claude 能直接開始，又不會被當成無上限付費授權？寫回 repo 的方式是否清楚？ | `PRODUCER_CLAUDE_HANDOFF_PROMPT.md` |
| Q8 | 客戶回饋是否忠實落實？有沒有新增假背書、否認身分、掩飾共同管理的方案？AI 揭露有沒有被寫成「一律不用標示」？有沒有把「其他應該沒問題」寫成全部選項已選定？ | `CLIENT_FEEDBACK_2026-10-07.md`；`review/CHANGELOG_TASK_002_CLIENT_FEEDBACK.md`；README |
| Q9 | 核查紀錄是否如實？有沒有把腳本跑完當成語意通過？ | `review/INTERNAL_QA_TASK_002_MODELING_PACK_R1.md` |
| Q10 | 範圍：是否只做文件，沒有生成、付費、訓練、發布；沒有更新 main、沒有改主管覆核文件？ | QA §3 第 7、9 項、§6 |

## 5. 已知未解問題（詳見內部核查 §5、§7）

- 沒有任何參考圖、候選圖或撞臉實測。
- 製作師帳號的實際工具、Soul ID 訓練張數（官方來源互相衝突：20–80 或 5–20）、角色數上限、扣點都要製作師確認；沒有價格。
- AI 揭露方式、被問到帳號之間關係時的回答口徑，都還沒有決定。
- 子任務回報的人設來源問題沒有在本輪修改（例如 L08 缺臉長寬比與髮色、L03 平口斜裁屬哪個尺度、各角色 §3／§10 的「發布時標示 AI」原句、撞臉配對稱呼不一致）。

## 6. 回寫方式

1. 請把覆核結果寫成 `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md`，內容包括：覆核依據的 commit SHA、Q1–Q10 的判定與理由、要改的地方（檔案與章節）、整體結論。
2. commit 到來源分支 `claude/luscena-kol-initial-draft-et17t8`，不要直接 commit 到 main；不 force push、不改寫既有 commit。
3. 無法 commit 時，輸出完整 Markdown，由 Penny 貼回 repo。

主管覆核不代替 Penny 或客戶選角；不授權生圖、付費、訓練、開帳號、發布、聯絡製作師或重開導流。提交後執行者停在這個階段。
