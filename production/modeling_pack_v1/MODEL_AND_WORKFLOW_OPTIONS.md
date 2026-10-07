# 建模選項與工作流程（Claude＋Higgsfield MCP）

> 狀態：PROPOSED。這份文件整理製作師用 Claude＋Higgsfield MCP 建立十個角色時，**目前查得到**的選項。不要求製作師一定採用某個模型或流程；工具、模型、生成、訓練與費用由製作師決定，不需要 Penny 批准（2026-10-07 責任分工調整，見 `review/RESPONSIBILITY_CHANGE_TASK_002_2026-10-07.md`）。
> 查核日：2026-10-07。功能、模型、扣點與方案都可能變動；使用前請在自己的帳號再確認一次。
> 本文件**不填任何價格**：官方定價頁讀不到，其他頁面出現的數字不是定價頁內容，不能當預算依據。

## 0. 證據狀態與查核方法

| 標記 | 意思 |
|---|---|
| **已查證（官方網頁）** | 在 higgsfield.ai 的 help center、部落格、落地頁、Academy、官方 GitHub 讀到。引文是用網頁讀取工具摘錄的，不是人工逐字抄錄；正式引用前請點連結核對 |
| **已觀察（本 session 的 MCP）** | 執行者這個 session 連接的 Higgsfield MCP 工具說明與模型目錄。這是 Penny 這邊的連線，**不等於製作師帳號**；也沒有實際呼叫生成或訓練，所以實際行為未驗證 |
| **推論** | 執行者根據上面兩種證據推出的判斷，沒有官方原文直接支持 |
| **需製作師確認** | 查不到、來源互相衝突、或會因帳號方案而不同 |

**查核方法**
- 網頁：只用網頁搜尋與讀取；沒有登入、購買或生成。
- MCP：讀取工具說明（schema），並只做唯讀查詢：`get_workflow_instructions`（character-sheet）、`models_explore`（get：soul_2、soul_cast、soul_cinematic、nano_banana_pro、gpt_image_2、seedream_v4_5）。**沒有**呼叫任何生成、報價、上傳、訓練、建立角色元素或查詢帳戶餘額的工具。

---

## 1. 三件事要分開：不要都叫「建模」

| | 生成候選人物 | 參考圖維持身分 | 專屬角色訓練／角色模型 |
|---|---|---|---|
| 是什麼 | 從文字或選單產生新的、虛構的人物 | 生成時附上同一個人的參考圖，讓新圖維持那張臉；**不訓練** | 用同一個人的多張照片訓練出可重複呼叫的角色身分 |
| Higgsfield 對應功能 | AI Influencer（選單式角色產生器）、Soul Cast、文字生圖模型 | Elements（存起來的參考，生成時呼叫）、多參考圖模型（例如 Nano Banana 系列）、Soul 2.0／Soul Cinema 的單張參考 | Soul ID（Soul Character） |
| 輸入 | 文字描述或選單設定；AI Influencer 可選擇附一張照片 | 已選定的參考圖 | 同一人的多張照片（張數見 §2 的衝突） |
| 輸出 | 候選人物圖（AI Influencer 每次一張近照＋一張全身照） | 新的圖，盡量維持參考圖的臉 | 具名的角色，之後在 Soul 系列模型呼叫 |
| 本案用途 | 階段 1 臉部候選 | 階段 2 身分測試、形象照、換裝 | 選定之後，需要大量、長期維持同一張臉時 |
| 證據 | 已查證（官方網頁）；已觀察（MCP） | 已查證（官方網頁）；已觀察（MCP） | 已查證（官方網頁）；已觀察（MCP 工具說明） |

官方對一致性的說法是「看得出是同一個人」，不是完全相同：Soul ID 頁寫 "Expect 'clearly the same person' rather than a pixel-identical face"；部落格寫 "Consistency is high, not absolute"。官方網頁**沒有**任何以數字表示的相似度保證。〔已查證（官方網頁）〕

## 2. 查到的能力與證據

### 2.1 生成候選人物

