# 補正紀錄：TASK-002 R2 最後兩項（R2-M01、R2-M02）

- 日期：2026-10-07
- 執行者：Claude；Owner：Penny
- 依據：主管覆核 `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2.md`（主管 commit `defbd0bb00442bb1e1c6b7215f5d9602516ccde8`，判定 REVISE，只剩 R2-M01、R2-M02）
- 分支：`claude/luscena-kol-initial-draft-et17t8`；開工時 HEAD `defbd0b`；遠端 main `2283244aa0c01343361d0100b185732809b617af`（沒有更新）
- 內容 commit：`[R2M_CONTENT_SHA]`（下一個 commit 補上；不追同檔自指）
- 範圍：只改這兩項，加上交接版本、導覽與核查腳本的必要更新。已通過的 T2-F01、F02 指定部分、F04、F05、F06 不重開；不全面重寫十角色；不替客戶選角（L08 定位 C-L08-1 仍待選）。R2 原紀錄 `review/CORRECTION_TASK_002_MODELING_PACK_R2.md` 保留不改。
- 沒有生成、付費、訓練、開帳號、發布、聯絡製作師或重開導流；沒有修改主管覆核文件；沒有 force push 或改寫歷史。全部仍是 PROPOSED。

---

## 1. R2-M01：L08 G-4 A 版頭像

- 位置：`production/modeling_pack_v1/L08.md` G-4「A 版頭像」（B 版頭像 prompt 正下方）
- 原句：

> A 版頭像：把服裝那一句換成 `Plain crew-neck T-shirt and a plain baseball cap with no logo, brim raised so both eyebrows and eyes stay visible, bare face with a sunscreen-only look.`

- 新句（兩句同步替換，並附完整 A 版）：

> A 版頭像（只在 C-L08-1 選 A 時用；定位仍**待選**）：以上面的 B 版頭像為底，**服裝句與妝容句兩句一起換**，其餘（鏡位、表情、背景、光線、比例、Avoid）不變：
> - 服裝句 `Upper part of an original cheer-dance performance top in [TROUPE COLORS] for a fictional adult dance troupe, with a matching headband holding back her ear-length bob.` 換成 `Plain crew-neck T-shirt and a plain baseball cap with no logo, brim raised so both eyebrows and eyes stay visible, her ear-length bob showing under the cap.`
> - 妝容句 `Light everyday makeup, freckles on her nose and cheeks visible.` 換成 `Bare face with a sunscreen-only look, freckles on her nose and cheeks visible.`
>
> 只換服裝句、留下 B 版的淡妝句，會變成「素顏」和「淡妝」互相矛盾。換好之後的完整 A 版頭像：
>
> ```text
> The same woman as in the attached identity reference image, keep her face identical. Chest-up portrait, front view turned very slightly, eye level, face filling more than half of the square frame. Big open laugh showing her teeth, eyes on the camera. Plain crew-neck T-shirt and a plain baseball cap with no logo, brim raised so both eyebrows and eyes stay visible, her ear-length bob showing under the cap. Bare face with a sunscreen-only look, freckles on her nose and cheeks visible. Plain light-colored background. Soft daylight. Realistic photography, 1:1. Avoid: any real team, league or brand logo, readable text or numbers, school cheerleader look, school uniform, younger look, beauty filter, watermark.
> ```

- B 版頭像的 prompt 一字未改；A 版只在 C-L08-1 選 A 時用，定位仍待選。
- 和 R1 的 A 版服裝句相比，R2 版多了 `her ear-length bob showing under the cap`：B 版被換掉的服裝句原本帶著「耳上短鮑伯」這個髮型條件，換句時一併保留，沒有新增人設以外的特徵。`bare face` 從服裝句移到妝容句，意思不變。

**人工核對（把 A 版全文放回模板逐句讀）**

