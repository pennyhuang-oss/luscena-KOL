# 局部補正紀錄：TASK-002 建模交付包 R2

- 日期：2026-10-07
- 執行者：Claude；Owner：Penny
- 依據：主管覆核 `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md`（主管 commit `86407a5906f2f4ef75578c1db28eaa2936a38b06`，判定 REVISE，六組局部必修 T2-F01～T2-F06）
- 分支：`claude/luscena-kol-initial-draft-et17t8`；開工時的來源 HEAD `86407a5`；遠端 main `2283244aa0c01343361d0100b185732809b617af`（本輪沒有更新 main）
- 本輪只依 T2-F01～T2-F06 做局部補正：不整批重寫十角色，不替客戶選定任何待選項目，保留已接受的整體方向與 PROPOSED／未驗收的區別。
- 本輪沒有生成、付費、訓練、開帳號、發布、聯絡製作師或重開導流；沒有修改任何主管覆核文件；沒有 force push，也沒有改寫歷史。
- 全部仍是 PROPOSED。Penny 未回答不等於同意；主管覆核也不代替 Penny 或客戶選角。
- 本檔的「腳本檢查」（§4）和「人工判讀」（§3）分開寫：腳本只證明它檢查到的字串與檔案存在，不代表語意正確。

---

## 1. 主管必修項目與處理摘要

| 主管項目 | 處理 | 補正編號 |
|---|---|---|
| T2-F01 訓練張數與官方來源適用疑義 | 十頁 I 節拿掉確定的「5–20 張」，改為「張數、工具、能不能訓練都依製作師實際帳號確認」，並引用工具研究 §2.3、§2.5。工具研究 §2.3 虛構角色列、§2.5 輸出訓練限制列、流程 2 的限制、確認問題第 12 題改為明列「來源之間有適用疑義」，不推論 Higgsfield 內部訓練自動豁免；不影響不訓練的參考圖路線與文件詢價 | R2-F01-* |
| T2-F02 prompt 替換、眼鏡矛盾、佔位符、角度、全身身分參考 | 十頁 G-3 補 T6–T8 角度對照；造型變化改成「只換指定整句」並給出保留灰 T、妝容狀態、無配件等固定條件的完整替代句；L07 眼鏡推到額頭的版本同時拿掉 `No glasses.` 與 Avoid 的 `glasses`（給完整 Avoid 句）；L09 G-3 模板補 `[HAIR]`，G-2 的「Hair pulled back」改成髮型 A、B 都成立的 `Hair kept off the forehead`，只適用長髮的檢查標明；全身照改為「臉選定後附參考圖 A 的全身照 B」，不附參考圖的版本明標「獨立體態候選，不代表同一人」；H 第 1 步註明全身照 B 等臉選定之後才做 | R2-F02-* |
| T2-F03 低／中方案張數、新增測試計費、尺度用語 | `REFERENCE_AND_ACCEPTANCE.md` 新增 §7（低 T1–T3＝3 張、中 T1–T8＝8 張；全身照 B、造型變化、L02 W1／W2／W3、L03 體態檢查、L07／L10 眼鏡、L09 遮鬍子比對、年齡檢查、候補頭像各自的歸類；L05 Q 版 7／11 與撞臉不重複計、45 組另列沿用原規則；無價格）；§4.1 第 9 項與交接 prompt 改成主管指定的「本包以尺度 1 作建議起點；實作依另行取得的選項與費用授權」；各頁「T1–T8 通過之後」改為「身分測試通過之後：低方案 T1–T3、中方案 T1–T8」，H 第 3 步寫明低／中張數與新增項目 | R2-F03-*（含部分 R2-F02-*） |
| T2-F04 交接版本包含全部必讀檔案 | 交接 prompt 指定 R2 內容 commit（SHA 由下一個 commit 補上，不追同檔自指）；必讀清單擴充為 28 個檔案，含主管覆核 R1 與本紀錄；要求製作師的 Claude 第一步記錄 `git rev-parse HEAD` 並逐一確認必讀檔案存在，缺檔就停下；START_HERE 版本說明改為以交接 prompt 為準，並加主管覆核與本紀錄的連結；README 更新目前階段與導覽 | R2-F04-* |
| T2-F05 客戶回饋殘句與已停用事件的依賴 | 總覽角色宇宙 L04 改為「朋友星座運勢」；SHARED_EVENTS 規則 2 移除 SE-12 第 1 步的例子；SE-12 總表與插曲說明不再依賴第 1 步，插曲 A 改為等團隊決定瓜雯自己的 AI 揭露方式之後才發；L10 故事 1 同步 | R2-F05-* |
| T2-F06 QA 差異、L04 左右特徵、腳本覆蓋範圍 | QA §1 改為「除該覆核檔外，檔案內容無其他差異」；§3 第 1 項更正 L04 有左右特徵（臉部：下巴痣略偏本人右側；條件配件：本人左手腕玉珠手鍊），並補人工核對；§3 第 8 項與輸出摘要的「沒有遺漏」限定為「指定字串模式未檢出」，記錄「替團隊算」的發現與修正；`check_t2.py` 加 L04 兩組字串與一小段 R2 欄位檢查，說明仍只是欄位檢查 | R2-F06-* |

---

## 2. 逐條補正（原句、新句、檔案章節、驗證方式）

> 由執行者的編輯紀錄產生：每一處修改都先確認原句在檔案中**剛好出現一次**才替換。十頁內容相同的修改合併成一條，列出全部編號與檔案。原句、新句照檔案原文（含反引號）引用。

### 2.1 T2-F01 訓練張數與官方來源的適用疑義（14 處）

#### R2-F01-Lxx（10 處：R2-F01-L01、R2-F01-L02、R2-F01-L03、R2-F01-L04、R2-F01-L05、R2-F01-L06、R2-F01-L07、R2-F01-L08、R2-F01-L09、R2-F01-L10）

- 檔案：`production/modeling_pack_v1/L01.md`、`production/modeling_pack_v1/L02.md`、`production/modeling_pack_v1/L03.md`、`production/modeling_pack_v1/L04.md`、`production/modeling_pack_v1/L05.md`、`production/modeling_pack_v1/L06.md`、`production/modeling_pack_v1/L07.md`、`production/modeling_pack_v1/L08.md`、`production/modeling_pack_v1/L09.md`、`production/modeling_pack_v1/L10.md`
- 章節：I 節第 1 點
- 主管項目：T2-F01
- 原句：

> 或在臉鎖定後用 5–20 張同一人的圖訓練專屬角色模型。

- 新句：

> 或在臉鎖定後訓練專屬角色模型（需要幾張圖、用哪個工具、帳號能不能訓練，都依製作師實際帳號確認；官方來源的張數互相衝突，輸出能不能拿來訓練也有適用疑義，見 `MODEL_AND_WORKFLOW_OPTIONS.md` §2.3、§2.5）。

- 驗證方式：grep 該頁「5–20」無結果；讀檔確認改指向工具研究 §2.3、§2.5

#### R2-F01-M1

- 檔案：`production/modeling_pack_v1/MODEL_AND_WORKFLOW_OPTIONS.md`
- 章節：§2.3 虛構角色列
- 主管項目：T2-F01
- 原句：

> | 虛構角色 | 官方部落格與 help center 的路線：先用 AI Influencer 產生虛構角色，再用它的多張肖像訓練 Soul ID | 已查證（官方網頁） |

- 新句：

> | 虛構角色 | 官方部落格與 help center 的路線：先用 AI Influencer 產生虛構角色，再用它的多張肖像訓練 Soul ID | 已查證（官方網頁）。但這和所有權頁「不得用 outputs 訓練任何 AI 模型」之間有適用疑義，見 §2.5；訓練前要先確認，不推論可以直接這樣做 |

- 驗證方式：讀檔確認加註適用疑義並指向 §2.5

#### R2-F01-M2

- 檔案：`production/modeling_pack_v1/MODEL_AND_WORKFLOW_OPTIONS.md`
- 章節：§2.5 輸出訓練限制列
- 主管項目：T2-F01
- 原句：

> | 未經書面許可，不得用 outputs 去訓練、微調任何 AI 模型 | 如果製作師打算把 Higgsfield 生成的圖拿到**其他平台**訓練角色模型，要先確認是否允許；在 Higgsfield 內訓練 Soul ID 是官方的流程 | 已查證（help center 所有權頁）；適用範圍需製作師確認 |

- 新句：

> | 未經書面許可，不得用 outputs 去訓練、微調任何 AI 模型 | **來源之間有適用疑義**：所有權頁寫的是廣泛的限制；Soul ID 官方說明與部落格又介紹「用生成的虛構角色肖像訓練 Soul ID」。兩者是否互相排除、內部訓練是否算例外，官方網頁沒有寫清楚。本文件**不推論** Higgsfield 內部訓練自動豁免。實際訓練前（不論在 Higgsfield 內或其他平台），先確認要用的流程、訓練素材的來源，以及適用的許可（例如向 Higgsfield 確認或取得書面許可），並把確認結果寫進回報。這不影響不訓練的參考圖路線（流程 1、3）與文件詢價 | 已查證（help center 所有權頁、Soul ID 頁）；適用範圍需製作師確認 |

- 驗證方式：讀檔確認：明列兩個來源與適用疑義；不再寫「在 Higgsfield 內訓練是官方流程」當成例外；不影響非訓練的參考圖路線與文件詢價

#### R2-F01-M3

- 檔案：`production/modeling_pack_v1/MODEL_AND_WORKFLOW_OPTIONS.md`
- 章節：§3 流程 2 限制列
- 主管項目：T2-F01
- 原句：

> | 限制 | 訓練張數來源衝突；需要付費方案；

- 新句：

> | 限制 | 用生成的肖像訓練是否符合輸出使用限制有適用疑義（§2.5），訓練前要先確認；訓練張數來源衝突；需要付費方案；

- 驗證方式：讀檔確認流程 2 的限制加入適用疑義

#### R2-F01-M4

- 檔案：`production/modeling_pack_v1/MODEL_AND_WORKFLOW_OPTIONS.md`
- 章節：§6 第 12 題
- 主管項目：T2-F01
- 原句：

> 12. 使用條款：是否明文禁止裸露（本案不做）；把生成圖拿到其他平台訓練是否允許。

- 新句：

> 12. 使用條款：是否明文禁止裸露（本案不做）；用生成圖訓練角色模型（包括在 Higgsfield 內用 AI Influencer 肖像訓練 Soul ID，以及拿到其他平台訓練）是否允許、需要什麼許可（§2.5 的適用疑義）。

- 驗證方式：讀檔確認確認問題改寫

### 2.2 T2-F02 prompt 替換、眼鏡矛盾、佔位符、角度與全身身分參考（68 處）

#### R2-F02-Lxx-a（10 處：R2-F02-L01-a、R2-F02-L02-a、R2-F02-L03-a、R2-F02-L04-a、R2-F02-L05-a、R2-F02-L06-a、R2-F02-L07-a、R2-F02-L08-a、R2-F02-L09-a、R2-F02-L10-a）

- 檔案：`production/modeling_pack_v1/L01.md`、`production/modeling_pack_v1/L02.md`、`production/modeling_pack_v1/L03.md`、`production/modeling_pack_v1/L04.md`、`production/modeling_pack_v1/L05.md`、`production/modeling_pack_v1/L06.md`、`production/modeling_pack_v1/L07.md`、`production/modeling_pack_v1/L08.md`、`production/modeling_pack_v1/L09.md`、`production/modeling_pack_v1/L10.md`
- 章節：G-3 [VIEW] 替換用語
- 主管項目：T2-F02
- 原句：

> （T5）。

- 新句：

