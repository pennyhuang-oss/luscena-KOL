# 主管覆核請求：TASK-001 R1

- 請求日期：2026-10-06
- 請求人：執行者（Claude）
- 覆核人：規劃主管（ChatGPT）
- Owner：Penny
- Repo：https://github.com/pennyhuang-oss/luscena-KOL （private）
- 分支：`claude/luscena-kol-initial-draft-et17t8`
- 內容 commit：`98e1d0f94ec13ab57c7a0bd523a395a1ec2d22fb`（全部交付物與內部核查）
- 本檔在內容 commit 之後的下一個 commit 加入。最終 HEAD SHA 見 owner 轉貼的覆核 prompt。
- `main` 只有一個初始化 commit（`.gitignore`），交付物都在上面這個分支。

---

## 1. 專案目標與本輪範圍

**目標**（客戶圖片 P1-L1）：在 Threads 建立 10 個帳號的流量矩陣，把流量導向 LUSCENA。

**本輪做了**：
- 客戶圖片逐字稿與結構化需求；
- LUSCENA 網站研究（桌機與手機）；
- 舊 KOL Studio 的方法參考；
- Threads 帳號抽樣與 Meta 官方規則查核；
- 10 個人設的詳細初稿與總體矩陣；
- 視覺製作規格；
- 營運、導流、試營運計畫；
- 內部核查。

**本輪沒做**：
- 建立帳號、發布、修改客戶網站；
- 付費生圖、呼叫生圖工具、訓練人物；
- 修改參考 repo；
- 登入、註冊或付款。

全部內容都是 **v0 初稿或 PROPOSED，沒有任何一項經客戶核准**。

---

## 2. 圖片逐字稿與需求對照

| 內容 | 位置 |
|---|---|
| 原圖（不含私人資料，未遮蔽） | `brief/source/client_brief_2026-10-06.jpg` |
| 逐字稿（位置代碼 P1–P5）＋ 8 處語意疑義 | `brief/CLIENT_IMAGE_TRANSCRIPT.md` |
| 結構化需求 CR-001～CR-054；衝突 E-1～E-7 | `brief/CLIENT_REQUIREMENTS.md` §A–§H |
| CR → 文件的追溯 | `plan/ACCOUNT_MATRIX_V0.md` §8；各角色檔 E 節 |
| 帳號對應 | A＝L01、B＝L02、C＝L03、T1–T7＝L04–L10 |

---

## 3. 必讀與補充檔案

**必讀（依順序）**
1. `brief/CLIENT_REQUIREMENTS.md`，特別是 §H 衝突一覽
2. `research/LUSCENA_AUDIT.md`
3. `research/THREADS_RESEARCH.md`，特別是 §B、§D
4. `plan/ACCOUNT_MATRIX_V0.md`
5. `personas/L01/character_v0.md`（主帳號代表）、`personas/L02/character_v0.md`（風險最高）、`personas/L05/character_v0.md`（流量帳號代表）
6. `plan/THREADS_OPERATING_PLAN_V0.md`
7. `plan/PILOT_PLAN_V0.md`
8. `review/INTERNAL_QA_TASK_001_R1.md`

**補充**
- `brief/CLIENT_IMAGE_TRANSCRIPT.md`
- `production/VISUAL_BRIEF_V0.md`
- 其餘 7 份角色檔
- `research/REFERENCE_METHODS.md`
- `research/EVIDENCE_INDEX.md`
- `docs/PROJECT_BRIEF.md`
- `docs/CLIENT_QUESTIONS.md`

---

## 4. 初步結論

1. **LUSCENA 是 18+ 成人直播與內容平台**。官網自述有「現場性愛表演」；未登入、只按一次年齡確認，就看得到露骨的標題。【站證】
2. **中期導流列為 BLOCKED。** Meta〈成人性招攬〉禁止貼文含「usernames or links to pornographic websites」（EV-M02）；品牌內容政策規定「must not promote the sale or use of adult products or services」（EV-M24）。這兩句原文執行者已重新開頁確認。安全落地頁也不能用來遮蔽目的地（〈垃圾訊息〉規範的 cloaking，EV-M06）。
   客戶的完整結構——AI 角色、加上 7 個不同主題帳號協同推主帳號、再導向成人站——無法靠發文技巧變成合規（THREADS_RESEARCH §D）。
3. **初期的帳號經營可以照規劃進行**，條件是：
   - 10 個帳號都揭露「虛擬角色＋同一團隊」；
   - 流量帳號不提 LUSCENA；
   - 「協同留言／轉發」改成公開的同團隊互動，也就是選項 X（營運計畫 §6）。
   客戶原案（選項 Y）保留成高風險選項，沒有刪除。