| 項目 | 內容 | 證據 |
|---|---|---|
| AI Influencer | 選單式角色產生器（"works like a game character creator"）；可設定性別、族裔基底、膚色、眼色、年齡等；可選擇上傳一張照片，"keeps the facial features from your uploaded image"；每次產出近照與全身照 | 已查證（官方網頁）。族裔有 6 個選項，但選項名稱沒有列出，**有沒有可對應台灣／東亞的選項需製作師確認**；年齡選項是 Adult／Mature／Senior；性別選項數在部落格與落地頁寫法不一致 |
| AI Influencer（MCP） | MCP 有 `ai_influencer_prepare`（產生設計與報價，不建立工作、不扣點）、`ai_influencer_generate`／`build_ai_influencer`（產生 1–4 張角色表，會扣點）、`ai_influencer_get_options`（列出可選特徵）。說明寫明 "Does not train a Soul"；可附最多一張身分參考與三張風格參考 | 已觀察（MCP 工具說明）；沒有實際呼叫 |
| Soul Cast | Cinema Studio 裡的角色產生器；可設定性別、族裔、年齡、外觀、服裝等 | 已查證（官方網頁）。MCP 目錄有 `soul_cast`（"Consistent cinematic character identity"，只有 16:9，參數 budget 10–500）〔已觀察（MCP）〕。budget 參數的意義需製作師確認 |
| 文字生圖模型 | 官方列出 Soul 系列、Nano Banana 系列、GPT Image、Seedream、Recraft、FLUX 等 | 已查證（官方網頁）。本 session 的 MCP 目錄可見 `soul_2`（Soul 2.0）、`soul_cinematic`（Soul Cinema）、`nano_banana_pro`（Nano Banana Pro）、`gpt_image_2`（GPT Image 2）、`seedream_v4_5`（Seedream 4.5）〔已觀察（MCP）〕 |
| character-sheet 工作流程 | MCP 內附的工作流程說明（v1.0）：用固定的欄位順序組 prompt；寫實預設是「不修圖」的質感；明列「只做原創角色」「成年角色要有成熟骨架，避免娃娃臉」「已建立的細節沿用不變」；版面有全身＋近照、四視圖、表情表、換裝表；只有在明確要求時才生成 | 已觀察（MCP 唯讀查詢）。本包的 prompt 寫法有參考它的欄位順序與「避免娃娃臉」規則 |

### 2.2 參考圖維持身分

| 項目 | 內容 | 證據 |
|---|---|---|
| Elements | 官方定義："a saved, reusable reference that you pull into any generation with @"。MCP 說明：可從**一張**清楚的參考圖建立角色元素；生成時把元素放進 prompt；支援的圖片模型包括 Nano Banana Pro、Nano Banana 2、GPT Image 2、Seedream 4.5、Seedream 5.0 lite、Cinema Studio Image 2.5；元素狀態可能是處理中、IP 檢查中、失敗或 NSFW，只有完成的能用 | 已查證（官方網頁）；已觀察（MCP 工具說明）。建立元素時最好用幾張圖，官方網頁沒寫，需製作師確認 |
| 多參考圖模型 | Nano Banana 一次最多 8 張參考，Pro／2／2 Lite 最多 14 張；官方建議「每次生成都附同一組角色肖像」 | 已查證（官方網頁）。MCP 目錄的 `nano_banana_pro`、`seedream_v4_5` 參考圖角色為 image_references，張數上限沒有寫；`gpt_image_2` 角色為 image〔已觀察（MCP）〕 |
| Soul 2.0／Soul Cinema 的單張參考 | 官方網頁：附參考圖後，網頁介面的 prompt 欄位會停用（"the prompt field becomes unavailable"）。MCP 目錄：`soul_2`、`soul_cinematic` 可附 1 張參考圖 | 已查證（官方網頁）；已觀察（MCP）。**透過 MCP 附參考圖時 prompt 是否仍有作用，需製作師確認**。因此用 Soul 系列「參考圖＋文字換裝」不一定可行 |
| 換裝 | 官方有 AI Clothes Changer（宣稱保留臉、髮型、膚色；服裝類別含 cosplay；"Outfits are changed, never removed"）、Nano Banana 的編輯指令 | 已查證（官方網頁，屬行銷頁）。實際效果需製作師測試 |

