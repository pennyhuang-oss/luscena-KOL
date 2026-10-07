# 責任分工調整：TASK-002 建模交付包（2026-10-07）

- 依據：Penny 2026-10-07 的最新指示（下方引用）。這份指示**優先於**先前文件與主管覆核中的授權、選臉及驗收安排。
- 分支：`claude/luscena-kol-initial-draft-et17t8`；調整前 HEAD `9b540cb4174d6ad52ba079fb1dd141503cbd98b4`（主管最後核對）
- 內容 commit：`ef096d8074eace9b297fb7c2241092a0fbaead73`。下一個 commit 只把這個 SHA 填進交接 prompt 與本檔。
- 執行者：Claude。本次只修文件，沒有替製作師生成或訓練；沒有修改主管覆核文件、沒有更新 main、沒有 force push 或改寫歷史。

## 1. Penny 的指示（引用）

> 【正確分工】
> Penny 只負責初步人設建立與交付。
> AIGC 製作師接手後，自行決定工具、模型、生成、訓練、參考圖、製作方法及迭代流程。
> 建模成果由製作師自行判斷是否可用，或依他的工作流程提交客戶選定、驗收與定案。
> 不需要 Penny 批准生成、訓練、選臉、鎖定身分或核准形象。
> 費用、額度及製作範圍由製作師依其帳號權限與客戶約定處理，不設 Penny 為付款或製作批准人。
> 人設規格、prompt、測試張數和模型流程都是供製作師參考的建議，不強制他照做。

> 待選項目不要假稱客戶已選。製作師可提出方案、做比較，並依其與客戶的流程決定；不要將所有選項退回 Penny。
> 若需要實質改變客戶的人設方向，列出差異並向客戶確認。

## 2. 被取代的舊分工

主管覆核文件保留不改，作為歷史紀錄。以下文件中的**授權與驗收分工**已被本指示取代；其中對文件內容的修正（左右、prompt 組裝、測試範圍、估價歸類等）仍然有效，已併入現行檔案。

| 文件 | 被取代的部分 |
|---|---|
| `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md` | 製作師只做可行性討論與條件式詢價；生成、付費、訓練要另行授權 |
| `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2.md` | 同上；實際聯絡與製作等 Penny 指派、授權 |
| `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2_FINAL.md` | 「實際生成、付費或訓練仍需對應的授權、費用範圍」「人物形象仍由 Penny／客戶看圖選定」 |
| 先前版本的 `PRODUCER_CLAUDE_HANDOFF_PROMPT.md` | 只做規劃與詢價、等 Penny 授權與費用上限、由 Penny／客戶選臉、每批停下等 Penny 與主管 |

## 3. 改了哪些分工