> （T5）。T6–T8 的角度依 `persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md` §6.2：T6＝`front view, eye level`；T7＝同 T2；T8＝同 T3（三張都用招牌表情）。

- 驗證方式：讀檔確認 T6–T8 的角度和 PRODUCER_REFERENCE_NEEDS §6.2 一致（T6 正面、T7＝T2、T8＝T3）

#### R2-F02-Lxx-b（10 處：R2-F02-L01-b、R2-F02-L02-b、R2-F02-L03-b、R2-F02-L04-b、R2-F02-L05-b、R2-F02-L06-b、R2-F02-L07-b、R2-F02-L08-b、R2-F02-L09-b、R2-F02-L10-b）

- 檔案：`production/modeling_pack_v1/L01.md`、`production/modeling_pack_v1/L02.md`、`production/modeling_pack_v1/L03.md`、`production/modeling_pack_v1/L04.md`、`production/modeling_pack_v1/L05.md`、`production/modeling_pack_v1/L06.md`、`production/modeling_pack_v1/L07.md`、`production/modeling_pack_v1/L08.md`、`production/modeling_pack_v1/L09.md`、`production/modeling_pack_v1/L10.md`
- 章節：G-3 開頭說明
- 主管項目：T2-F02、T2-F03
- 原句：

> §6.2 的 T1–T8 清單替換。

- 新句：

> §6.2 的 T1–T8 清單替換。低方案只做 T1–T3（共 3 張），中方案做 T1–T8（共 8 張）；本頁其他檢查（全身照 B、造型變化等）是新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7。

- 驗證方式：讀檔確認寫明低方案 T1–T3、中方案 T1–T8，其他檢查指向 §7

#### R2-F02-Lxx-c（9 處：R2-F02-L01-c、R2-F02-L02-c、R2-F02-L04-c、R2-F02-L05-c、R2-F02-L06-c、R2-F02-L07-c、R2-F02-L08-c、R2-F02-L09-c、R2-F02-L10-c）

- 檔案：`production/modeling_pack_v1/L01.md`、`production/modeling_pack_v1/L02.md`、`production/modeling_pack_v1/L04.md`、`production/modeling_pack_v1/L05.md`、`production/modeling_pack_v1/L06.md`、`production/modeling_pack_v1/L07.md`、`production/modeling_pack_v1/L08.md`、`production/modeling_pack_v1/L09.md`、`production/modeling_pack_v1/L10.md`
- 章節：G-2 全身照標題
- 主管項目：T2-F02
- 原句：

>
> 全身中性照：
>

- 新句：

>
> 全身中性照 B（看體態；臉部候選選定之後才做，必須附身分參考圖 A；新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：
>
> > 如果想在挑臉之前先看體態，可以把下面 prompt 的第一句改成 `Full-body neutral body-type candidate.`、不附參考圖。那只是「獨立體態候選」，**不代表和任何臉部候選是同一人**，也不能當成身分已維持。
>

- 驗證方式：讀檔確認全身照 B 綁定參考圖 A，並另外說明獨立體態候選

#### R2-F02-Lxx-d（5 處：R2-F02-L01-d、R2-F02-L02-d、R2-F02-L04-d、R2-F02-L08-d、R2-F02-L10-d）

- 檔案：`production/modeling_pack_v1/L01.md`、`production/modeling_pack_v1/L02.md`、`production/modeling_pack_v1/L04.md`、`production/modeling_pack_v1/L08.md`、`production/modeling_pack_v1/L10.md`
- 章節：G-2 全身照 prompt 第一句
- 主管項目：T2-F02
- 原句：

> Full-body neutral casting photo of the same woman.

- 新句：

> The same woman as in the attached identity reference image A; keep her face identical. Full-body neutral casting photo B.

- 驗證方式：逐句讀：第一句改為附參考圖 A 的同一人；其餘句子不變

#### R2-F02-Lxx-e（9 處：R2-F02-L01-e、R2-F02-L02-e、R2-F02-L04-e、R2-F02-L05-e、R2-F02-L06-e、R2-F02-L07-e、R2-F02-L08-e、R2-F02-L09-e、R2-F02-L10-e）

- 檔案：`production/modeling_pack_v1/L01.md`、`production/modeling_pack_v1/L02.md`、`production/modeling_pack_v1/L04.md`、`production/modeling_pack_v1/L05.md`、`production/modeling_pack_v1/L06.md`、`production/modeling_pack_v1/L07.md`、`production/modeling_pack_v1/L08.md`、`production/modeling_pack_v1/L09.md`、`production/modeling_pack_v1/L10.md`
- 章節：H 使用順序第 1 步
- 主管項目：T2-F02
- 原句：

> ：G-2 純文字

- 新句：

> ：G-2 的臉部候選，純文字（全身照 B 等臉選定之後才做）

- 驗證方式：讀檔確認階段 1 只限臉部候選

#### R2-F02-L03-c

- 檔案：`production/modeling_pack_v1/L03.md`
- 章節：G-2 全身照標題
- 主管項目：T2-F02
- 原句：

>
> 全身中性照（看體態）：
>

- 新句：

>
> 全身中性照 B（看體態；臉部候選選定之後才做，必須附身分參考圖 A；新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：
>
> > 如果想在挑臉之前先看體態，可以把下面 prompt 的第一句改成 `Full-body neutral body-type candidate.`、不附參考圖。那只是「獨立體態候選」，**不代表和任何臉部候選是同一人**，也不能當成身分已維持。
>

- 驗證方式：讀檔確認全身照 B 綁定參考圖 A，並另外說明獨立體態候選

#### R2-F02-L03-d

- 檔案：`production/modeling_pack_v1/L03.md`
- 章節：G-2 全身照 prompt 第一句
- 主管項目：T2-F02
- 原句：

> Full-body neutral casting photo of the same woman, to show her build.

- 新句：

> The same woman as in the attached identity reference image A; keep her face identical. Full-body neutral casting photo B, to show her build.

- 驗證方式：逐句讀：第一句改為附參考圖 A 的同一人；其餘句子不變

#### R2-F02-Lxx-d（4 處：R2-F02-L05-d、R2-F02-L06-d、R2-F02-L07-d、R2-F02-L09-d）

- 檔案：`production/modeling_pack_v1/L05.md`、`production/modeling_pack_v1/L06.md`、`production/modeling_pack_v1/L07.md`、`production/modeling_pack_v1/L09.md`
- 章節：G-2 全身照 prompt 第一句
- 主管項目：T2-F02
- 原句：

> Full-body neutral casting photo of the same man.

- 新句：

> The same man as in the attached identity reference image A; keep his face identical. Full-body neutral casting photo B.

- 驗證方式：逐句讀：第一句改為附參考圖 A 的同一人；其餘句子不變

#### R2-F02-L01-f

- 檔案：`production/modeling_pack_v1/L01.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> 造型變化檢查（T1–T8 通過之後再做）：把服裝與髮型那一句換成
> `hair in a low ponytail` 或 `hair in a low bun, thin inner eyeliner extended along the outer corner, matte wine-red lipstick`，其餘不變。用來確認換髮型、換妝之後仍是同一張臉。

- 新句：

> 造型變化檢查（身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8；新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：只把模板裡的 `Plain heather-gray crew-neck T-shirt, hair tucked behind ears, very light makeup.` 整句換成下面其中一句；`[VIEW]`、`[EXPRESSION]` 用 T1 的設定，光線、背景與 Avoid 都不變。用來確認換髮型、換妝之後仍是同一張臉。
> - `Plain heather-gray crew-neck T-shirt, hair in a low ponytail, very light makeup.`
> - `Plain heather-gray crew-neck T-shirt, hair in a low bun, thin inner eyeliner extended along the outer corner, matte wine-red lipstick.`

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在

#### R2-F02-L02-f

- 檔案：`production/modeling_pack_v1/L02.md`
- 章節：G-3 造型漂移檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> **造型漂移檢查（T1–T3 通過之後必做；至少一組假髮＋舞台妝）**：把「Her own black shoulder-length hair … no colored contact lenses.」那一句換成下面其中一組，其餘不變（灰 T、灰背景、均勻光），並把 `Avoid` 加上 `anime or doll-like face`：

- 新句：

> **造型漂移檢查（T1–T3 通過之後必做；至少一組假髮＋舞台妝）**：只把模板裡的 `Her own black shoulder-length hair tucked behind ears, no wig, plain heather-gray crew-neck T-shirt, very light makeup, no colored contact lenses.` 整句換成下面其中一組；`[VIEW]`、`[EXPRESSION]` 用 T1 的設定，其餘不變（灰 T、灰背景、均勻光），並把 `Avoid` 加上 `anime or doll-like face`。W1 屬於 L02 的身分建立（`persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md` §6.4 第 3 項「L02 的身分建立含本人＋Vera 的臉」，張數請製作師在報價寫明）；W2、W3 是新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7：

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在

#### R2-F02-L02-g

- 檔案：`production/modeling_pack_v1/L02.md`
- 章節：G-3 中文解釋
- 主管項目：T2-F03
- 原句：

> 所以除了 T1–T8，一定要至少做一組假髮＋舞台妝的檢查。

- 新句：

> 所以除了身分測試（低方案 T1–T3、中方案 T1–T8），一定要至少做一組假髮＋舞台妝的檢查。

- 驗證方式：人工核對：低／中方案用語與 PRODUCER_REFERENCE_NEEDS §6.2 一致

#### R2-F02-L03-f

- 檔案：`production/modeling_pack_v1/L03.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> 造型變化檢查（T1–T8 通過之後再做）：灰 T 恤不變，只把 `hair pulled back into a low bun, very light makeup` 換成
> `hair down in natural soft waves, warm brown eyeshadow, matte brick-red lips` 或 `hair in a high ponytail, very light makeup` 或 `hair clipped up with a claw clip, very light makeup`，其餘不變。

- 新句：

> 造型變化檢查（身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8；新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：灰 T 恤不變，只把 `hair pulled back into a low bun, very light makeup` 換成
> `hair down in natural soft waves, warm brown eyeshadow, matte brick-red lips` 或 `hair in a high ponytail, very light makeup` 或 `hair clipped up with a claw clip, very light makeup`；`[VIEW]`、`[EXPRESSION]` 用 T1 的設定，其餘不變。

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在

#### R2-F02-L04-f