### 2.3 專屬角色訓練：Soul ID

| 項目 | 內容 | 證據 |
|---|---|---|
| 是什麼 | Soul 系列模型的角色一致性功能；訓練後的角色可以在 Soul 系列使用，並會自動出現在 Elements | 已查證（官方網頁） |
| 訓練照片張數 | **來源衝突**：help center 寫 20 張以上、最多 80 張；官方 GitHub 的 skill 寫 5–20 張；本 session 的 MCP 工具說明寫 5–20 張、約 10 分鐘 | 已查證（官方網頁）＋已觀察（MCP），但互相衝突，**以製作師帳號的介面為準** |
| 照片要求 | 清楚、光線好、不同角度與表情；不戴墨鏡、沒有重陰影、臉不被裁切；至少一張全身照 | 已查證（官方網頁） |
| 虛構角色 | 官方部落格與 help center 的路線：先用 AI Influencer 產生虛構角色，再用它的多張肖像訓練 Soul ID | 已查證（官方網頁）。但這和所有權頁「不得用 outputs 訓練任何 AI 模型」之間有適用疑義，見 §2.5；訓練前要先確認，不推論可以直接這樣做 |
| 使用限制 | MCP 工具說明：訓練好的 Soul 只能用在 Soul 2.0 與 Soul Cinema；每次生成只能用一個 Soul；多人同框要改用 Elements | 已觀察（MCP 工具說明） |
| 能不能透過 MCP 訓練 | 官方網頁只寫 MCP 可以「使用」Soul characters 與 Elements，沒寫能不能訓練；本 session 的 MCP 工具說明有 `show_characters` 的 train 動作 | 已觀察（MCP 工具說明）；**沒有實際呼叫，需製作師確認** |
| 方案與數量 | 官方 GitHub skill 寫訓練需要付費方案；每個帳號能建幾個 Soul ID 沒有官方說明（本案需要 10 個角色） | 已查證（官方網頁）；數量上限需製作師確認 |
| 真人照片 | 只能上傳自己或已取得同意者的照片 | 已查證（官方網頁）。本案是原創角色，不用真人照片訓練 |

### 2.4 MCP 連接與扣點

| 項目 | 內容 | 證據 |
|---|---|---|
| 連接方式 | MCP 網址 `https://mcp.higgsfield.ai/mcp`；在 Claude 以自訂連接器加入，登入 Higgsfield 授權；不需要 API key | 已查證（官方網頁） |
| 方案 | 需要有效的付費訂閱 | 已查證（官方網頁） |
| 扣點 | "Every generation through a connected agent deducts credits, regardless of your plan."；Unlimited 與免費生成不適用於 MCP | 已查證（官方網頁）。本 session 的 MCP 說明另有「免費試用的 unlim」選項，和官方網頁寫法不同，**以製作師帳號實際情況為準** |
| 查價 | MCP 的 `generate_image` 有 `get_cost` 參數，可以只查扣點不生成；`ai_influencer_prepare` 會報價但不建立工作 | 已觀察（MCP 工具說明）；沒有實際呼叫 |

### 2.5 條款與內容規則（影響本案的部分）

