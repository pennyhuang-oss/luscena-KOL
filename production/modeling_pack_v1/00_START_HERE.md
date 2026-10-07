# 十角色 AIGC 建模交付包：從這裡開始

> **給製作師**：這個資料夾是 Luscena KOL 十個虛擬角色的建模交付包。它把已完成的文字人設整理成可以直接建模的規格與 prompt。
> **狀態**：PROPOSED。客戶在 2026-10-07 接受了整體十角色方向，但還有幾個選項沒選定（見第 3 節）。**文字人設被接受，不等於生成出來的人物形象已驗收。**
> 本包本身只是文件：撰寫時沒有生成圖片、訓練人物、付費、建立帳號或發布。製作師接手後的製作由製作師執行。
>
> **責任分工（2026-10-07 Penny 指示；優先於先前文件與主管覆核中的授權、選臉及驗收安排）**
> - Penny 只負責初步人設建立與交付。
> - 製作師接手後，自行決定工具、模型、生成、訓練、參考圖、製作方法與迭代流程。
> - 建模成果由製作師判斷是否可用，或依製作師的工作流程交客戶選定、驗收與定案。不需要 Penny 批准生成、訓練、選臉、鎖定身分或核准形象。
> - 費用、額度與製作範圍由製作師依帳號權限與客戶約定處理；Penny 不是付款或製作批准人。
> - 本包的人設規格、prompt、測試張數與模型流程都是建議，不強制照做。
> - 紀錄：`review/RESPONSIBILITY_CHANGE_TASK_002_2026-10-07.md`。

---

## 1. 任務目標

1. 為十個角色各建立一張**原創、成年、可重複使用的臉與體態**。
2. 十個人要彼此分得開，而且不只靠髮型、髮色或衣服分開。
3. 同一個角色換角度、換表情、換造型時，仍然是同一個人。L02 凜換不同的幻想角色服時，仍是同一張臉。
4. 由製作師產生候選、選定並鎖定形象；或依製作師的工作流程，交客戶選定、驗收與定案。

## 2. 十個角色與文件

| ID | 客戶格 | 角色 | 年齡／性別 | 建模頁 | 人設來源 |
|---|---|---|---|---|---|
| L01 | A 兩性話題（主） | 簡予安 | 29／女 | [L01.md](L01.md) | [persona_pack_v1/L01.md](../../persona_pack_v1/L01.md) |
| L02 | B 大尺度 Cos（主） | 凜 | 25／女 | [L02.md](L02.md) | [persona_pack_v1/L02.md](../../persona_pack_v1/L02.md) |
| L03 | C 性感身材時尚（主） | 周以晨 | 27／女 | [L03.md](L03.md) | [persona_pack_v1/L03.md](../../persona_pack_v1/L03.md) |
| L04 | T1 星座命理 | 林可妮 | 31／女 | [L04.md](L04.md) | [persona_pack_v1/L04.md](../../persona_pack_v1/L04.md) |
| L05 | T2 迷因梗圖 | 陳柏凱「阿凱」 | 24／男 | [L05.md](L05.md) | [persona_pack_v1/L05.md](../../persona_pack_v1/L05.md) |
| L06 | T3 電玩手遊 | 黃子翔「翔哥」 | 34／男 | [L06.md](L06.md) | [persona_pack_v1/L06.md](../../persona_pack_v1/L06.md) |
| L07 | T4 AI 科技 | 程翊 | 28／男 | [L07.md](L07.md) | [persona_pack_v1/L07.md](../../persona_pack_v1/L07.md) |
| L08 | T5 運動賽事／啦啦隊 | 蔡沛岑「沛沛」（A／B）；C、D 待選 | 26／女（A／B） | [L08.md](L08.md) | [persona_pack_v1/L08.md](../../persona_pack_v1/L08.md) |
| L09 | T6 攝影人像 | 方士哲 | 36／男 | [L09.md](L09.md) | [persona_pack_v1/L09.md](../../persona_pack_v1/L09.md) |
| L10 | T7 時事新聞 | 邱雅雯「瓜雯」（名字待選） | 32／女 | [L10.md](L10.md) | [persona_pack_v1/L10.md](../../persona_pack_v1/L10.md) |