- 檔案：`production/modeling_pack_v1/L04.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> **造型變化檢查（T1–T8 通過之後再做）**：把服裝與髮型那一句換成下面其中一句，其餘不變。用來確認換髮型、放下瀏海、換妝之後仍是同一張臉，而且仍像 30 出頭。
> - 瀏海放下（C-L04-1 選定後；選 C 時略過）：`hair down with [BANGS]`，`[BANGS]` 用 Penny 選定的那句。選 A 齊瀏海時，成年外觀檢查要特別嚴。
> - `hair in a low ponytail`
> - `half-up hair`
> - `hair twisted up with a plain claw clip`
> - 特殊場合妝：`matte wine-red lips, light gold eyeshadow, small pearl stud earrings`

- 新句：

> **造型變化檢查**（身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8；新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：只把模板裡的 `Plain heather-gray crew-neck T-shirt, hair tucked behind ears with any bangs pinned back so the forehead and both eyebrows are visible, very light makeup, no glasses, no jewelry.` 整句換成下面其中一句；`[VIEW]`、`[EXPRESSION]` 用 T1 的設定，光線、背景與 Avoid 都不變。用來確認換髮型、放下瀏海、換妝之後仍是同一張臉，而且仍像 30 出頭。
> - 瀏海放下（C-L04-1 選定後；選 C 時略過）：`Plain heather-gray crew-neck T-shirt, hair down with [BANGS], very light makeup, no glasses, no jewelry.`，`[BANGS]` 用 Penny 選定的那句。選 A 齊瀏海時，成年外觀檢查要特別嚴。
> - `Plain heather-gray crew-neck T-shirt, hair in a low ponytail with any bangs pinned back, very light makeup, no glasses, no jewelry.`
> - `Plain heather-gray crew-neck T-shirt, half-up hair with any bangs pinned back, very light makeup, no glasses, no jewelry.`
> - `Plain heather-gray crew-neck T-shirt, hair twisted up with a plain claw clip, any bangs pinned back, very light makeup, no glasses, no jewelry.`
> - 特殊場合妝：`Plain heather-gray crew-neck T-shirt, hair tucked behind ears with any bangs pinned back so the forehead and both eyebrows are visible, matte wine-red lips, light gold eyeshadow, small pearl stud earrings, no glasses.`（這一句有耳環，所以拿掉 `no jewelry`；模板的 Avoid 沒有 jewelry，不必改）

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在

#### R2-F02-L05-f

- 檔案：`production/modeling_pack_v1/L05.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> **造型變化檢查（T1–T8 通過之後再做）**：把服裝、髮型或表情那一句換成下面其中一句，其餘不變。
> - 笑容檢查（頭像 #1 的表情）：`squinting wide grin showing the upper teeth, monolid eyes narrowed into two lines, double chin slightly more visible`。確認笑起來沒有冒出雙眼皮摺痕。
> - `freshly buzzed very short hair`
> - `hair flattened by a scooter helmet`
> - `messy bedhead hair sticking up`
> - 婚禮：`hair styled upward with wax, stubble trimmed shorter but not shaved off`

- 新句：

> **造型變化檢查**（身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8；新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：`[VIEW]` 用 T1 的 `front view, eye level`，只換下面指定的欄位，其餘（灰 T、無妝、光線、背景、Avoid）都不變。
> - 笑容檢查（頭像 #1 的表情）：`[EXPRESSION]` 換成 `squinting wide grin showing the upper teeth, monolid eyes narrowed into two lines, double chin slightly more visible`，固定條件那一句不動。確認笑起來沒有冒出雙眼皮摺痕。
> - 以下四項：`[EXPRESSION]` 用 T1 的中性表情，只把模板裡的 `Plain heather-gray crew-neck T-shirt, top hair pushed off the forehead, no makeup, visible pores and faint dark circles.` 整句換成其中一句：
>   - `Plain heather-gray crew-neck T-shirt, freshly buzzed very short hair, no makeup, visible pores and faint dark circles.`
>   - `Plain heather-gray crew-neck T-shirt, hair flattened by a scooter helmet, no makeup, visible pores and faint dark circles.`
>   - `Plain heather-gray crew-neck T-shirt, messy bedhead hair sticking up, no makeup, visible pores and faint dark circles.`
>   - 婚禮：`Plain heather-gray crew-neck T-shirt, hair styled upward with wax, stubble trimmed shorter but not shaved off, no makeup, visible pores and faint dark circles.`

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在

#### R2-F02-L06-f

- 檔案：`production/modeling_pack_v1/L06.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> 造型變化檢查（T1–T8 通過之後再做）：把服裝與髮型那一句換成下面其中一句，其餘不變。用來確認換髮型、戴帽、換衣之後仍是同一張臉。
> - `hair falling loosely over the forehead after a shower, faded old T-shirt`
> - `neat side-parted hair slicked down with pomade, light-blue dress shirt`
> - `plain baseball cap without any logo, hair flattened under it`
> - 刺青左右檢查（鏡位改成半身，雙前臂入鏡）：`half-body framing, dark navy short-sleeve work shirt without logos, sleeves cuffed up, both forearms visible, the gear tattoo on the outer side of his own right forearm`。

- 新句：

> 造型變化檢查（身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8；新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：只把模板裡的 `Plain heather-gray crew-neck T-shirt, hair combed back off the forehead, bare face, freshly shaven.` 整句換成下面其中一句；`[VIEW]`、`[EXPRESSION]` 用 T1 的設定，光線、背景與 Avoid 都不變。用來確認換髮型、戴帽、換衣之後仍是同一張臉。
> - `Faded old T-shirt, hair falling loosely over the forehead after a shower, bare face, freshly shaven.`
> - `Light-blue dress shirt, neat side-parted hair slicked down with pomade, bare face, freshly shaven.`
> - `Plain heather-gray crew-neck T-shirt, plain baseball cap without any logo, hair flattened under it, bare face, freshly shaven.`
> - 刺青左右檢查（鏡位改成半身，雙前臂入鏡）：`Half-body framing. Dark navy short-sleeve work shirt without logos, sleeves cuffed up, both forearms visible, the gear tattoo on the outer side of his own right forearm, hair combed back off the forehead, bare face, freshly shaven.`。

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在

#### R2-F02-L07-f

- 檔案：`production/modeling_pack_v1/L07.md`
- 章節：G-3 戴眼鏡的身分檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> **戴眼鏡的身分檢查**（不戴眼鏡的 T1–T8 通過之後再做）：

- 新句：

> **戴眼鏡的身分檢查**（不戴眼鏡的身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8）：

- 驗證方式：人工核對：低／中方案用語一致

#### R2-F02-L07-g

- 檔案：`production/modeling_pack_v1/L07.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> 造型變化檢查：把服裝與髮型那一句換成下面其中一句，其餘不變。
> - `black thick-rimmed square-frame glasses pushed up onto his forehead`
> - `wind-blown curly hair, one side flattened and the other side sticking up`
> - `freshly cut shorter hair with smaller curls, sides not faded`
> - `plain knit beanie, a few curls showing at the edge`（用來確認沒有捲髮這個線索時，仍認得出是他）

- 新句：

> 造型變化檢查（身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8；新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：`[VIEW]`、`[EXPRESSION]` 用 T1 的設定，光線、背景不變。
> - 眼鏡推到額頭：把模板裡的 `No glasses. Plain heather-gray crew-neck T-shirt, curls pushed back off the forehead, bare face.` 這兩句換成 `Plain heather-gray crew-neck T-shirt, curls pushed back off the forehead, black thick-rimmed square-frame glasses pushed up onto his forehead, bare face.`，**同時把 Avoid 整句換成** `Avoid: a different person, younger or student look, wider or rounder face, deep-set eyes, beard, beauty filter, text, watermark.`（也就是拿掉 `No glasses.` 和 Avoid 裡的 `glasses`，避免和額頭上的眼鏡互相矛盾）。
> - 其他三項：保留 `No glasses.` 和原本的 Avoid，只把 `Plain heather-gray crew-neck T-shirt, curls pushed back off the forehead, bare face.` 整句換成其中一句：
>   - `Plain heather-gray crew-neck T-shirt, wind-blown curly hair, one side flattened and the other side sticking up, bare face.`
>   - `Plain heather-gray crew-neck T-shirt, freshly cut shorter hair with smaller curls, sides not faded, bare face.`
>   - `Plain heather-gray crew-neck T-shirt, plain knit beanie, a few curls showing at the edge, bare face.`（用來確認沒有捲髮這個線索時，仍認得出是他）

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在；眼鏡推到額頭的版本同時拿掉 `No glasses.` 與 Avoid 的 `glasses`，並給完整 Avoid 句

#### R2-F02-L08-f

- 檔案：`production/modeling_pack_v1/L08.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> 造型變化檢查（T1–T8 通過之後再做）：把服裝、髮型與妝那一句換成下面其中一句，其餘不變。用來確認換髮型、換妝之後仍是同一張臉，特別是單眼皮和雀斑還在：
> - B 表演妝：`hair pinned back with plain clips and a [TROUPE COLORS] headband, stage performance makeup with glitter eye makeup, extended lashes and bright lip color, a small original-pattern sticker on one cheek, monolid eyes kept, freckles still partly visible`
> - B 表演髮型：`hair styled with a half-bun hairpiece, light everyday makeup`
> - A 看球：`plain baseball cap with no logo, brim raised so both eyebrows and eyes stay visible, bare face with a sunscreen-only look`

- 新句：

> 造型變化檢查（身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8；新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：只把模板裡的 `Plain heather-gray crew-neck T-shirt, hair tucked behind ears, bare face with the freckles visible.` 整句換成下面其中一句；`[VIEW]`、`[EXPRESSION]` 用 T1 的設定，光線、背景與 Avoid 都不變。用來確認換髮型、換妝之後仍是同一張臉，特別是單眼皮和雀斑還在：
> - B 表演妝：`Plain heather-gray crew-neck T-shirt, hair pinned back with plain clips and a [TROUPE COLORS] headband, stage performance makeup with glitter eye makeup, extended lashes and bright lip color, a small original-pattern sticker on one cheek, monolid eyes kept, freckles still partly visible.`
> - B 表演髮型：`Plain heather-gray crew-neck T-shirt, hair styled with a half-bun hairpiece, light everyday makeup, freckles visible.`
> - A 看球：`Plain heather-gray crew-neck T-shirt, plain baseball cap with no logo, brim raised so both eyebrows and eyes stay visible, bare face with a sunscreen-only look, freckles visible.`

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在

#### R2-F02-L09-f

- 檔案：`production/modeling_pack_v1/L09.md`
- 章節：G-3 IDENTITY_CHECK 模板
- 主管項目：T2-F02
- 原句：

> [VIEW]. [EXPRESSION]. Plain heather-gray crew-neck T-shirt, hair pulled back so the forehead is visible, no ring, no hat, no glasses.

- 新句：

> [VIEW]. [EXPRESSION]. Plain heather-gray crew-neck T-shirt, [HAIR], forehead and both eyebrows visible, no ring, no hat, no glasses.

- 驗證方式：逐句人工核對：模板新增 `[HAIR]` 佔位，與 G-1 欄位一致；短髮 B 不再被要求往後綁；grep 確認 G-3 模板含 [HAIR]

#### R2-F02-L09-g

- 檔案：`production/modeling_pack_v1/L09.md`
- 章節：G-3 替換用語
- 主管項目：T2-F02
- 原句：

> - `[EXPRESSION]`：`neutral expression, mouth closed`（T1–T5）／`signature expression: focused and calm, eyes looking slightly off-camera toward a light source, mouth relaxed`（T6–T8 招牌表情，依 §6.2 的定義取自 F 表 #2）。

- 新句：

> - `[EXPRESSION]`：`neutral expression, mouth closed`（T1–T5）／`signature expression: focused and calm, eyes looking slightly off-camera toward a light source, mouth relaxed`（T6–T8 招牌表情，依 §6.2 的定義取自 F 表 #2）。
> - `[BEARD]`、`[HAIR]`：用產生參考圖 A 時 G-1 那兩個欄位的同一句（C-L09-3 **待選**；選定前照執行者建議 A，標明「待選」）。髮型 A、B 都要露出額頭與雙眉。

- 驗證方式：人工核對：[BEARD]、[HAIR] 的來源說明，待選仍標待選

#### R2-F02-L09-h

- 檔案：`production/modeling_pack_v1/L09.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> **造型變化檢查（T1–T8 通過之後再做）**：把服裝、髮型或表情那一句換成下面其中一句，其餘不變。
> - 半笑檢查（頭像 #1 的表情）：`barely-there half-smile, mouth corners almost still`
> - `shoulder-length hair down, loose`
> - `hair in a neat low ponytail, combed smoothly, beard trimmed sharper`（婚禮工作）
> - `slightly damp hair after rain, loosely half tied up`
> - 只在 Penny 要比較 C-L09-3 時才做（不代表已選）：`[BEARD]` 換成鬍子 B 那句；或 `[HAIR]` 換成髮型 B 那句。

- 新句：