| 規則 | 對本案的影響 | 證據 |
|---|---|---|
| 使用者須年滿 18 歲；禁止以不當方式描繪未成年人（真實或合成） | 所有角色都是成年人，外觀也要明顯成年 | 已查證（使用條款） |
| 使用他人肖像須取得同意；禁止非自願私密影像 | 不用真人照片當臉部參考或訓練素材 | 已查證（使用條款、Soul ID 頁） |
| NSFW 過濾：泳裝或暴露服裝、健身內容是常見的誤判類型；判定本身無法申訴，確認誤判時退回點數 | L02、L03、L08 的服裝可能被誤判；要預留重試與改寫的空間，回報時記錄被擋的次數 | 已查證（help center） |
| 可辨識的版權角色、品牌名、授權 IP 可能被擋 | L02 同人選項（C-L02-2 B）就算選了，也可能生成不了；版權責任在使用者 | 已查證（help center） |
| 不得宣稱 Output 是人類創作；法律要求時須揭露是 AI 生成 | AI 揭露方式雖然交由團隊評估，仍要遵守工具條款與法律；和「被問時不否認」一致 | 已查證（使用條款 5.2、5.5；摘錄，建議人工通讀） |
| 未經書面許可，不得用 outputs 去訓練、微調任何 AI 模型 | **來源之間有適用疑義**：所有權頁寫的是廣泛的限制；Soul ID 官方說明與部落格又介紹「用生成的虛構角色肖像訓練 Soul ID」。兩者是否互相排除、內部訓練是否算例外，官方網頁沒有寫清楚。本文件**不推論** Higgsfield 內部訓練自動豁免。實際訓練前（不論在 Higgsfield 內或其他平台），先確認要用的流程、訓練素材的來源，以及適用的許可（例如向 Higgsfield 確認或取得書面許可），並把確認結果寫進回報。這不影響不訓練的參考圖路線（流程 1、3）與文件詢價 | 已查證（help center 所有權頁、Soul ID 頁）；適用範圍需製作師確認 |
| 條款是否明文禁止裸露 | 摘錄結果沒有出現相關字眼 | **需人工通讀條款確認**。本案本來就不做裸露 |

## 3. 可行的三條流程

### 流程 1：文字候選 → 選定 → 單張參考（Elements）維持身分

| | 說明 |
|---|---|
| 用途 | 最快、最少前置的做法；適合先看方向 |
| 步驟 | ① 用各建模頁的 NEUTRAL_CASTING 以文字生成臉部候選 ② 製作師選定（或依其流程交客戶選定） ③ 用選定的那張建立角色元素 ④ 用支援元素的模型做身分測試與形象照 |
| 輸入 | 文字 prompt；選定的一張中性候選照 |
| 輸出 | 每角色一個角色元素、身分測試圖、形象照 |
| 優點 | 不需要訓練；一張圖就能開始；同一張圖可放進多個模型；多人同框可用 |
| 限制 | 只靠一張參考，角度、表情變化大時容易漂移；建立元素可能被 IP 或 NSFW 檢查擋下 |
| 適合 | 造型變化少的角色：L01、L04、L06、L07、L09、L10 |
| 證據 | 已查證（官方網頁）＋已觀察（MCP）；效果需製作師測試 |

### 流程 2：AI Influencer 角色表 → 選定 → 多張肖像 → Soul ID 訓練

| | 說明 |
|---|---|
| 用途 | 官方針對虛構角色的長期一致性路線 |
| 步驟 | ① 用 AI Influencer 依建模頁 B 節設定特徵，產生候選角色表 ② 製作師選定（或依其流程交客戶選定） ③ 用同一個角色產生多張不同角度、表情、含全身的肖像（張數依帳號介面要求） ④ 訓練 Soul ID ⑤ 用 Soul 2.0 或 Soul Cinema 生成身分測試與形象照 |
| 輸入 | 選單設定（可附一張方向參考）；訓練用的多張肖像 |
| 輸出 | 每角色一個 Soul 角色 |
| 優點 | 官方說換裝、換場景、換角度仍能維持同一張臉；適合長期大量出圖 |
| 限制 | 用生成的肖像訓練是否符合輸出使用限制有適用疑義（§2.5），訓練前要先確認；訓練張數來源衝突；需要付費方案；每帳號角色數上限未知；Soul ID 只能用在 Soul 系列；每次生成只能用一個 Soul，多人同框要改用元素；AI Influencer 的族裔選項是否對得上台灣角色未知；訓練素材本身要先通過人工審查，不能把漂移的圖放進去 |
| 適合 | 需要大量換裝、長期維持同一張臉的角色：**L02 凜**（多套幻想角色服）、L03 以晨、L08 沛沛 |
| 證據 | 已查證（官方網頁）＋已觀察（MCP 工具說明）；透過 MCP 能否訓練需製作師確認 |

### 流程 3：角色表（多視圖）→ 存成元素 → 多參考圖模型