| 句子 | 對照 | 判讀 |
|---|---|---|
| `The same woman as in the attached identity reference image, keep her face identical.` | B 版同句 | 不變；仍附身分參考圖 A |
| `Chest-up portrait, front view turned very slightly, eye level, face filling more than half of the square frame.` | F 表 #1「胸上，正面略側」 | 鏡位不變 |
| `Big open laugh showing her teeth, eyes on the camera.` | F 表 #1 表情「大笑露齒」（A、B 共用） | 不變 |
| `Plain crew-neck T-shirt and a plain baseball cap with no logo, brim raised so both eyebrows and eyes stay visible, her ear-length bob showing under the cap.` | F 表 #1 A 欄「無標誌棒球帽（帽簷不要遮住眉眼）、素 T」；G-1「Ear-length short bob haircut」 | 素 T、無 logo 帽、抬帽簷保留；短鮑伯保留 |
| `Bare face with a sunscreen-only look, freckles on her nose and cheeks visible.` | B 節妝容列「A：幾乎素顏，防曬加護唇」；雀斑是必須維持的身分特徵 | 素顏防曬外觀與雀斑保留；**B 版的 `Light everyday makeup` 已不在 A 版全文裡**，素顏與淡妝不再矛盾。護唇沒有另寫（看不出差別），沿用 R1 的 `sunscreen-only look` |
| `Plain light-colored background. Soft daylight.` | F 表 #1「單純淺色背景」「柔和日光」 | 不變 |
| `Realistic photography, 1:1.` | 頭像比例 1:1 | 不變 |
| `Avoid: any real team, league or brand logo, readable text or numbers, school cheerleader look, school uniform, younger look, beauty filter, watermark.` | B 版同句 | 和無 logo 帽、素顏一致（`beauty filter` 與素顏方向相同）；沒有和帽子或素 T 衝突的字 |

- 驗證：人工逐句讀如上表；`grep` 確認 A 版全文不含 `Light everyday makeup`；`check_t2.py` 的 R2-M01 欄位檢查（A 版頭像只有一個 prompt 區塊、不含 `Light everyday makeup`、含 `Bare face` 與 `freckles`）。這只是文字層面，沒有圖。

## 2. R2-M02：`REFERENCE_AND_ACCEPTANCE.md` §7 最後一列

- 位置：`production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md` §7「各建模頁的其他檢查怎麼算」表最後一列；另在 §7「基本數量」補一行形象照（必要註記）。
- 原句（最後一列）：

> | 四張形象照以外的候補或比較版本（例如 L10 戴眼鏡的頭像候補、L08 A 版頭像） | 各頁 G-4 | 不在 | 依 §6.4 第 4、6 項另列 |

- 新句（最後一列）：

> | 四張形象照的備選、候補或比較版本（例如 L10 戴眼鏡的頭像候補、L08 A 版頭像） | 各頁 G-4 | 部分在。沿用 §6.2 階段 4：低方案四張各 1 張定稿；中方案四張各 1 張定稿＋各 1 張備選。中方案已含的備選不重複收費 | 超過方案既定備選數量的候補，或另開定位、造型分支的比較版本，才另列（§6.4 第 3、4、6 項）。L10 戴眼鏡頭像候補、L08 A 版頭像要看是佔用既有的備選名額，還是另開分支（L08 依 §6.1、§6.4 第 6 項 A、B 分開估），請製作師在報價說明怎麼歸類，不一概排除也不一概另計 |

- 原句（基本數量）：

> - L05 Q 版設計稿：低方案 7 張、中方案 11 張（§6.2 階段 5），和寫實身分分開估。

- 新句（基本數量，加在前面一行）：

> - 形象照：每角色低方案是各檔 §6 的四張各 1 張定稿；中方案是四張各 1 張定稿＋各 1 張備選（§6.2 階段 4）。
> - L05 Q 版設計稿：低方案 7 張、中方案 11 張（§6.2 階段 5），和寫實身分分開估。

**對照原估價規則（`persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md`）**

| 原規則 | 原文重點 | 新列是否一致 |
|---|---|---|
| §6.2 階段 4 形象照 | 低方案「各檔 §6 的四張，各 1 張定稿」；中方案「四張各 1 張定稿＋各 1 張備選」 | 一致；新列與基本數量都照抄這兩個數字，中方案已含的備選不再另計 |
| §6.4 第 3 項 | 四張形象照（每角色）只含各檔 §6 四張裡出現的造型 | 一致；另開造型分支的比較版本才另列 |
| §6.4 第 4 項 | 四張以外的新造型另列，寫明候選與定稿數 | 一致 |
| §6.1、§6.4 第 6 項 | L08 的 A、B、C、D 分開估 | 一致；L08 A 版頭像要看是佔用既有備選名額還是另開分支，由製作師說明 |
| §6.2 製作師可提替代數量 | 用「原假設／製作師建議／理由」並列 | 沿用 §7 開頭的同一句，沒有改 |