> **造型變化檢查**（身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8；新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：`[VIEW]` 用 T1 的 `front view, eye level`，只換下面指定的欄位，其餘（灰 T、無戒指、無帽、無眼鏡、光線、背景、Avoid）都不變。
> - 半笑檢查（頭像 #1 的表情）：`[EXPRESSION]` 換成 `barely-there half-smile, mouth corners almost still`。
> - 以下三項只適用髮型 A（長髮）：`[EXPRESSION]` 用 T1 的中性表情，`[HAIR]` 換成其中一句。C-L09-3 選髮型 B（短髮）時略過，製作師可以提出短髮的替代檢查並回報。
>   - `shoulder-length hair down, loose`
>   - `hair in a neat low ponytail, combed smoothly, beard trimmed sharper`（婚禮工作）
>   - `slightly damp hair after rain, loosely half tied up`
> - 只在 Penny 要比較 C-L09-3 時才做（不代表已選）：`[BEARD]` 換成鬍子 B 那句；或 `[HAIR]` 換成髮型 B 那句。

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在；只適用髮型 A 的項目已標明

#### R2-F02-L09-i

- 檔案：`production/modeling_pack_v1/L09.md`
- 章節：G-2 臉部候選
- 主管項目：T2-F02
- 原句：

> Hair pulled back so the forehead and both eyebrows are fully visible. Beard neatly trimmed.

- 新句：

> Hair kept off the forehead so the forehead and both eyebrows are fully visible. Beard neatly trimmed.

- 驗證方式：逐句人工核對：髮型 A、B 都成立；不再要求短髮往後綁

#### R2-F02-L09-j

- 檔案：`production/modeling_pack_v1/L09.md`
- 章節：G-2 全身中性照 B
- 主管項目：T2-F02
- 原句：

> plain dark shoes without logos, no ring, no jewelry. Hair pulled back. Even soft studio light

- 新句：

> plain dark shoes without logos, no ring, no jewelry. Hair kept off the forehead. Even soft studio light

- 驗證方式：逐句人工核對：髮型 A、B 都成立

#### R2-F02-L10-f