| | 說明 |
|---|---|
| 用途 | 在不訓練的情況下，提供比單張更完整的參考 |
| 步驟 | ① 先用流程 1 或 2 選定臉 ② 以選定的臉為參考，做一張多視圖角色表（例如全身正面、背面、側面近照） ③ 人工檢查角色表是否仍是同一張臉 ④ 存成元素，或把多張同一人的圖一起當參考 ⑤ 用多參考圖模型生成身分測試與形象照；換裝用編輯指令 |
| 輸入 | 選定的臉；角色表 |
| 輸出 | 角色表與元素；身分測試圖與形象照 |
| 優點 | 官方 Academy 示範的做法；角色表本身就是很好的驗收材料；多參考圖模型可放進多張同一人的圖 |
| 限制 | 角色表本身是生成出來的，也可能已經漂移；多張參考裡只要有一張不像，就會把結果拉偏；換裝效果與體態保持沒有官方量化說法 |
| 適合 | 體態與比例很重要的角色：L03、L06、L08；以及需要正背側面的 L02 角色服 |
| 證據 | 已查證（官方 Academy、help center）＋已觀察（MCP 的 character-sheet 工作流程）；效果需製作師測試 |

## 4. 依任務比較

| 任務 | 流程 1（單張元素） | 流程 2（Soul ID） | 流程 3（角色表＋多參考） | 證據狀態 |
|---|---|---|---|---|
| 候選生成 | 文字生圖 | AI Influencer 選單 | 同流程 1 或 2 | 已查證 |
| 身分保持 | 中：只有一張參考 | 官方說「看得出是同一人」 | 中到高：參考較完整，但受角色表品質影響 | 推論；需製作師並排測試 |
| L02 Cos 換裝（同一張臉換假髮、舞台妝、角色服） | 容易漂移 | 官方路線；仍可能因風格跳太遠而漂移 | 可行；要逐套檢查 | 推論；需製作師測試 |
| 體態保持（L03、L06、L08） | 弱 | 訓練照要含全身照 | 角色表含全身；官方未量化 | 推論 |
| L05 Q 版 | 不適用；Q 版要另做插畫設計稿 | Soul 跨到 Q 版是否還認得出，官方沒寫 | 可先做寫實角色表，再另外畫 Q 版設計稿 | 未查證；需製作師測試 |
| 多人同框（角色客串） | 可以（多個元素） | 一次只能一個 Soul | 可以 | 已觀察（MCP 工具說明） |

**角色對應只是執行者的推論**，製作師可以全部用同一條流程，或混用；請回報選擇的理由。

## 5. 費用

- 官方定價頁是動態載入，讀不到方案價格與每月點數。**本文件不填任何價格。**
- 部落格與落地頁出現的數字不是定價頁內容，不列入，也不能當預算依據。
- 已查證的規則：每次生成的扣點會顯示在 Generate 按鈕上；透過 MCP 的生成一律扣點。
- 查價方法（不扣點）：在網頁介面看 Generate 按鈕上的點數；MCP 的 `generate_image` 用 `get_cost`、AI Influencer 用 `prepare` 報價。〔已觀察（MCP 工具說明）〕
- 估價請照 `persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md` §6 的數量假設與計費邊界，用實際查到的點數換算；查不到就寫查不到。

## 6. 需要製作師在自己的帳號確認

1. 方案價格、每月點數、各功能實際扣點。
2. AI Influencer 的族裔選項實際名稱，有沒有可以對應台灣／東亞的選項；性別、渲染風格的選項。
3. Soul ID 實際需要幾張訓練照（20–80 或 5–20）、訓練時間。
4. 每個帳號能建幾個 Soul ID（本案需要 10 個）；會不會過期、能不能刪除或重訓。
5. 用 AI Influencer 生成的虛構角色肖像訓練 Soul ID，在你的帳號是否可行。
6. Claude 的 Higgsfield 連接器在你的帳號實際開放哪些工具：能不能建立 AI Influencer、能不能訓練 Soul ID、能不能建立元素，以及每次扣點。
7. 透過 MCP 用 Soul 2.0 附參考圖時，prompt 是否仍有作用。
8. 多參考圖模型的參考張數上限；建立元素時用幾張圖最好。
9. 泳裝、緊身服、舞台裝（L02、L03、L08）在你選的模型上會不會被 NSFW 過濾；被擋的比例。
10. L02 同人造型（如果客戶選了）會不會被 IP 過濾擋下。
11. L05 Q 版：用寫實角色的參考做 Q 版時，是否還認得出同一人。
12. 使用條款：是否明文禁止裸露（本案不做）；用生成圖訓練角色模型（包括在 Higgsfield 內用 AI Influencer 肖像訓練 Soul ID，以及拿到其他平台訓練）是否允許、需要什麼許可（§2.5 的適用疑義）。
13. 本 session 的 MCP 說明提到的免費試用額度，與官方「MCP 一律扣點」的寫法是否衝突。