- 沒有重做估價表、沒有新增價格；L05 Q 版 7／11、撞臉不重複計與 45 組另列沒有動。
- 驗證：人工對照上表；`check_t2.py` 的 R2-M02 欄位檢查（§7 含「中方案已含的備選不重複收費」）。

## 3. 交接版本、導覽與腳本的必要更新

| 編號 | 位置 | 原句 → 新句（摘要） | 驗證 |
|---|---|---|---|
| R2-M-H-1 | 交接 prompt 檔頭「交付版本」 | `43bfa51`（R2 內容）→ 最後補正的內容 commit `[R2M_CONTENT_SHA]`；註明 `3cb0a0c`、`43bfa51` 都不要再用 | 下一個 commit 補 SHA；§5 存在性 |
| R2-M-H-2 | 交接 prompt 檔頭交接附件 | 只附主管 R1 → 附主管 R1、R2，寫明 R2 結論與已補兩項、待主管最後核對 | 人工核對 |
| R2-M-H-3 | prompt【Repo 與交付版本】 | 同 H-1 | 同上 |
| R2-M-H-4 | prompt【必讀】標題 | 共 28 個檔案 → 共 30 個 | §5 |
| R2-M-H-5 | prompt【必讀】第 7–10 項 | 新增第 9 項主管 R2 報告、第 10 項本紀錄；「更新的主管覆核」例子改為 R3 | §5 |
| R2-M-S-1 | `00_START_HERE.md` §2 其他文件表 | 新增主管 R2 報告與本紀錄兩列 | 相對連結全部可解析（§4） |
| R2-M-R-1、R-2 | `README.md` 目前階段、導覽表 | 改為「R2 最後兩項補正完成，等主管最後核對」；新增一列 | 人工核對：沒有寫成選角或形象核准 |
| — | `review/qa/check_t2.py` | 必讀清單 28 → 30；blob 清單加主管 R2 報告（`f8e4930b450a1ccca9394d618d59a14c2c6c045c`）；加 R2-M01、R2-M02 兩個欄位檢查 | §4 輸出 |

## 4. 腳本檢查（和上面的人工判讀分開）

> 欄位與字串檢查；退出碼永遠是 0，要看輸出。不能代表語意全通過。

`python3 review/qa/check_t2.py .`（內容 commit 前，工作目錄）：

```text
L01 text_blocks=6 OK
L02 text_blocks=9 OK
L03 text_blocks=9 OK
L04 text_blocks=6 OK
L05 text_blocks=9 OK
L06 text_blocks=6 OK
L07 text_blocks=6 OK
L08 text_blocks=8 OK
L09 text_blocks=6 OK
L10 text_blocks=6 OK
[file] 00_START_HERE.md: exists
[file] CLIENT_FEEDBACK_2026-10-07.md: exists
[file] MODEL_AND_WORKFLOW_OPTIONS.md: exists
[file] REFERENCE_AND_ACCEPTANCE.md: exists
[file] PRODUCER_CLAUDE_HANDOFF_PROMPT.md: exists
[links] 00_START_HERE unresolved: none
[feedback] "依客戶回饋不採用" occurrences in persona_pack_v1: 13
[feedback] Lxx files with 2026-10-07 header note: 10/10
[feedback] same-team lines without a 2026-10-07 note: none
[R2] string/structure anomalies: none
[R2] handoff must-read files: 30 listed in script; missing on disk: none; basename not in handoff: none
[R2] blob REVIEW_RESPONSE_TASK_001_R1.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_R2_PERSONA.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_R3.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_R3_F01-F06.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_R3_F01_FINAL.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_MERGE_MAIN.md: same
[R2] blob REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md: same
[R2] blob REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2.md: same
```

反向測試：同一支腳本對 R2-M01／M02 之前的版本（`git archive 0e7ddbe`，另放入主管 R2 報告）執行，R2 區塊前幾行：

```text
[R2] string/structure anomalies: 2
[R2] REFERENCE_AND_ACCEPTANCE.md: §7 does not say mid-plan alternates are not billed twice
[R2] L08.md: A-version headshot blocks=0
[R2] handoff must-read files: 30 listed in script; missing on disk: review/CORRECTION_TASK_002_MODELING_PACK_R2_M01-M02.md; basename not in handoff: review/CORRECTION_TASK_002_MODELING_PACK_R2_M01-M02.md
[R2] blob REVIEW_RESPONSE_TASK_001_R1.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_R2_PERSONA.md: same
```