其他文件：

| 文件 | 內容 |
|---|---|
| [CLIENT_FEEDBACK_2026-10-07.md](CLIENT_FEEDBACK_2026-10-07.md) | 客戶回饋原文、解讀、決策、仍未選定的事項 |
| [MODEL_AND_WORKFLOW_OPTIONS.md](MODEL_AND_WORKFLOW_OPTIONS.md) | 可行的建模流程與工具能力（分「已查證／推論／需製作師確認」） |
| [REFERENCE_AND_ACCEPTANCE.md](REFERENCE_AND_ACCEPTANCE.md) | 要補的參考圖、權利登記、候選人物的審查建議、誰決定形象可用 |
| [PRODUCER_CLAUDE_HANDOFF_PROMPT.md](PRODUCER_CLAUDE_HANDOFF_PROMPT.md) | 製作師可以貼給自己 Claude 的完整 prompt |
| [persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md](../../persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md) | 原有的 OK／NG 參考需求、身分測試標準（§2）、撞臉配對（§4）、估價假設（§6） |
| [persona_pack_v1/00_OVERVIEW.md](../../persona_pack_v1/00_OVERVIEW.md) | 十角色總覽、外型差異地圖、撞臉配對優先順序 |
| [review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md](../../review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md) | 主管覆核 R1（歷史紀錄）。其中「只做詢價、等授權、由 Penny／客戶選定」的分工已被 2026-10-07 責任分工調整取代 |
| [review/CORRECTION_TASK_002_MODELING_PACK_R2.md](../../review/CORRECTION_TASK_002_MODELING_PACK_R2.md) | R2 局部補正紀錄：依主管覆核改了哪些句子、怎麼驗證 |
| [review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2.md](../../review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2.md) | 主管覆核 R2（歷史紀錄；授權與驗收分工同上，已被取代） |
| [review/CORRECTION_TASK_002_MODELING_PACK_R2_M01-M02.md](../../review/CORRECTION_TASK_002_MODELING_PACK_R2_M01-M02.md) | 最後兩項補正紀錄：L08 A 版頭像、形象照備選的計費邊界 |
| [review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2_FINAL.md](../../review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2_FINAL.md) | 主管最後核對（歷史紀錄；文件內容 PASS。其中「生成、付費、訓練要另行授權」「形象由 Penny／客戶選定」已被 2026-10-07 責任分工調整取代） |
| [review/RESPONSIBILITY_CHANGE_TASK_002_2026-10-07.md](../../review/RESPONSIBILITY_CHANGE_TASK_002_2026-10-07.md) | **2026-10-07 責任分工調整**：Penny 的指示原文與改了哪些分工；以這份為準 |

## 3. 版本來源與決定狀態

**以哪份為準**
- 角色設定：`persona_pack_v1/Lxx.md`。建模頁只摘錄建模需要的部分；兩者不一致時以人設檔為準，並回報。
- 建模規格與 prompt：本資料夾的 `Lxx.md`。
- 客戶決定：`CLIENT_FEEDBACK_2026-10-07.md`。
- 本包的版本：以 GitHub 分支 `claude/luscena-kol-initial-draft-et17t8` 上、`PRODUCER_CLAUDE_HANDOFF_PROMPT.md` 的「交付版本」（或交接時另外指定的 commit）為準。R1 的內容 commit `3cb0a0c` 缺少部分必讀檔案，不要再用。讀之前先記錄 `git rev-parse HEAD`，並確認交接 prompt【必讀】列出的檔案都存在；缺檔就請交接的 Penny 補交（這是交付問題，不是製作批准），不要用其他版本的檔案補。

**客戶已接受、已決定的**
- 整體十角色方向。
- 十個帳號是同一團隊這件事先不公開；角色之間的互動與客串照常。
- 被問到 AI 身分時不否認；影片照平台規定處理。
- AI 揭露方式交由團隊評估，**目前尚未決定**。