- 檔案：`production/modeling_pack_v1/L10.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> 造型變化檢查（T1–T8 通過之後再做），把服裝、髮型、眼鏡與妝那一句換成下面其中一句，其餘不變：
> - **戴眼鏡的身分核對（C-L10-2 不論選哪一個都要做）**：`thin silver round metal-frame glasses with clear lenses and no strong reflections, the frame sitting below the eyebrows so the brow peaks stay visible`。

- 新句：

> 造型變化檢查（身分測試通過之後再做：低方案 T1–T3、中方案 T1–T8；新增項目，是否在基本數量內、怎麼計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）：只把模板裡的 `Plain heather-gray crew-neck T-shirt, hair behind her shoulders and ears, no glasses, very light makeup.` 整句換成下面其中一句；`[EXPRESSION]` 用 T1 的中性表情，`[VIEW]` 除了戴眼鏡那組都用 T1，光線、背景與 Avoid 都不變：
> - **戴眼鏡的身分核對（C-L10-2 不論選哪一個都要做）**：`Plain heather-gray crew-neck T-shirt, hair behind her shoulders and ears, thin silver round metal-frame glasses with clear lenses and no strong reflections, the frame sitting below the eyebrows so the brow peaks stay visible, very light makeup.`。

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在

#### R2-F02-L10-g

- 檔案：`production/modeling_pack_v1/L10.md`
- 章節：G-3 造型變化檢查
- 主管項目：T2-F02、T2-F03
- 原句：

> - 髮型：`hair in a low ponytail`、`hair twisted up with a claw clip` 或 `hair in a low bun`。
> - 特殊場合妝：`thin eyeliner following the double-eyelid line and lifting slightly at the outer corner, cool berry-toned lipstick`。

- 新句：

> - 髮型：`Plain heather-gray crew-neck T-shirt, hair in a low ponytail, no glasses, very light makeup.`、`Plain heather-gray crew-neck T-shirt, hair twisted up with a claw clip, no glasses, very light makeup.` 或 `Plain heather-gray crew-neck T-shirt, hair in a low bun, no glasses, very light makeup.`。
> - 特殊場合妝：`Plain heather-gray crew-neck T-shirt, hair behind her shoulders and ears, no glasses, thin eyeliner following the double-eyelid line and lifting slightly at the outer corner, cool berry-toned lipstick.`。

- 驗證方式：逐句人工核對：替代句保留原固定條件（灰 T、妝容狀態、無配件等），只換指定欄位；Avoid 無矛盾；grep 確認舊指令已不存在

#### R2-F02-L02-h

- 檔案：`production/modeling_pack_v1/L02.md`
- 章節：H 使用順序第 3 步
- 主管項目：T2-F02、T2-F03
- 原句：

> 全身中性照也在這一步附 A 產生（或製作師在階段 1 同時出全身候選，回報做法）。

- 新句：

> 全身中性照 B 也在這一步附 A 產生（新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）。製作師如果在階段 1 先出不附參考圖的全身圖，那只是「獨立體態候選」，不代表和臉部候選是同一人，不能直接當成 B；請回報做法。

- 驗證方式：人工核對：低 3／中 8 與 PRODUCER_REFERENCE_NEEDS §6.2 一致；新增項目指向 §7；全身照 B 附 A；不附 A 的全身候選明標為獨立體態候選

#### R2-F02-L03-h

- 檔案：`production/modeling_pack_v1/L03.md`
- 章節：H 使用順序第 3 步
- 主管項目：T2-F02、T2-F03
- 原句：

> 3. **全身中性照**：G-2 全身照，附參考圖 A 產生（或製作師在階段 1 同時出全身候選，回報做法）。Penny 選定的那張成為「全身參考圖 B」。

- 新句：

> 3. **全身中性照 B**：G-2 全身照，附參考圖 A 產生（新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）。Penny 選定的那張成為「全身參考圖 B」。製作師如果在階段 1 先出不附參考圖的全身圖，那只是「獨立體態候選」，不代表和臉部候選是同一人，不能直接當成 B；請回報做法。

- 驗證方式：人工核對：低 3／中 8 與 PRODUCER_REFERENCE_NEEDS §6.2 一致；新增項目指向 §7；全身照 B 附 A；不附 A 的全身候選明標為獨立體態候選

### 2.3 T2-F03 低／中方案張數、新增測試計費、尺度授權用語（21 處）

#### R2-F03-L03-a

- 檔案：`production/modeling_pack_v1/L03.md`
- 章節：G-3 體態一致性檢查
- 主管項目：T2-F03
- 原句：

> 低方案至少做招牌造型一組；中方案三組都做。

- 新句：

> 這組是新增項目，不在 §6.2 身分測試的 3／8 張之內，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7；執行者建議低方案至少做招牌造型一組、中方案三組都做（數量是假設，製作師可以提替代方案）。

- 驗證方式：人工核對：標為新增項目並指向 §7；數量標為假設

#### R2-F03-L07-a

- 檔案：`production/modeling_pack_v1/L07.md`
- 章節：G-3 戴眼鏡的身分檢查
- 主管項目：T2-F03
- 原句：

> 這組不在 §6.2 的 T1–T8 數量內，要做幾張請先和 Penny 確認費用。

- 新句：

> 這組不在 §6.2 低方案 T1–T3／中方案 T1–T8 的數量內，是新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7；要做幾張請先和 Penny 確認費用。

- 驗證方式：人工核對：指向 §7，保留先確認費用

#### R2-F03-L10-a

- 檔案：`production/modeling_pack_v1/L10.md`
- 章節：C 待選（C-L10-2）
- 主管項目：T2-F03
- 原句：

> 中性建角照與 T1–T8 身分測試都不戴眼鏡；通過之後，另外做一組戴眼鏡的身分核對（G-3）。

- 新句：

> 中性建角照與身分測試（低方案 T1–T3、中方案 T1–T8）都不戴眼鏡；通過之後，另外做一組戴眼鏡的身分核對（G-3；新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）。

- 驗證方式：人工核對：低／中方案用語一致、指向 §7

#### R2-F03-Lxx-h（5 處：R2-F03-L01-h、R2-F03-L04-h、R2-F03-L05-h、R2-F03-L06-h、R2-F03-L08-h）

- 檔案：`production/modeling_pack_v1/L01.md`、`production/modeling_pack_v1/L04.md`、`production/modeling_pack_v1/L05.md`、`production/modeling_pack_v1/L06.md`、`production/modeling_pack_v1/L08.md`
- 章節：H 使用順序第 3 步
- 主管項目：T2-F02、T2-F03
- 原句：

> 3. **階段 2 身分測試**：G-3，只附參考圖 A。

- 新句：

> 3. **階段 2 身分測試**：G-3，只附參考圖 A；低方案做 T1–T3（3 張），中方案做 T1–T8（8 張）。全身中性照 B（G-2，附參考圖 A）與造型變化檢查等是新增項目，在 A 選定之後做，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7。

- 驗證方式：人工核對：低 3／中 8 與 PRODUCER_REFERENCE_NEEDS §6.2 一致；新增項目指向 §7；全身照 B 附 A

#### R2-F03-L02-h

- 檔案：`production/modeling_pack_v1/L02.md`
- 章節：H 使用順序第 4 步
- 主管項目：T2-F03
- 原句：

> 4. **造型漂移檢查**：G-3 的 W1（必做），W2、W3 建議做。

- 新句：

> 4. **造型漂移檢查**：G-3 的 W1（必做；屬於 L02 身分建立「本人＋Vera 的臉」，見 `persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md` §6.4 第 3 項），W2、W3 建議做（新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）。

- 驗證方式：人工核對：W1 依 PRODUCER_REFERENCE_NEEDS §6.4 第 3 項屬身分建立；W2、W3 指向 §7

#### R2-F03-L03-h

- 檔案：`production/modeling_pack_v1/L03.md`
- 章節：H 使用順序第 4 步
- 主管項目：T2-F03
- 原句：

> 之後做造型變化檢查與體態一致性檢查（附 A＋B）。

- 新句：

> 之後做造型變化檢查與體態一致性檢查（附 A＋B；兩者都是新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7）。

- 驗證方式：人工核對：低 3／中 8 與 PRODUCER_REFERENCE_NEEDS §6.2 一致；新增項目指向 §7；全身照 B 附 A

#### R2-F03-L07-h

- 檔案：`production/modeling_pack_v1/L07.md`
- 章節：H 使用順序第 3 步
- 主管項目：T2-F02、T2-F03
- 原句：

> 3. **階段 2 身分測試**：G-3，只附參考圖 A；先做不戴眼鏡的 T1–T8，再做戴眼鏡的檢查。

- 新句：

> 3. **階段 2 身分測試**：G-3，只附參考圖 A；先做不戴眼鏡的身分測試（低方案 T1–T3 共 3 張，中方案 T1–T8 共 8 張），再做戴眼鏡的檢查。全身中性照 B（G-2，附參考圖 A）、戴眼鏡檢查與造型變化檢查是新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7。

- 驗證方式：人工核對：低 3／中 8 與 PRODUCER_REFERENCE_NEEDS §6.2 一致；新增項目指向 §7；全身照 B 附 A

#### R2-F03-L09-h

- 檔案：`production/modeling_pack_v1/L09.md`
- 章節：H 使用順序第 3 步
- 主管項目：T2-F02、T2-F03
- 原句：

> 3. **階段 2 身分測試**：G-3，只附參考圖 A；加上年齡感檢查。

- 新句：

> 3. **階段 2 身分測試**：G-3，只附參考圖 A；低方案做 T1–T3（3 張），中方案做 T1–T8（8 張），加上年齡感檢查（人工判讀，不另外生成）。全身中性照 B（G-2，附參考圖 A）與造型變化檢查是新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7。

- 驗證方式：人工核對：低 3／中 8 與 PRODUCER_REFERENCE_NEEDS §6.2 一致；新增項目指向 §7；全身照 B 附 A

#### R2-F03-L10-h

- 檔案：`production/modeling_pack_v1/L10.md`
- 章節：H 使用順序第 3 步
- 主管項目：T2-F02、T2-F03
- 原句：

> 3. **階段 2 身分測試**：G-3，只附參考圖 A；T1–T8 通過之後，再做戴眼鏡的身分核對。

- 新句：

> 3. **階段 2 身分測試**：G-3，只附參考圖 A；低方案做 T1–T3（3 張），中方案做 T1–T8（8 張），通過之後再做戴眼鏡的身分核對。全身中性照 B（G-2，附參考圖 A）、戴眼鏡核對與造型變化檢查是新增項目，計費見 `REFERENCE_AND_ACCEPTANCE.md` §7。

- 驗證方式：人工核對：低 3／中 8 與 PRODUCER_REFERENCE_NEEDS §6.2 一致；新增項目指向 §7；全身照 B 附 A

#### R2-F03-RA-1

- 檔案：`production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md`
- 章節：§3 身分測試規格
- 主管項目：T2-F03
- 原句：

> 角度與表情依 `PRODUCER_REFERENCE_NEEDS.md` §6.2 的 T1–T8 |

- 新句：

> 角度與表情依 `PRODUCER_REFERENCE_NEEDS.md` §6.2（低方案 T1–T3、中方案 T1–T8；見本檔 §7） |

- 驗證方式：人工核對：與 PRODUCER_REFERENCE_NEEDS §6.2 低／中一致

#### R2-F03-RA-2

- 檔案：`production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md`
- 章節：§4.1 第 3 項
- 主管項目：T2-F03
- 原句：

> | 3 | 角度與表情維持身分 | T1–T8 同一人；

- 新句：

> | 3 | 角度與表情維持身分 | 所做的身分測試（低方案 T1–T3、中方案 T1–T8）都是同一人；

- 驗證方式：人工核對：不再以 8 張作低方案驗收

#### R2-F03-RA-3

- 檔案：`production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md`
- 章節：§4.1 第 9 項
- 主管項目：T2-F03
- 原句：

> | 9 | 尺度與條件項 | 只做目前允許的尺度 1；沒有越過各角色 §10 的限制 |

- 新句：

> | 9 | 尺度與條件項 | 本包以尺度 1 作建議起點；實作依另行取得的選項與費用授權。沒有越過各角色 §10 的限制 |

- 驗證方式：grep 確認「目前允許的尺度」已不存在；用語與主管指定句一致

#### R2-F03-RA-4

- 檔案：`production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md`
- 章節：§7（新增）
- 主管項目：T2-F03
- 原句：

> （無；新增一節）

- 新句：

> §7 測試範圍與計費對照（全文見檔案）

- 驗證方式：人工核對：基本數量與 PRODUCER_REFERENCE_NEEDS §6.2／§6.4 一致；L05 Q 版 7／11、撞臉不重複計、45 組另列沿用；所有歸類標為假設、無價格；各建模頁引用的 §7 已存在

#### R2-F03-RA-5

- 檔案：`production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md`
- 章節：開頭狀態說明
- 主管項目：T2-F03
- 原句：

> 各角色的詳細 OK／NG 方向（文字）見 `persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md` §3；本檔補上收集、權利與驗收的做法。

- 新句：

> 各角色的詳細 OK／NG 方向（文字）見 `persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md` §3；本檔補上收集、權利與驗收的做法。低／中方案的測試範圍與新增項目計費對照見 §7（R2 新增）。

- 驗證方式：人工核對：導覽指向 §7

#### R2-F03-H-4

- 檔案：`production/modeling_pack_v1/PRODUCER_CLAUDE_HANDOFF_PROMPT.md`
- 章節：prompt【分批進行】
- 主管項目：T2-F03
- 原句：

> 之後才做身分測試（T1–T8）與形象照。

- 新句：

> 之後才做身分測試（低方案 T1–T3、中方案 T1–T8）與形象照。全身照 B、造型變化、眼鏡檢查等是新增項目，哪些在基本數量內、怎麼計費，照 REFERENCE_AND_ACCEPTANCE.md §7 報價；你可以提出替代流程或數量，用「原假設／你的建議／理由」並列。

- 驗證方式：人工核對：低 3／中 8；新增項目指向 §7

#### R2-F03-H-5

- 檔案：`production/modeling_pack_v1/PRODUCER_CLAUDE_HANDOFF_PROMPT.md`
- 章節：prompt【不可以】尺度
- 主管項目：T2-F03
- 原句：

> 不越過各角色檔 §10 的限制（L02、L03 目前只做尺度 1）。

- 新句：

> 不越過各角色檔 §10 的限制。L02、L03：本包以尺度 1 作建議起點；實作依另行取得的選項與費用授權（尺度 2、同人是條件項，只列價，不替 Penny 啟用）。

- 驗證方式：grep 確認「只做尺度 1」已不存在；用語與主管指定句一致

#### R2-F03-S-3

- 檔案：`production/modeling_pack_v1/00_START_HERE.md`
- 章節：§5 進行順序第 3 步
- 主管項目：T2-F03
- 原句：

> 3. **Penny／客戶選定**之後，才做身分測試（T1–T8）。

- 新句：

> 3. **Penny／客戶選定**之後，才做身分測試（低方案 T1–T3、中方案 T1–T8）。全身照 B、造型變化等新增檢查的計費見 `REFERENCE_AND_ACCEPTANCE.md` §7。

- 驗證方式：人工核對：低 3／中 8；指向 §7

### 2.4 T2-F04 交接版本與必讀檔案（8 處）

#### R2-F04-H-1

- 檔案：`production/modeling_pack_v1/PRODUCER_CLAUDE_HANDOFF_PROMPT.md`
- 章節：檔頭「交付版本」
- 主管項目：T2-F04
- 原句：

> > **交付版本**：分支 `claude/luscena-kol-initial-draft-et17t8`，TASK-002 R1 內容 commit `3cb0a0c175a3fccf5196ce6482476134fa3745e5`。這個 SHA 是在內容 commit 之後的下一個 commit 補上的；之後如果有修訂，以 Penny 指定的 commit 為準，並在回報中寫明你讀的是哪個 commit。

- 新句：

> > **交付版本**：分支 `claude/luscena-kol-initial-draft-et17t8`，TASK-002 R2 內容 commit `[R2_CONTENT_SHA]`。這個 commit 含下面【必讀】列出的全部檔案（含主管覆核 R1 與 R2 補正紀錄）。SHA 在內容 commit 之後的下一個 commit 補上；R1 的內容 commit `3cb0a0c` 缺少部分必讀檔案，**不要再用**。之後如果有修訂，以 Penny 指定的 commit 為準；不論讀哪個 commit，都先記錄 `git rev-parse HEAD`，並確認必讀檔案都存在。
> > 交接時，Penny 要把主管覆核 `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md` 和本包一起交給製作師（該報告的結論：可以做可行性討論與條件式詢價，測試範圍仍待對齊）。

- 驗證方式：實際確認：內容 commit 中每一個必讀檔案都存在（見補正紀錄 §4 存在性表）；SHA 由下一個 commit 補上，不追同檔自指

#### R2-F04-H-2

- 檔案：`production/modeling_pack_v1/PRODUCER_CLAUDE_HANDOFF_PROMPT.md`
- 章節：prompt【Repo 與交付版本】
- 主管項目：T2-F04
- 原句：

> - 交付版本：TASK-002 R1 內容 commit 3cb0a0c175a3fccf5196ce6482476134fa3745e5（之後如有修訂，以 Penny 指定的 commit 為準）。請用 git log 確認你讀到的 commit，並在每次回報寫明。

- 新句：

> - 交付版本：TASK-002 R2 內容 commit [R2_CONTENT_SHA]（之後如有修訂，以 Penny 指定的 commit 為準；不要用 R1 的 3cb0a0c，那個版本缺檔）。
> - 第一步：切到交付版本後執行 `git rev-parse HEAD`，把完整 SHA 寫進第一次回報；再逐一確認下面【必讀】的每個檔案都存在（例如對每個路徑執行 `test -f <路徑> && echo OK <路徑> || echo MISSING <路徑>`），把結果列表回報。有任何檔案缺少，就停下來回報 Penny，不要用其他版本的檔案補。

- 驗證方式：同上

#### R2-F04-H-3

- 檔案：`production/modeling_pack_v1/PRODUCER_CLAUDE_HANDOFF_PROMPT.md`
- 章節：prompt【必讀】
- 主管項目：T2-F04
- 原句：

> 【必讀】
> 1. production/modeling_pack_v1/00_START_HERE.md：任務目標、十角色清單、版本來源、已決定與待選事項、進行順序。
> 2. production/modeling_pack_v1/L01.md～L10.md：每個角色的外型規格、必須維持的身分特徵、撞臉配對、中性建角照、形象照、英文 prompt 與使用方式。
> 3. production/modeling_pack_v1/MODEL_AND_WORKFLOW_OPTIONS.md：可行流程與工具能力（分已查證、推論、需製作師確認）。
> 4. production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md：參考素材登記、身分測試與形象照分開、候選審查、誰可以鎖定形象、哪些工作要先授權。
> 5. production/modeling_pack_v1/CLIENT_FEEDBACK_2026-10-07.md：客戶回饋與仍未選定的選項。
> 6. 角色的完整設定：persona_pack_v1/L01.md～L10.md；撞臉配對與身分測試標準：persona_pack_v1/00_OVERVIEW.md、persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md（§2、§4、§6）。

- 新句：

> 【必讀】（共 28 個檔案；每個都要確認存在）
> 1. production/modeling_pack_v1/00_START_HERE.md：任務目標、十角色清單、版本來源、已決定與待選事項、進行順序。
> 2. production/modeling_pack_v1/L01.md、L02.md、L03.md、L04.md、L05.md、L06.md、L07.md、L08.md、L09.md、L10.md：每個角色的外型規格、必須維持的身分特徵、撞臉配對、中性建角照、形象照、英文 prompt 與使用方式。
> 3. production/modeling_pack_v1/MODEL_AND_WORKFLOW_OPTIONS.md：可行流程與工具能力（分已查證、推論、需製作師確認）。
> 4. production/modeling_pack_v1/REFERENCE_AND_ACCEPTANCE.md：參考素材登記、身分測試與形象照分開、候選審查、誰可以鎖定形象、哪些工作要先授權；§7 是低／中方案的測試範圍與新增項目計費對照。
> 5. production/modeling_pack_v1/CLIENT_FEEDBACK_2026-10-07.md：客戶回饋與仍未選定的選項。
> 6. 角色的完整設定：persona_pack_v1/L01.md、L02.md、L03.md、L04.md、L05.md、L06.md、L07.md、L08.md、L09.md、L10.md；撞臉配對與身分測試標準：persona_pack_v1/00_OVERVIEW.md、persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md（§2、§4、§6）。
> 7. review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md：主管覆核 R1。結論是可以做可行性討論與條件式詢價，但測試範圍仍待對齊；這份報告要和本包一起看。
> 8. review/CORRECTION_TASK_002_MODELING_PACK_R2.md：R2 依主管覆核做的局部補正（原句、新句、驗證方式）。
> 如果 Penny 指定的版本裡有更新的 TASK-002 主管覆核（review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R2.md 之類），也一起讀，並以較新的為準。

- 驗證方式：實際確認：清單上每個路徑在內容 commit 都存在（git cat-file -e）

#### R2-F04-H-6

- 檔案：`production/modeling_pack_v1/PRODUCER_CLAUDE_HANDOFF_PROMPT.md`
- 章節：prompt【把成果寫回 repo】REPORT 第 1 項
- 主管項目：T2-F04
- 原句：

>   1. 讀的是哪個 commit；

- 新句：

>   1. 讀的是哪個 commit（`git rev-parse HEAD` 的完整 SHA），以及必讀檔案的存在性檢查結果；

- 驗證方式：人工核對：要求寫 SHA 與必讀檔案存在性

#### R2-F04-S-1

- 檔案：`production/modeling_pack_v1/00_START_HERE.md`
- 章節：§3 版本來源
- 主管項目：T2-F04
- 原句：

> - 本包的版本：以 GitHub 分支 `claude/luscena-kol-initial-draft-et17t8` 上、加入本包的 commit 為準（實際 SHA 見 `review/REVIEW_REQUEST_TASK_002_MODELING_PACK_R1.md`）。

- 新句：

> - 本包的版本：以 GitHub 分支 `claude/luscena-kol-initial-draft-et17t8` 上、`PRODUCER_CLAUDE_HANDOFF_PROMPT.md` 的「交付版本」（或 Penny 交接時另外指定的 commit）為準。R1 的內容 commit `3cb0a0c` 缺少部分必讀檔案，不要再用。讀之前先記錄 `git rev-parse HEAD`，並確認交接 prompt【必讀】列出的檔案都存在；缺檔就停下回報 Penny。

- 驗證方式：實際確認：指向的交接 prompt 與必讀清單在內容 commit 都存在

#### R2-F04-S-2

- 檔案：`production/modeling_pack_v1/00_START_HERE.md`
- 章節：§2 其他文件表
- 主管項目：T2-F04
- 原句：

> | [persona_pack_v1/00_OVERVIEW.md](../../persona_pack_v1/00_OVERVIEW.md) | 十角色總覽、外型差異地圖、撞臉配對優先順序 |

- 新句：

> | [persona_pack_v1/00_OVERVIEW.md](../../persona_pack_v1/00_OVERVIEW.md) | 十角色總覽、外型差異地圖、撞臉配對優先順序 |
> | [review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md](../../review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md) | 主管覆核 R1：可以做可行性討論與條件式詢價，但測試範圍仍待對齊；交接時和本包一起看 |
> | [review/CORRECTION_TASK_002_MODELING_PACK_R2.md](../../review/CORRECTION_TASK_002_MODELING_PACK_R2.md) | R2 局部補正紀錄：依主管覆核改了哪些句子、怎麼驗證 |

- 驗證方式：實際確認：兩個連結的檔案在內容 commit 都存在

#### R2-F04-RM-1

- 檔案：`README.md`
- 章節：開頭「目前階段」
- 主管項目：T2-F04
- 原句：

> - **目前階段**：TASK-002 建模交付包整理中。

- 新句：

> - **目前階段**：TASK-002 建模交付包 R2 局部補正完成，等主管覆核（R1 主管覆核：`review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md`；R2 補正紀錄：`review/CORRECTION_TASK_002_MODELING_PACK_R2.md`）。

- 驗證方式：人工核對：不把交付當成選角核准；指向主管覆核 R1 與 R2 補正紀錄

#### R2-F04-RM-2

- 檔案：`README.md`
- 章節：導覽表 TASK-002 覆核列
- 主管項目：T2-F04
- 原句：

> | ★ | `review/REVIEW_REQUEST_TASK_002_MODELING_PACK_R1.md`、`review/INTERNAL_QA_TASK_002_MODELING_PACK_R1.md`、`review/CHANGELOG_TASK_002_CLIENT_FEEDBACK.md` | TASK-002 覆核請求、內部核查、客戶回饋相關修改紀錄 |

- 新句：

> | ★ | `review/REVIEW_REQUEST_TASK_002_MODELING_PACK_R1.md`、`review/INTERNAL_QA_TASK_002_MODELING_PACK_R1.md`、`review/CHANGELOG_TASK_002_CLIENT_FEEDBACK.md` | TASK-002 覆核請求、內部核查、客戶回饋相關修改紀錄 |
> | ★ | `review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md`、`review/CORRECTION_TASK_002_MODELING_PACK_R2.md` | TASK-002 主管覆核 R1（REVISE，六組局部必修）與 R2 局部補正紀錄 |

- 驗證方式：實際確認：列出的檔案在內容 commit 都存在

### 2.5 T2-F05 客戶回饋殘句與已停用事件的依賴（5 處）

#### R2-F05-OV-1

- 檔案：`persona_pack_v1/00_OVERVIEW.md`
- 章節：角色宇宙 L04 列
- 主管項目：T2-F05
- 原句：

> - **L04 可妮**每個月替團隊算一次星座運勢，常點名「天蠍的予安」（SE-10）。

- 新句：

> - **L04 可妮**每個月發一次「朋友星座運勢」，替她認識的朋友（會互動的角色）算運勢，常點名「天蠍的予安」（SE-10）〔2026-10-07 依客戶回饋改字：公開文案不用「團隊」二字，不對外宣稱共同團隊〕。

- 驗證方式：grep 確認「替團隊算」不再出現於現行敘述；人工核對與 SE-10「朋友星座運勢」一致、不對外稱共同團隊

#### R2-F05-SE-1

- 檔案：`persona_pack_v1/SHARED_EVENTS.md`
- 章節：開頭規則 2 的例子
- 主管項目：T2-F05
- 原句：

> 例如 L07 的「W1（SE-12 第 1 步）」、L10 的「W1（＝SE-02 第 1 步）」。

- 新句：

> 例如 L10 的「W1（＝SE-02 第 1 步）」。〔2026-10-07 依客戶回饋移除原本的 L07「W1（SE-12 第 1 步）」例子：那一步已不採用〕

- 驗證方式：人工核對：剩下的例子 L10 W1＝SE-02 第 1 步，總表寫明「第 1 步沒有前置條件」，是有效例子；grep 確認規則 2 不再引用 SE-12 第 1 步

#### R2-F05-SE-2

- 檔案：`persona_pack_v1/SHARED_EVENTS.md`
- 章節：總表 SE-12 前置條件
- 主管項目：T2-F05
- 原句：

> | 無；插曲 A、B 要在第 1 步之後 |

- 新句：

> | 第 2 步：無。插曲 A：等團隊決定瓜雯自己的 AI 揭露方式之後才發（不依賴已停用的第 1 步；插曲 B 不採用）〔2026-10-07 依客戶回饋修改〕 |

- 驗證方式：人工核對：插曲 A 不再依賴已停用的第 1 步；改依瓜雯自身 AI 揭露方式的實際決定；不替團隊做決定

#### R2-F05-SE-3

- 檔案：`persona_pack_v1/SHARED_EVENTS.md`
- 章節：SE-12 插曲說明
- 主管項目：T2-F05
- 原句：

> 插曲（不排固定順序，只要在主線第 1 步之後）：
> - 插曲 A：瓜雯發「AI 圖的破綻」，說自己就是 AI 生成的，所以很懂（主文：L10；回應：L07；L10 故事 1）。

- 新句：

> 插曲（不排固定順序）〔2026-10-07 依客戶回饋修改：原本寫「只要在主線第 1 步之後」，第 1 步已不採用，插曲 A 不再依賴它〕：
> - 插曲 A：瓜雯發「AI 圖的破綻」，說自己就是 AI 生成的，所以很懂（主文：L10；回應：L07；L10 故事 1）。前置條件：團隊已決定瓜雯自己的 AI 揭露方式，而且那個方式讓她可以用第一人稱說自己是 AI 生成；只講她自己，不代表其他帳號，也不暗示同一團隊。決定之前不發。

- 驗證方式：同上

#### R2-F05-L10-1

- 檔案：`persona_pack_v1/L10.md`
- 章節：§7 故事 1 發展
- 主管項目：T2-F05
- 原句：

> SE-12 插曲 A（在程翊主線第 1 步之後）：

- 新句：

> SE-12 插曲 A（等團隊決定瓜雯自己的 AI 揭露方式之後才發，不依賴程翊主線第 1 步；見 `SHARED_EVENTS.md`）〔2026-10-07 依客戶回饋修改〕：

- 驗證方式：人工核對：與 SHARED_EVENTS SE-12 插曲 A 的新前置條件一致

### 2.6 T2-F06 內部核查的更正與腳本覆蓋範圍（6 處）

#### R2-F06-QA-1

- 檔案：`review/INTERNAL_QA_TASK_002_MODELING_PACK_R1.md`
- 章節：§1 版本確認「兩者差異」
- 主管項目：T2-F06
- 原句：

> main 比來源多 1 個合併 commit（`2283244`），檔案內容無差異 |

- 新句：

> main 比來源多 1 個合併 commit（`2283244`），~~檔案內容無差異~~ 除該覆核檔外，檔案內容無其他差異（R2 更正，T2-F06：原句和同一欄「多一份主管合併覆核檔」矛盾；`git diff --stat 2283244 8d16cc1` 只列出這一個檔案） |

- 驗證方式：`git diff --stat 2283244 8d16cc1` 只列出 review/REVIEW_RESPONSE_TASK_001_MERGE_MAIN.md 一個檔案（99 行新增）

#### R2-F06-QA-2

- 檔案：`review/INTERNAL_QA_TASK_002_MODELING_PACK_R1.md`
- 章節：§3 第 1 項（豁免範圍與限制）
- 主管項目：T2-F06
- 原句：

> L04、L07、L08 沒有分左右的特徵，不檢查 |

- 新句：

> ~~L04、L07、L08 沒有分左右的特徵，不檢查~~ L07、L08 沒有分左右的特徵，不檢查（R2 更正，T2-F06）。**L04 有左右特徵，原句錯誤**：臉部身分特徵是下巴小痣（下唇正下方、略偏她本人的右側，人設寫明是「位置提案」）；條件配件是她本人左手腕的淺綠玉珠手鍊（公開造型都戴，身分測試不戴，不是臉部身分依據）。R2 人工核對：人設 L04 §1 第 2 點與 §4「辨識特徵」列、建模頁 B 節、C 節固定配件、G-1／G-3 的 `slightly toward her own right side`、G-4 #2 的 `on her own left wrist` 都寫成她本人的左右，一致。R1 腳本沒有檢查這兩項，不代表它們不存在；R2 版 `check_t2.py` 加上這兩組字串，仍只是欄位檢查，不是整份 prompt 的語意驗證 |

- 驗證方式：人工核對 persona_pack_v1/L04.md §1 第 2 點、§4 辨識特徵列與建模頁 B、C、G-1、G-3、G-4；check_t2 R2 版新增 L04 兩組字串

#### R2-F06-QA-3

- 檔案：`review/INTERNAL_QA_TASK_002_MODELING_PACK_R1.md`
- 章節：§3 第 8 項（結果）
- 主管項目：T2-F06
- 原句：

> 標記 13 處；開頭註記 10／10；沒有遺漏的行。

- 新句：

> 標記 13 處；開頭註記 10／10；~~沒有遺漏的行~~ 指定的四個字串模式未檢出遺漏（R2 更正，T2-F06：腳本只搜尋「同一個團隊」「同團隊」「我們這群」「規格書」，沒有涵蓋其他寫法。主管覆核找到 `00_OVERVIEW.md` 角色宇宙仍寫「L04 可妮每個月替團隊算一次星座運勢」，R2 已改為「朋友星座運勢」；SHARED_EVENTS 規則 2 與 SE-12 插曲仍依賴已停用的第 1 步，R2 一併修正）。

- 驗證方式：人工重讀 persona_pack_v1/00_OVERVIEW.md 角色宇宙；修正見補正紀錄 R2-F05-OV-1

#### R2-F06-QA-4

- 檔案：`review/INTERNAL_QA_TASK_002_MODELING_PACK_R1.md`
- 章節：§3 下方 check_t2 輸出摘要
- 主管項目：T2-F06
- 原句：

> 「依客戶回饋不採用」13 處；開頭註記 10／10；遺漏的同團隊行為 none。

- 新句：

> 「依客戶回饋不採用」13 處；開頭註記 10／10；遺漏的同團隊行為 none。（R2 更正，T2-F06：none 只代表四個指定字串模式未檢出，不代表沒有遺漏；見第 8 項）

- 驗證方式：同上

#### R2-F06-QA-5

- 檔案：`review/INTERNAL_QA_TASK_002_MODELING_PACK_R1.md`
- 章節：檔頭
- 主管項目：T2-F06
- 原句：

>   - 每一項寫出檢查的欄位與豁免範圍。
>

- 新句：

>   - 每一項寫出檢查的欄位與豁免範圍。
> - R2 更正（2026-10-07，依主管覆核 T2-F06）：§1、§3 第 1／8 項與 §3 下方的輸出摘要有更正，用刪除線保留原句。R2 的核查與全部補正見 `review/CORRECTION_TASK_002_MODELING_PACK_R2.md`。
>

- 驗證方式：人工核對：補正紀錄檔存在

#### R2-F06-QC-1

- 檔案：`review/qa/check_t2.py`
- 章節：CANON L04；檔尾新增 [R2] 區塊
- 主管項目：T2-F06
- 原句：

> 'L04': ('林可妮', 31, 158, None),（L04 不檢查左右特徵）

- 新句：

> 'L04' 改成兩組字串：（'略偏她本人的右側'，'slightly toward her own right side'）、（'左手腕'，'on her own left wrist'）；檔尾新增 [R2] 區塊：R1 殘留字串、T6–T8 對照、全身照 B 綁參考圖 A、§7 指向、L07 眼鏡推到額頭有 Avoid 替換句、L09 G-3 模板有 [HAIR]、角色宇宙無「替團隊算」、SE-12 總表不依賴第 1 步、交接必讀 28 個檔案存在、七份主管覆核檔 blob

- 驗證方式：執行 `python3 review/qa/check_t2.py .`，輸出見本檔 §4；說明字串寫明只是欄位檢查

---

## 3. 改過的英文 prompt：逐句人工核對

> 這一節是**人工判讀**，不是腳本結果。核對方法：把每一句放回所在模板，讀完整的組裝結果，確認（a）原本的固定條件（灰 T、妝容狀態、無配件、露額頭等）沒有被刪掉；（b）和同模板的 Avoid 或其他句子沒有矛盾；（c）性別代名詞、左右（角色本人的左右）與人設一致；（d）沒有新增人設沒有的五官。結果只代表文字層面；**成像是否一致要看圖**，本輪沒有任何圖。

| # | 位置 | 改後的英文句子 | 人工判讀 |
|---|---|---|---|
| 1 | 十頁 G-3 `[VIEW]`（T6–T8 對照） | `front view, eye level`（T6）；T7＝T2 的句子；T8＝T3 的句子 | 與 `PRODUCER_REFERENCE_NEEDS.md` §6.2 一致：T6 正面、T7 本人左 3/4、T8 本人右 3/4，三張都用招牌表情。沿用 R1 已修正的 3/4 寫法，沒有新增矛盾 |
| 2 | 十頁 G-2 全身照第一句 | `The same woman as in the attached identity reference image A; keep her face identical. Full-body neutral casting photo B.`（L05、L06、L07、L09 是 man／his；L03 後面接 `, to show her build.`） | 十頁的代名詞和角色性別一致（L01–L04、L08、L10 女；L05–L07、L09 男）。後面接 `[BASE_IDENTITY]`，沒有和臉部描述衝突。A、B 是給人看的編號，模型不一定理解，製作師可以刪掉，不影響內容。不附參考圖的替代句 `Full-body neutral body-type candidate.` 只是體態候選，頁面已寫明不代表同一人 |
| 3 | L01 G-3 造型 | `Plain heather-gray crew-neck T-shirt, hair in a low ponytail, very light makeup.` | 只換髮型；灰 T、淡妝保留。左眉尾小痣不受影響 |
| 4 | L01 G-3 造型 | `Plain heather-gray crew-neck T-shirt, hair in a low bun, thin inner eyeliner extended along the outer corner, matte wine-red lipstick.` | 換髮型與妝；灰 T 保留。Avoid 沒有和妝容衝突的字 |
| 5 | L02 G-3 W 系列的被替換句 | `Her own black shoulder-length hair tucked behind ears, no wig, plain heather-gray crew-neck T-shirt, very light makeup, no colored contact lenses.` | 和模板原文逐字相同（R1 用「…」省略，R2 改成全文）。W1／W2／W3 的替代句本身沒改，原本就保留灰 T |
| 6 | L04 G-3 被替換句 | `Plain heather-gray crew-neck T-shirt, hair tucked behind ears with any bangs pinned back so the forehead and both eyebrows are visible, very light makeup, no glasses, no jewelry.` | 和模板原文逐字相同 |
| 7 | L04 G-3 造型 | `Plain heather-gray crew-neck T-shirt, hair down with [BANGS], very light makeup, no glasses, no jewelry.` | 瀏海放下會遮額頭，這是這一項要測的；`[BANGS]` 用 Penny 選定那句，C-L04-1 未選前不做（頁面已寫）。下巴痣仍可見 |
| 8 | L04 G-3 造型 | `Plain heather-gray crew-neck T-shirt, hair in a low ponytail with any bangs pinned back, very light makeup, no glasses, no jewelry.` | 只換髮型；瀏海仍夾起，避免同時改兩個變因 |
| 9 | L04 G-3 造型 | `Plain heather-gray crew-neck T-shirt, half-up hair with any bangs pinned back, very light makeup, no glasses, no jewelry.` | 同上 |
| 10 | L04 G-3 造型 | `Plain heather-gray crew-neck T-shirt, hair twisted up with a plain claw clip, any bangs pinned back, very light makeup, no glasses, no jewelry.` | 同上 |
| 11 | L04 G-3 造型 | `Plain heather-gray crew-neck T-shirt, hair tucked behind ears with any bangs pinned back so the forehead and both eyebrows are visible, matte wine-red lips, light gold eyeshadow, small pearl stud earrings, no glasses.` | 換妝並加珍珠耳針，所以刻意拿掉 `no jewelry`；模板的 Avoid 沒有 jewelry，不需要改 Avoid。頁面已註明 |
| 12 | L05 G-3 被替換句 | `Plain heather-gray crew-neck T-shirt, top hair pushed off the forehead, no makeup, visible pores and faint dark circles.` | 和模板原文逐字相同 |
| 13 | L05 G-3 造型 | `… freshly buzzed very short hair, no makeup, visible pores and faint dark circles.`（開頭同為 `Plain heather-gray crew-neck T-shirt,`） | 只換髮型；無妝、毛孔、黑眼圈這些成年線索保留 |
| 14 | L05 G-3 造型 | `… hair flattened by a scooter helmet, no makeup, visible pores and faint dark circles.` | 同上 |
| 15 | L05 G-3 造型 | `… messy bedhead hair sticking up, no makeup, visible pores and faint dark circles.` | 同上 |
| 16 | L05 G-3 造型 | `… hair styled upward with wax, stubble trimmed shorter but not shaved off, no makeup, visible pores and faint dark circles.` | 鬍渣變短但不刮掉，和 Avoid 的 `clean-shaven face` 一致 |
| 17 | L05 G-3 笑容檢查 | `[EXPRESSION]` 換成原有的咧嘴笑句子，固定條件那一句不動 | 句子本身沒改；R1 的指示會把表情放進服裝句，R2 改成換 `[EXPRESSION]`，固定條件全部保留 |
| 18 | L06 G-3 被替換句 | `Plain heather-gray crew-neck T-shirt, hair combed back off the forehead, bare face, freshly shaven.` | 和模板原文逐字相同 |
| 19 | L06 G-3 造型 | `Faded old T-shirt, hair falling loosely over the forehead after a shower, bare face, freshly shaven.` | 這一項本來就要換舊 T 恤；素顏、刮乾淨保留，和 Avoid 的 `beard or stubble` 一致 |
| 20 | L06 G-3 造型 | `Light-blue dress shirt, neat side-parted hair slicked down with pomade, bare face, freshly shaven.` | 這一項本來就要換襯衫；其他保留 |
| 21 | L06 G-3 造型 | `Plain heather-gray crew-neck T-shirt, plain baseball cap without any logo, hair flattened under it, bare face, freshly shaven.` | 只加帽子；帽簷可能遮眉，原 R1 也沒寫露眉，沿用 |
| 22 | L06 G-3 刺青檢查 | `Half-body framing. Dark navy short-sleeve work shirt without logos, sleeves cuffed up, both forearms visible, the gear tattoo on the outer side of his own right forearm, hair combed back off the forehead, bare face, freshly shaven.` | 刺青在他本人的右前臂外側，與人設一致；R1 版漏掉的髮型、素顏、刮乾淨補回 |
| 23 | L07 G-3 眼鏡推到額頭 | `Plain heather-gray crew-neck T-shirt, curls pushed back off the forehead, black thick-rimmed square-frame glasses pushed up onto his forehead, bare face.` | 取代 `No glasses.` 和固定條件兩句，所以組裝後不再有 `No glasses.` |
| 24 | L07 G-3 眼鏡推到額頭的 Avoid | `Avoid: a different person, younger or student look, wider or rounder face, deep-set eyes, beard, beauty filter, text, watermark.` | 和原 Avoid 逐項比對，只拿掉 `glasses`，其他不變。眼鏡句和 Avoid 不再互相矛盾 |
| 25 | L07 G-3 造型（其他三項） | `Plain heather-gray crew-neck T-shirt, wind-blown curly hair, one side flattened and the other side sticking up, bare face.`／`… freshly cut shorter hair with smaller curls, sides not faded, bare face.`／`… plain knit beanie, a few curls showing at the edge, bare face.` | 保留 `No glasses.` 與原 Avoid；只換髮型或加毛帽；灰 T、素顏保留 |
| 26 | L08 G-3 被替換句 | `Plain heather-gray crew-neck T-shirt, hair tucked behind ears, bare face with the freckles visible.` | 和模板原文逐字相同 |
| 27 | L08 G-3 造型 | `Plain heather-gray crew-neck T-shirt, hair pinned back with plain clips and a [TROUPE COLORS] headband, stage performance makeup with glitter eye makeup, extended lashes and bright lip color, a small original-pattern sticker on one cheek, monolid eyes kept, freckles still partly visible.` | 補回灰 T；`[TROUPE COLORS]` 是 C 節已說明的佔位；`monolid eyes kept`、`freckles still partly visible` 和 Avoid 的 `added double eyelids`、`freckles removed` 一致 |
| 28 | L08 G-3 造型 | `Plain heather-gray crew-neck T-shirt, hair styled with a half-bun hairpiece, light everyday makeup, freckles visible.` | 補回灰 T 與雀斑 |
| 29 | L08 G-3 造型 | `Plain heather-gray crew-neck T-shirt, plain baseball cap with no logo, brim raised so both eyebrows and eyes stay visible, bare face with a sunscreen-only look, freckles visible.` | 補回灰 T 與雀斑；A、B 只是看效果，C-L08-1 仍待選 |
| 30 | L09 G-3 模板固定條件 | `Plain heather-gray crew-neck T-shirt, [HAIR], forehead and both eyebrows visible, no ring, no hat, no glasses.` | 模板現在有 `[HAIR]`，和 G-1、替換指令一致。髮型 A（綁小髻、露額頭）組裝後「forehead」重複一次，不矛盾；髮型 B（短髮）組裝後不再要求往後綁 |
| 31 | L09 G-2 臉部候選 | `Hair kept off the forehead so the forehead and both eyebrows are fully visible. Beard neatly trimmed.` | 原句 `Hair pulled back` 在短髮 B 下不成立；新句 A、B 都成立 |
| 32 | L09 G-2 全身照 B | `… no ring, no jewelry. Hair kept off the forehead. Even soft studio light …` | 同上 |
| 33 | L09 G-3 造型 | `[HAIR]` 換成 `shoulder-length hair down, loose`／`hair in a neat low ponytail, combed smoothly, beard trimmed sharper`／`slightly damp hair after rain, loosely half tied up` | 句子沿用 R1；R2 改成只換 `[HAIR]`，灰 T、無戒指、無帽、無眼鏡保留。三項只適用長髮 A，頁面已標明；`beard trimmed sharper` 和 Avoid 的 `longer or bushier beard` 一致 |
| 34 | L10 G-3 被替換句 | `Plain heather-gray crew-neck T-shirt, hair behind her shoulders and ears, no glasses, very light makeup.` | 和模板原文逐字相同 |
| 35 | L10 G-3 戴眼鏡核對 | `Plain heather-gray crew-neck T-shirt, hair behind her shoulders and ears, thin silver round metal-frame glasses with clear lenses and no strong reflections, the frame sitting below the eyebrows so the brow peaks stay visible, very light makeup.` | 拿掉 `no glasses`、加眼鏡；模板 Avoid 沒有 glasses，不矛盾；頭髮仍在耳後，右耳耳骨環可見 |
| 36 | L10 G-3 造型 | `Plain heather-gray crew-neck T-shirt, hair in a low ponytail, no glasses, very light makeup.`／`… hair twisted up with a claw clip, …`／`… hair in a low bun, …` | 只換髮型；灰 T、無眼鏡、淡妝保留 |
| 37 | L10 G-3 特殊妝 | `Plain heather-gray crew-neck T-shirt, hair behind her shoulders and ears, no glasses, thin eyeliner following the double-eyelid line and lifting slightly at the outer corner, cool berry-toned lipstick.` | 只換妝；其他保留 |

沒有逐句改寫的部分：各頁 G-1、G-2 臉部候選（L09 除外）、G-4 形象照、L02 W1–W3 的替代句、L03 造型與體態檢查的句子、L05 Q 版。這些在 R1 主管覆核已逐句讀過，R2 沒有改動。

---

## 4. 腳本與字串檢查（和 §3 的人工判讀分開）

> 腳本只證明它檢查到的字串與檔案存在；退出碼永遠是 0，要看輸出。字串存在不等於語意正確，也檢不出矛盾的替換指令以外的語意問題（例如 R1 的「替團隊算」就不在原本的字串模式內）。

### 4.1 `python3 review/qa/check_t2.py .`（R2 版，內容 commit 前在工作目錄執行）

```text
L01 text_blocks=6 OK
L02 text_blocks=9 OK
L03 text_blocks=9 OK
L04 text_blocks=6 OK
L05 text_blocks=9 OK
L06 text_blocks=6 OK
L07 text_blocks=6 OK
L08 text_blocks=7 OK
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
[R2] handoff must-read files: 28 listed in script; missing on disk: none; basename not in handoff: none
[R2] blob REVIEW_RESPONSE_TASK_001_R1.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_R2_PERSONA.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_R3.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_R3_F01-F06.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_R3_F01_FINAL.md: same
[R2] blob REVIEW_RESPONSE_TASK_001_MERGE_MAIN.md: same
[R2] blob REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md: same
```

R2 版新增的欄位（見 R2-F06-QC-1）：L04 兩組左右字串；R1 殘留字串（`5–20`／`5-20` 只查建模頁，工具研究頁要列出來源衝突所以豁免；`T1–T8 通過之後再做`；四種「把服裝…那一句換成」的 R1 寫法；`目前允許的尺度`；`只做尺度 1`）；十頁都有 T6–T8 對照、全身照 B 綁參考圖 A、指向 §7；L07 眼鏡推到額頭那一行有 Avoid 替換句；L09 G-3 模板有 `[HAIR]`；`REFERENCE_AND_ACCEPTANCE.md` 有 §7；總覽沒有「替團隊算」；SE-12 總表列不再要求「第 1 步之後」；交接必讀 28 個檔案都存在、檔名都出現在交接 prompt；七份主管覆核檔的 blob。

**反向測試**：把同一支腳本對 R1 版本（`git archive 86407a5` 解開到暫存目錄）執行，R2 區塊會列出 R1 的問題，例如十頁的 `5–20`、`T1–T8 通過之後再做`、R1 的「把服裝…那一句換成」寫法、缺 T6–T8 對照、全身照沒綁參考圖 A、交接 prompt 的「只做尺度 1」、驗收文件的「目前允許的尺度」、L07 眼鏡推到額頭沒有 Avoid 替換、L09 G-3 沒有 `[HAIR]`、沒有 §7、總覽的「替團隊算」、SE-12 總表依賴第 1 步，以及 R1 交接 prompt 缺少主管覆核與補正紀錄。這只證明這些字串檢查抓得到 R1 的寫法，不代表能抓到其他語意問題。

### 4.2 其他字串檢查（grep，內容 commit 前在工作目錄執行）

```text
$ grep -c "5–20" production/modeling_pack_v1/L??.md
production/modeling_pack_v1/L01.md:0 production/modeling_pack_v1/L02.md:0 production/modeling_pack_v1/L03.md:0 production/modeling_pack_v1/L04.md:0 production/modeling_pack_v1/L05.md:0 production/modeling_pack_v1/L06.md:0 production/modeling_pack_v1/L07.md:0 production/modeling_pack_v1/L08.md:0 production/modeling_pack_v1/L09.md:0 production/modeling_pack_v1/L10.md:0 
$ grep -rn "T1–T8 通過之後\|目前允許的尺度\|只做尺度 1\|目前只做尺度" production/modeling_pack_v1
(無輸出＝未檢出)
$ grep -rn "替團隊" persona_pack_v1
(無輸出＝未檢出)
$ grep -n "第 1 步之後" persona_pack_v1/SHARED_EVENTS.md（每行只印前 60 字）
31:| SE-13 | 詐騙新聞 × 手機設定 | L10 瓜雯（第 1 步）、L07 程翊（第 2 步） | 對方在
120:插曲（不排固定順序）〔2026-10-07 依客戶回饋修改：原本寫「只要在主線第 1 步之後」，第 1 步已不採
126:2. 程翊只接手「手機要怎麼設」（主文：L07；在第 1 步之後；每一項設定都由真人在實機上照做過，還沒照做完就
$ grep -rn "那一句換成\|那兩句換成" production/modeling_pack_v1（每行只印前 70 字）
production/modeling_pack_v1/L08.md:122:選 A 時，把體態那一句換成：
production/modeling_pack_v1/L08.md:175:A 版頭像：把服裝那一句換成 `Plain crew-neck
$ grep -c "\[HAIR\]" production/modeling_pack_v1/L09.md
6
$ grep -rln "\[R2_CONTENT_SHA\]" --include=*.md .
./review/CORRECTION_TASK_002_MODELING_PACK_R2.md
./production/modeling_pack_v1/PRODUCER_CLAUDE_HANDOFF_PROMPT.md
```

