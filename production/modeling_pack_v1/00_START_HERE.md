# 十角色 AIGC 建模交付包：從這裡開始

> **給製作師**：這個資料夾是 Luscena KOL 十個虛擬角色的建模交付包。它把已完成的文字人設整理成可以直接建模的規格與 prompt。
> **狀態**：PROPOSED。客戶在 2026-10-07 接受了整體十角色方向，但還有幾個選項沒選定（見第 3 節）。**文字人設被接受，不等於生成出來的人物形象已驗收。**
> 本包只是文件：沒有生成任何圖片、沒有訓練人物、沒有付費、沒有建立帳號或發布。

---

## 1. 任務目標

1. 為十個角色各建立一張**原創、成年、可重複使用的臉與體態**。
2. 十個人要彼此分得開，而且不只靠髮型、髮色或衣服分開。
3. 同一個角色換角度、換表情、換造型時，仍然是同一個人。L02 凜換不同的幻想角色服時，仍是同一張臉。
4. 先交**候選與方法**，由 Penny／客戶看圖選定，再鎖定形象。

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
| [REFERENCE_AND_ACCEPTANCE.md](REFERENCE_AND_ACCEPTANCE.md) | 要補的參考圖、權利登記、候選人物的審查與鎖定規則 |
| [PRODUCER_CLAUDE_HANDOFF_PROMPT.md](PRODUCER_CLAUDE_HANDOFF_PROMPT.md) | 製作師可以貼給自己 Claude 的完整 prompt |
| [persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md](../../persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md) | 原有的 OK／NG 參考需求、身分測試標準（§2）、撞臉配對（§4）、估價假設（§6） |
| [persona_pack_v1/00_OVERVIEW.md](../../persona_pack_v1/00_OVERVIEW.md) | 十角色總覽、外型差異地圖、撞臉配對優先順序 |

## 3. 版本來源與決定狀態

**以哪份為準**
- 角色設定：`persona_pack_v1/Lxx.md`。建模頁只摘錄建模需要的部分；兩者不一致時以人設檔為準，並回報。
- 建模規格與 prompt：本資料夾的 `Lxx.md`。
- 客戶決定：`CLIENT_FEEDBACK_2026-10-07.md`。
- 本包的版本：以 GitHub 分支 `claude/luscena-kol-initial-draft-et17t8` 上、加入本包的 commit 為準（實際 SHA 見 `review/REVIEW_REQUEST_TASK_002_MODELING_PACK_R1.md`）。

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

## 4. 本包的 prompt 只是建議

- 每份建模頁都提供英文 prompt（BASE_IDENTITY、NEUTRAL_CASTING、IDENTITY_CHECK、SIGNATURE_PORTRAIT），附中文解釋。
- **文字 prompt 不能保證每次都是同一張臉。** 鎖定候選之後，要附參考圖，或用角色模型維持身分，並逐張人工檢查。
- 製作師可以採用自己的工具與流程，例如角色產生器、單張參考圖的角色元素、專屬角色訓練。請回報實際用了什麼、為什麼、取捨是什麼（見各建模頁 I 節與 `MODEL_AND_WORKFLOW_OPTIONS.md`）。
- 不要求仿製任何真人、名人或既有 KOL 的臉；所有角色都是原創、成年人。

## 5. 建議的進行順序

1. **先確認**：可用的工具與帳號方案、參考素材的權利、待選分支、費用上限。生成與訓練要先取得 Penny 的授權與費用上限。
2. **分批出臉部候選**：不要一次鎖定十張臉。建議先做撞臉優先 1 的配對（L02↔L10、L01↔L08、L05↔L06）各自的候選，並排比較。
3. **Penny／客戶選定**之後，才做身分測試（T1–T8）。
4. 身分測試通過，再做形象照。
5. 每一批都照 `REFERENCE_AND_ACCEPTANCE.md` §4.3 的格式回報。

## 6. 怎麼回報

每一批候選請回報：
- 使用的工具、模型名稱與版本、prompt 全文、參考圖編號與來源；
- 生成張數、交付張數、實際花費（以帳戶實際扣除為準；不要用估算值冒充實際值）；
- 依 `REFERENCE_AND_ACCEPTANCE.md` §4.1 的審查結果，以及失敗樣本與原因；
- 需要 Penny／客戶決定的事項。

成果與紀錄如何寫回 repo，見 `PRODUCER_CLAUDE_HANDOFF_PROMPT.md`。

## 7. 重要提醒

- 生成完成不等於形象核准；人物形象要 Penny／客戶看圖選定後才鎖定。
- 不在任何素材或文案裡公開「十個帳號是同一團隊」；也不做假裝獨立第三方的推薦、背書或假讀者回應。
- AI 揭露方式尚未決定：不要寫成「一律不用標示」；平台或工具要求的標示照規定。