**仍未選定（建模時不能當成已選）**
- **L08 定位**（C-L08-1）：A 女球迷／B 啦啦隊舞者兼死忠球迷／C 男球迷「啦啦隊迷」／D 場邊主持。團隊建議優先討論 B，**客戶尚未選 B**。
- **L02 的尺度與角色來源**（C-L02-1、C-L02-2）、**L03 的尺度**（C-L03-1）：建模先用保守的尺度 1、原創作為起點；尺度 2 與同人是待確認的分支。
- **其他會影響外型的選項**：L01、L04、L07 的風格方向；L04 瀏海；L05 寫實與 Q 版的搭配、年齡處理；L06 身形；L07、L10 眼鏡頻率；L09 鬍子與髮型；L02 頭像；G-4 寫實程度。
- 每個建模頁的 C 節列出該角色的待選項。
- 這些待選項目由製作師提出方案、做比較，依其與客戶的流程決定；不退回 Penny，也不要寫成客戶已選。需要實質改變客戶的人設方向時，列出差異並向客戶確認。

## 4. 本包的 prompt 只是建議

- 每份建模頁都提供英文 prompt（BASE_IDENTITY、NEUTRAL_CASTING、IDENTITY_CHECK、SIGNATURE_PORTRAIT），附中文解釋。
- **文字 prompt 不能保證每次都是同一張臉。** 鎖定候選之後，要附參考圖，或用角色模型維持身分，並逐張人工檢查。
- 製作師可以採用自己的工具與流程，例如角色產生器、單張參考圖的角色元素、專屬角色訓練。請回報實際用了什麼、為什麼、取捨是什麼（見各建模頁 I 節與 `MODEL_AND_WORKFLOW_OPTIONS.md`）。
- 不要求仿製任何真人、名人或既有 KOL 的臉；所有角色都是原創、成年人。

## 5. 建議的進行順序（參考；製作師可以照自己的流程）

1. **先確認**：可用的工具與帳號方案、參考素材的權利、待選分支。費用與額度由製作師依帳號權限與客戶約定處理，不需要 Penny 批准。
2. **分批出臉部候選**：不要一次鎖定十張臉。建議先做撞臉優先 1 的配對（L02↔L10、L01↔L08、L05↔L06）各自的候選，並排比較。
3. **選定身分參考圖 A**（製作師選定，或依其流程交客戶選定）之後，再做身分測試（低方案 T1–T3、中方案 T1–T8）。全身照 B、造型變化等新增檢查的估價歸類見 `REFERENCE_AND_ACCEPTANCE.md` §7。
4. 身分測試通過，再做形象照。
5. 每一批照 `REFERENCE_AND_ACCEPTANCE.md` §4.3 的格式記錄，依製作師的流程交客戶或留存。

## 6. 怎麼回報

每一批請記錄（寫進製作師自己工作分支的 REPORT.md，或依製作師與客戶約定的方式交付）：
- 使用的工具、模型名稱與版本、prompt 全文、參考圖編號與來源；
- 生成張數、交付張數、實際花費（以帳戶實際扣除為準；不要用估算值冒充實際值）；
- 依 `REFERENCE_AND_ACCEPTANCE.md` §4.1 的審查結果，以及失敗樣本與原因；
- 需要客戶決定的事項（由製作師依其流程向客戶確認）。

成果與紀錄如何寫回 repo，見 `PRODUCER_CLAUDE_HANDOFF_PROMPT.md`。

## 7. 重要提醒

- 生成完成不等於形象定案；形象由製作師判斷可用，或依其流程交客戶選定與驗收後才定案。
- 不在任何素材或文案裡公開「十個帳號是同一團隊」；也不做假裝獨立第三方的推薦、背書或假讀者回應。
- AI 揭露方式尚未決定：不要寫成「一律不用標示」；平台或工具要求的標示照規定。