說明：舊版的 A 版頭像是一行替換指示、沒有完整 prompt 區塊，所以腳本報的是「A 版區塊數＝0」；它不會判讀任意寫法的矛盾，矛盾是靠 §1 的人工逐句讀確認的。

## 5. 交接必讀檔案的存在性（30 個）

| # | 必讀檔案 | 工作目錄（提交前） | 內容 commit（`git cat-file -e`） |
|---|---|---|---|
| 1 | `production/modeling_pack_v1/00_START_HERE.md` | 存在 | 待下一個 commit 補上 |
| 2 | `production/modeling_pack_v1/L01.md` | 存在 | 待下一個 commit 補上 |
| 3 | `production/modeling_pack_v1/L02.md` | 存在 | 待下一個 commit 補上 |
| 4 | `production/modeling_pack_v1/L03.md` | 存在 | 待下一個 commit 補上 |
| 5 | `production/modeling_pack_v1/L04.md` | 存在 | 待下一個 commit 補上 |
| 6 | `production/modeling_pack_v1/L05.md` | 存在 | 待下一個 commit 補上 |
| 7 | `production/modeling_pack_v1/L06.md` | 存在 | 待下一個 commit 補上 |
| 8 | `production/modeling_pack_v1/L07.md` | 存在 | 待下一個 commit 補上 |
| 9 | `production/modeling_pack_v1/L08.md` | 存在 | 待下一個 commit 補上 |
| 10 | `production/modeling_pack_v1/L09.md` | 存在 | 待下一個 commit 補上 |
| 11 | `production/modeling_pack_v1/L10.md` | 存在 | 待下一個 commit 補上 |
| 12 | `production/modeling_pack_v1/MODEL_AND_WORKFLOW_OPTIONS.md` | 存在 | 待下一個 commit 補上 |
| 13 | `production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md` | 存在 | 待下一個 commit 補上 |
| 14 | `production/modeling_pack_v1/CLIENT_FEEDBACK_2026-10-07.md` | 存在 | 待下一個 commit 補上 |
| 15 | `persona_pack_v1/L01.md` | 存在 | 待下一個 commit 補上 |
| 16 | `persona_pack_v1/L02.md` | 存在 | 待下一個 commit 補上 |
| 17 | `persona_pack_v1/L03.md` | 存在 | 待下一個 commit 補上 |
| 18 | `persona_pack_v1/L04.md` | 存在 | 待下一個 commit 補上 |
| 19 | `persona_pack_v1/L05.md` | 存在 | 待下一個 commit 補上 |
| 20 | `persona_pack_v1/L06.md` | 存在 | 待下一個 commit 補上 |
| 21 | `persona_pack_v1/L07.md` | 存在 | 待下一個 commit 補上 |
| 22 | `persona_pack_v1/L08.md` | 存在 | 待下一個 commit 補上 |
| 23 | `persona_pack_v1/L09.md` | 存在 | 待下一個 commit 補上 |
| 24 | `persona_pack_v1/L10.md` | 存在 | 待下一個 commit 補上 |
| 25 | `persona_pack_v1/00_OVERVIEW.md` | 存在 | 待下一個 commit 補上 |
| 26 | `persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md` | 存在 | 待下一個 commit 補上 |
| 27 | `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md` | 存在 | 待下一個 commit 補上 |
| 28 | `review/CORRECTION_TASK_002_MODELING_PACK_R2.md` | 存在 | 待下一個 commit 補上 |
| 29 | `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2.md` | 存在 | 待下一個 commit 補上 |
| 30 | `review/CORRECTION_TASK_002_MODELING_PACK_R2_M01-M02.md` | 存在 | 待下一個 commit 補上 |

## 6. 未解事項

1. 仍沒有任何參考圖或成像；R2-M01 只解決文字矛盾，A 版頭像的實際效果要看圖。
2. 形象照備選、候補與分支比較的實際歸類，要製作師在報價說明；本檔不寫價格。
3. 主管 R2 報告列為各自階段處理的事項（短髮 B 的替代測試、AI 揭露方式、人設舊註記、名字查核、製作師帳號能力與許可等），本輪沒有處理。