## 7. 主要來源（查核日 2026-10-07）

| 來源 | 網址 | 狀態 |
|---|---|---|
| Help center：Soul ID | https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-create-and-use-a-soul-id-character | 已查證 |
| Help center：Soul | https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-soul-to-generate-images | 已查證 |
| Help center：Soul Cinema | https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-soul-cinema | 已查證 |
| Help center：Nano Banana | https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-nano-banana | 已查證 |
| Help center：Seedance（Elements） | https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-seedance | 已查證 |
| Help center：該用哪個模型 | https://higgsfield.ai/creator-hub/help-center/ai-models/which-ai-model-should-i-use | 已查證 |
| Help center：AI Influencer | https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-ai-influencer | 已查證 |
| Help center：Cinema Studio | https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-cinema-studio | 已查證 |
| Help center：什麼是 Higgsfield MCP | https://higgsfield.ai/creator-hub/help-center/integrations/what-is-higgsfield-mcp | 已查證 |
| Help center：連接 Claude 等代理 | https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent | 已查證 |
| Help center：CLI | https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-access-higgsfield-via-cli | 已查證 |
| Help center：哪些會扣點 | https://higgsfield.ai/creator-hub/help-center/credits/what-uses-my-credits | 已查證 |
| Help center：NSFW 判定 | https://higgsfield.ai/creator-hub/help-center/troubleshooting/content-flagged-as-nsfw | 已查證 |
| Help center：版權與 IP | https://higgsfield.ai/creator-hub/help-center/troubleshooting/my-generation-blocked-for-copyright-or-ip | 已查證 |
| Help center：生成物所有權 | https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially | 已查證 |
| 部落格：新版 AI Influencer（2026-10-03） | https://higgsfield.ai/blog/new-ai-influencer | 已查證 |
| 部落格：Soul ID（2026-06-15） | https://higgsfield.ai/blog/Soul-ID-AI-Character-Consistency | 已查證 |
| 部落格：Soul ID 一致性（2026-06-29） | https://higgsfield.ai/blog/sould-id-best-character-consistency | 已查證 |
| 部落格：建立一致的 AI influencer（2026-06-13） | https://higgsfield.ai/blog/how-to-create-ai-influencer | 已查證 |
| 落地頁：AI Influencer、Soul Cast、AI Clothes Changer、AI Anime Generator、MCP | https://higgsfield.ai/ai-influencer、https://higgsfield.ai/soul-cast-intro、https://higgsfield.ai/ai-clothes-changer、https://higgsfield.ai/ai-anime-generator、https://higgsfield.ai/mcp | 已查證（行銷頁） |
| Academy：建立角色、場景與道具素材 | https://higgsfield.ai/academy/courses/blockbuster-4k/stage-2-building-character-location-and-prop-assets | 已查證 |
| 使用條款 | https://higgsfield.ai/terms-of-use-agreement | 已查證（摘錄，建議人工通讀） |
| 官方 GitHub skill（Soul ID） | https://github.com/higgsfield-ai/skills/blob/main/higgsfield-soul-id/SKILL.md | 已查證（和 help center 張數衝突） |
| 定價頁 | https://higgsfield.ai/pricing | **讀不到**（動態載入） |
| 本 session 的 MCP 工具說明與目錄 | `generate_image`、`generate_image_batch`、`ai_influencer_prepare`、`ai_influencer_generate`、`build_ai_influencer`、`show_characters`、`show_reference_elements`、`manage_reference_elements`、`models_explore`、`get_workflow_instructions` | 已觀察（MCP；非製作師帳號） |