判讀：建模頁沒有「5–20」；R1 的尺度用語與「T1–T8 通過之後」寫法未檢出；人設包沒有「替團隊」；SHARED_EVENTS 剩下的「第 1 步之後」是 SE-13（第 31、126 行，與 SE-12 無關）和 SE-12 插曲說明裡保留原寫法的修改註記（第 120 行）；剩下兩處「那一句換成」都在 L08 的 G-1（選 A 時的體態句）與 G-4（A 版頭像），不在 G-3（G-4 那一處見 §7 第 9 點）；`[R2_CONTENT_SHA]` 佔位只在交接 prompt 與本檔，下一個 commit 補上。

---

## 5. 交接必讀檔案的存在性

交接 prompt【必讀】列出的 28 個檔案，逐一確認存在。

| # | 必讀檔案 | 工作目錄（提交前，`test -f`） | R2 內容 commit（`git cat-file -e`） |
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

R1 的內容 commit `3cb0a0c` 對照：`review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md` 與本檔在那個版本都不存在（主管覆核是 `86407a5` 才加入），所以交接 prompt 不再指定 `3cb0a0c`。

---

## 6. 本輪沒做的事

- 沒有生成、付費、訓練、開帳號、發布、聯絡製作師，也沒有重開導流。本輪沒有呼叫任何 Higgsfield MCP 工具。
- 沒有整批重寫十角色；人設檔只改主管點名的三處（`00_OVERVIEW.md` 角色宇宙 L04、`SHARED_EVENTS.md` 規則 2 與 SE-12、`L10.md` 故事 1 的 SE-12 插曲 A）。
- 沒有替客戶選定任何待選項目（L02／L03 尺度與 IP、L04 瀏海、L05 形式、L07／L10 眼鏡頻率、L08 定位、L09 鬍子與髮型等）；也沒有決定 AI 揭露方式。
- 沒有修改任何 `review/REVIEW_RESPONSE_*` 主管覆核文件；沒有更新 main；沒有 force push 或改寫歷史。
- 沒有新增 R2 的覆核請求檔；覆核 prompt 附在執行者給 Penny 的回報裡。