| 項目 | 舊寫法 | 新寫法 | 位置 |
|---|---|---|---|
| 生成、訓練、付費 | 取得 Penny 的授權與費用上限前不得進行 | 由製作師依帳號權限與客戶約定處理，不需要 Penny 批准；記錄實際張數與花費 | 十頁 I 節最後一點；`00_START_HERE` §5；`REFERENCE_AND_ACCEPTANCE` §6、§7；`PRODUCER_REFERENCE_NEEDS` 開頭、§5、§6；交接 prompt |
| 選臉、身分參考圖 A／B | Penny／客戶挑選後才成為 A；Penny 選定全身 B | 製作師挑選，或依製作師流程交客戶選定；A／B 由製作師建立與管理 | 十頁 G-2 說明與 H 第 2 步；L03 H 第 3 步；L05 Q 版定稿；`MODEL_AND_WORKFLOW_OPTIONS` 流程 1、2；`REFERENCE_AND_ACCEPTANCE` §2 |
| 鎖定與核准形象 | Penny 與客戶看圖選定才鎖定；製作師不能自己宣布 | 由製作師判斷可用，或依其流程交客戶選定、驗收與定案；不需要 Penny 批准 | 十頁開頭狀態；`00_START_HERE` §1、§7；`REFERENCE_AND_ACCEPTANCE` §5；README |
| 每批停下等批准 | 完成後通知 Penny 並停下等 Penny 與主管覆核；先回覆、不要開始生成 | 讀完後向製作師說明計畫，依製作師指示直接開始；成果寫進製作師自己的工作分支 | 交接 prompt；`00_START_HERE` §5、§6 |
| 待選項目 | 等 Penny 選；條件項只列價、不替 Penny 啟用 | 製作師提出方案、做比較，依其與客戶的流程決定；客戶確認前不當成已選；不退回 Penny | 各頁 C 節相關句（L02、L03、L04、L05、L06、L07、L08、L09、L10）；`REFERENCE_AND_ACCEPTANCE` §6；`PRODUCER_REFERENCE_NEEDS` 條件列 |
| 人設方向的實質改變 | 由 Penny 決定（例如 L05 改年齡、L08「舞者」新增設定、L03 平口斜裁） | 製作師列出差異，向客戶確認 | L03、L05、L08 |
| 測試張數、prompt、流程 | 低／中方案與 §7 歸類作為報價依據 | 都是建議，不強制照做；範圍與費用由製作師與客戶約定 | `REFERENCE_AND_ACCEPTANCE` §7；`PRODUCER_REFERENCE_NEEDS` §6；交接 prompt |
| 交接版本缺檔 | 停下回報 Penny | 請交接的 Penny 補交（交付問題，不是製作批准） | `00_START_HERE` §3；交接 prompt |

**修改的檔案**：`production/modeling_pack_v1/` 的 `00_START_HERE.md`、`L01.md`～`L10.md`、`MODEL_AND_WORKFLOW_OPTIONS.md`、`REFERENCE_AND_ACCEPTANCE.md`、`CLIENT_FEEDBACK_2026-10-07.md`（只加一行註記）、`PRODUCER_CLAUDE_HANDOFF_PROMPT.md`（重寫）；`persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md`；`README.md`；`review/qa/check_t2.py`（必讀清單改為 27 個檔案，加一個舊分工字串檢查）。

## 4. 保留不變

- 十角色的外型規格、英文 prompt 本文、撞臉配對與身分特徵沒有改；沒有重新啟動人設覆核。
- 製作要求保留：原創、成年；不仿製真人、名人或既有角色；不越過各角色 §10；身分一致性與左右（角色本人）；十人區隔不只靠髮型或服裝；工具條款與 NSFW、IP 限制；用生成圖訓練前確認許可；素材權利登記；失敗樣本與原因；實際張數與花費的紀錄。
- 客戶回饋保留：不公開十個帳號是同一團隊；不做假背書、假讀者回應或掩飾共同管理的方案；AI 揭露方式尚未決定，被問到不否認；影片照平台規定。
- 待選項目仍是待選，沒有寫成客戶已選。
- GitHub 回寫仍用製作師自己的工作分支；不推 main、不改寫既有 commit、不修改人設內容與歷史覆核文件。
- 建立帳號、發布、導流與網站規劃仍不在建模範圍。

## 5. 驗證

- 字串檢查（`grep`，提交前）：`production/modeling_pack_v1/`、`persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md`、`README.md` 中，舊分工字串（「先取得 Penny」「Penny 的授權」「Penny／客戶挑選」「Penny／客戶看圖選定」「Penny 選定」「費用上限」「要先授權」「送覆核」「停下等她」等）只出現在本紀錄與明寫「已取代／已取消／歷史」的說明句裡。
- 腳本只是字串與檔案存在性檢查，不代表語意全部正確；責任分工的語句是逐處人工改寫並讀過。
- 交接 prompt 的 27 個必讀檔案：提交後以 `git cat-file -e ef096d8:<路徑>` 逐一確認，27／27 存在。
- `python3 review/qa/check_t2.py .`（內容 commit）：十頁 OK；`00_START_HERE` 連結無法解析的為 none；R2 字串檢查 none；舊分工字串 none；必讀 27 個檔案都存在；九份主管覆核檔 blob 與原本相同。
