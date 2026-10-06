# Luscena KOL

依客戶要求，在 Threads 規劃 10 個虛擬角色帳號：3 個主帳號、7 個流量帳號。在符合平台規範、揭露虛擬身分與品牌關係的前提下，把流量導向 LUSCENA。

- **Owner**：Penny
- **規劃主管與覆核**：ChatGPT
- **執行者**：Claude
- **目前階段**：TASK-001 R2（人設優先），**等 Penny 與主管審閱人設**
  - 2026-10-06 Penny 調整範圍：先把 10 個人設規劃清楚，讓 Penny 選定，再交給 AIGC 製作師評估人物形象。導流與網站轉換延後到角色建立、帳號創建、實際每日經營之後另案討論（`review/SCOPE_CHANGE_TASK_001_2026-10-06.md`）。
  - 全部內容都是 PROPOSED，**沒有任何一項經 Penny 或客戶核准**。
  - 沒有建立帳號、沒有發布、沒有修改客戶網站、沒有生圖或付費、沒有訓練人物。

> **Penny 請從這裡看**：`persona_pack_v1/00_OVERVIEW.md`（十角色總覽）→ 各角色 `persona_pack_v1/Lxx.md` → `persona_pack_v1/PENNY_CHOICES.md`（勾選）→ `persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md`（交給製作師）。

> R1 背景（保留，不在本輪討論）：LUSCENA 是 18+ 成人直播與內容平台；R1 主管覆核把中期導流判定為 BLOCK（`review/REVIEW_RESPONSE_TASK_001_R1.md`）。

## 文件導航

| 順序 | 文件 | 內容 |
|---|---|---|
| ★ | `persona_pack_v1/00_OVERVIEW.md` | **R2 人設審閱包：十角色總覽** |
| ★ | `persona_pack_v1/L01.md`～`L10.md` | 每個角色的詳細提案（取代 v0 的人設部分） |
| ★ | `persona_pack_v1/PENNY_CHOICES.md` | Penny 需要選擇的事項 |
| ★ | `persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md` | 給 AIGC 製作師的參考需求（OK／NG 都是待選） |
| ★ | `review/SCOPE_CHANGE_TASK_001_2026-10-06.md` | 範圍調整紀錄 |
| ★ | `review/REVIEW_REQUEST_TASK_001_R2_PERSONA.md`、`review/INTERNAL_QA_TASK_001_R2_PERSONA.md` | R2 人設覆核請求與內部核查 |
| R1 | `review/REVIEW_RESPONSE_TASK_001_R1.md` | R1 主管覆核結果 |
| 1 | `review/REVIEW_REQUEST_TASK_001_R1.md` | 主管覆核包：結論、風險、Q1–Q7 |
| 2 | `brief/CLIENT_IMAGE_TRANSCRIPT.md` | 客戶圖片逐字稿（原圖：`brief/source/`） |
| 3 | `brief/CLIENT_REQUIREMENTS.md` | CR-001 起的結構化需求；需求衝突 E-1～E-7 |
| 4 | `research/LUSCENA_AUDIT.md` | 網站研究：業務、價格、流程、追蹤、落地頁 |
| 5 | `research/THREADS_RESEARCH.md` | Threads 帳號樣本、Meta 官方規則查核、政策風險初判 |
| 6 | `research/REFERENCE_METHODS.md` | 舊 KOL Studio 可沿用的方法與失敗教訓 |
| 7 | `research/EVIDENCE_INDEX.md` | 證據總索引（EV 編號） |
| 8 | `plan/ACCOUNT_MATRIX_V0.md` | 10 個帳號總體矩陣 v0（角色事實已改以 persona_pack_v1 為準） |
| 9 | `personas/L01`～`L10/character_v0.md` | 10 個角色的 v0 初稿（歷史紀錄，人設部分已由 persona_pack_v1 取代） |
| 10 | `production/VISUAL_BRIEF_V0.md` | 視覺與 AIGC 製作規格（只有規格） |
| 11 | `plan/THREADS_OPERATING_PLAN_V0.md` | 營運、產能、成本、導流、UTM、指標、追蹤規格 |
| 12 | `plan/PILOT_PLAN_V0.md` | 分批上線、檢查點、中期條件、停止條件 |
| 13 | `docs/PROJECT_BRIEF.md` | 前提、提案、未知 |
| 14 | `docs/CLIENT_QUESTIONS.md` | 待客戶確認的問題 |
| 15 | `review/INTERNAL_QA_TASK_001_R1.md` | 提交前的內部核查紀錄（問題與修正） |

## 帳號對照

| ID | 客戶格 | 暫定角色 |
|---|---|---|
| L01 | A 兩性話題 | 簡予安 |
| L02 | B 大尺度 Cos | 凜 Rin |
| L03 | C 性感身材時尚 | 周以晨 |
| L04 | T1 星座命理 | 林可妮 |
| L05 | T2 迷因梗圖 | 陳柏凱「阿凱」 |
| L06 | T3 電玩手遊 | 黃子翔「翔哥」 |
| L07 | T4 AI 科技 | 程翊 |
| L08 | T5 運動賽事／啦啦隊 | 蔡沛岑「沛沛」 |
| L09 | T6 攝影人像 | 方士哲 |
| L10 | T7 時事新聞 | 邱雅雯「瓜雯」 |

## 標記規則

| 標記 | 意思 |
|---|---|
| 客戶明說（CR-xxx） | 客戶圖片上有的要求 |
| PROPOSED | 執行者的提案，未經核准 |
| UNKNOWN／待確認 | 尚未確認 |
| INTERPRETATION | 執行者對客戶原文的解讀 |
| 【站證】【推論】【待確】 | 網站研究的證據等級 |

## Repo 規則

- 不提交帳密、token、私人聯絡資料。帳號的帳密存在客戶指定的密碼管理工具。
- 不提交含真實創作者影像或性內容的截圖。
- 參考 repo `pennyhuang-oss/Virtual_KOL_Studio` 只讀，不修改。
- 角色事實以 `persona_pack_v1/` 為準；v0 文件保留為歷史紀錄。