## 7. 未解事項（交主管判斷）

1. 仍沒有任何參考圖、候選圖或撞臉實測；R2 的修正都只在文字層面，成像一致要看圖。
2. 製作師帳號的實際工具、Soul ID 訓練張數（官方來源 20–80 與 5–20 衝突）、輸出能不能拿來訓練（所有權頁與 Soul ID 說明之間的適用疑義）、扣點與價格，都要製作師確認；本包不推論。
3. `REFERENCE_AND_ACCEPTANCE.md` §7 的「在不在基本數量內」是執行者的假設，製作師可以提出替代流程或數量；L02 W1 算在 L02 身分建立內，是依 `PRODUCER_REFERENCE_NEEDS.md` §6.4 第 3 項的解讀，請主管確認。
4. SE-12 插曲 A 現在等「團隊決定瓜雯自己的 AI 揭露方式」才發；AI 揭露方式本身仍未決定。
5. L09 選髮型 B（短髮）時，造型變化檢查的三項長髮檢查不適用，R2 沒有另寫短髮版，只請製作師提出替代並回報。
6. 交接 prompt 在內容 commit 裡的交付版本是 `[R2_CONTENT_SHA]` 佔位，SHA 由下一個 commit 補上；製作師應以 Penny 貼出的、已填 SHA 的交接 prompt 為準。
7. R1 內部核查 §5 列的人設來源問題仍未處理（各角色 §3／§10 的「發布時標示 AI」原句、撞臉配對稱呼不一致、L08 缺臉長寬比與髮色等）。另外，人設檔仍有「全團隊唯一…」這類內部定位句，以及 AI 問答裡指「單一帳號背後的製作者」的「團隊」用語；主管未列為必修，本輪沒改，請主管判斷是否需要處理。
8. `check_t2.py` 仍是欄位檢查，退出碼永遠是 0；本輪沒有建立新的測試系統。
9. 核對時另外發現（不在 T2-F02 點名的 G-2／G-3／H 範圍，本輪**沒有改**）：L08 G-4「A 版頭像：把服裝那一句換成 `… bare face with a sunscreen-only look.`」照做之後，同一個 prompt 下一句仍是 `Light everyday makeup, freckles on her nose and cheeks visible.`，「素顏」和「淡妝」矛盾。這是和 T2-F02 同類的替換問題，請主管判斷是否列入下一輪；L08 定位 C-L08-1 仍待選，A 版頭像只在選 A 時才用。