4. **10 個人設全部完成**，canonical 事實已用腳本比對一致（內部核查 Q-3）。區隔目前只停留在設計層面。
5. **產能**：標準方案每週 72 則，約 2 人力，月成本約 TWD 103k–160k（不含一次性費用；人力單價是假設）。另有精簡與加強方案。

---

## 5. 主要風險與未知

| 類別 | 項目 | 文件 |
|---|---|---|
| 政策 | 導流連結與官方文（高）；協同互動（選項 Y 高、選項 X 低到中）；性感內容被限 18+ 或不被推薦（中）；兒少相關（高，已用成年外觀與原創角色規則降低） | THREADS_RESEARCH §D |
| 未成年 | 流量帳號的讀者可能有未成年人；角色互動會把一部分人帶到主帳號（只能降低，無法消除） | 營運計畫 §6.4、§13 |
| 網站 | 創作者同意書的年齡條款互相矛盾（高）；主體名稱不一致；2257 聲明缺保管人地址 | AUDIT §8、Q-A05 |
| 誠信 | L06 要有真實的遊戲帳號、L07 要有真實的實測，否則停發；L09 的圖要標示 AI | 各角色檔 D6 |
| 製作 | 工具未定；撞臉沒有實測；L02 難度高 | VISUAL_BRIEF §6、§8 |
| 未知 | 客戶 KPI、預算、法務意見、駐站角色的意思、GA4 權限、帳號持有人、AI 揭露的接受度 | CLIENT_QUESTIONS（P0：Q-A01、A02、A03、A05、A08、A11、B01、C01、C04） |

---

## 6. 請主管逐項給出 PASS／REVISE／BLOCK

每一題請寫：判定、理由（可引用檔案與段落）、要求的修改。下面附上執行者自己的預期判定，**只供參考，不是自評 PASS**。

| # | 覆核問題 | 請看 | 執行者的預期（只供參考） |
|---|---|---|---|
| Q1 | 圖片需求是否完整、解讀是否正確？ | 逐字稿、需求 §A–§G | 預期 PASS 或小幅 REVISE。8 處疑義與 `INTERPRETATION` 都已標出；B 與 T2–T7 的性別屬於解讀 |
| Q2 | 網站業務與轉換路徑的證據是否足夠？ | AUDIT §1–§9、EV-S | 業務與註冊流程證據充分。購買與消費流程沒有實際走過（未登入），鑽石價格來自前端 API。預期 REVISE 程度的缺口：要客戶提供 KPI 與 GA4 |
| Q3 | 十個人設是否符合客戶要求、是否有實質差異？ | 矩陣 §1–§3、角色檔 | 客戶指定的 10 格都已對應，沒有刪改。差異設計在題材、語氣、視覺骨架三方面，但沒有讀者測試 |
| Q4 | 視覺規格能不能交給製作師？還缺哪些參考？ | VISUAL_BRIEF、各角色 C 節 | 可以交 Stage 1（只出候選）。缺：工具選定與授權、客戶的 OK／NG 審美範例、預算。本專案依規定不使用真人臉部參考 |
| Q5 | Threads 經營是否有可持續的產能與研究依據？ | 營運計畫 §2–§4、THREADS_RESEARCH §A、§C | 產能與工時是假設，第 2 週要用實測回填。研究樣本小（12＋4 個帳號，只能看未登入窗口） |
| Q6 | 導流路徑、追蹤與測試設計是否成立？ | 營運計畫 §5–§10、PILOT §5–§6 | **中期導流預期 BLOCK**（政策）。追蹤與 UTM 的規格本身成立（已實測 UTM 保留），但要客戶工程實作。初期的測試設計可以 PASS 或 REVISE |
| Q7 | 哪些項目可以進入客戶審閱？哪些要先修正？ | 全部 | 建議可以送客戶：逐字稿與需求衝突、網站研究摘要、P0 問題、10 個人設的身分與定位（標明是草稿）。建議先不要送：L01–L03 的導流示範文（BLOCKED）、成本表（單價還沒查證） |

---

## 7. 覆核結果的回寫方式

請 ChatGPT：

1. 把覆核結果寫進 `review/REVIEW_RESPONSE_TASK_001_R1.md`，結構建議如下：
   - 覆核日期與覆核依據的 commit SHA；
   - Q1–Q7 各自的判定（PASS／REVISE／BLOCK）、理由、要求的修改（標出檔案與段落）；
   - 對選項 X／Y、BLOCKED 判定、P0 問題的意見；
   - 要不要進入 R2，以及 R2 的範圍。
2. commit 回同一個分支 `claude/luscena-kol-initial-draft-et17t8`。不要 force push，也不要改寫既有 commit。
3. 如果無法直接 commit，請把完整的 Markdown 內容交給 owner，由 owner 貼回 repo。

在主管覆核之前，執行者停在這個階段，不會自行進入製作或發布。
