# 舊專案方法參考分析（Virtual_KOL_Studio → Luscena KOL）

> 用途：為「Luscena KOL」（台灣客戶、10 個 AI 虛擬人設 Threads 帳號）整理可沿用的方法與必須避開的失敗。
> 性質：**研究筆記**。文中標 **PROPOSED** 的項目是建議，尚未經客戶或專案負責人核准。
> 原則：只寫實際讀過的內容；「文件聲稱」與「有驗證證據」分開標示；舊專案的數值、模型與定位一律視為**歷史紀錄**，不是新專案的規格。

---

## 0. 來源紀錄

| 項目 | 內容 |
|---|---|
| Repo | https://github.com/pennyhuang-oss/Virtual_KOL_Studio（本機唯讀 clone：`/home/user/Virtual_KOL_Studio`，未修改、未 commit、未 push） |
| 讀取時的 checkout 分支 | `claude/luscena-kol-initial-draft-et17t8` |
| 讀取的 commit（HEAD，完整 SHA） | `c6c3512448571846918e99445b8a1e081a45d7e1`（2026-09-08 14:05 UTC，"Stop the detail page's videos from filling the viewport"） |
| 與 `origin/main` 的關係 | `git rev-parse origin/main` 同為 `c6c3512448571846918e99445b8a1e081a45d7e1` → **checkout 分支的 HEAD 與 origin/main 完全相同**，等同讀取 main |
| 讀取日期 | 2026-10-06 |
| 分支名稱附註 | 分支名含 "luscena"，但在該 repo 內 grep `luscena` 無任何結果；內容就是 main 的舊專案 |

### 0.1 實際讀過的檔案

| 檔案 | 讀取程度 |
|---|---|
| `README.md` | 全文 |
| `PERSONA_CANON.md` | 全文 |
| `kols/schema.json` | 全文（並以 jsonschema 實際驗證三位的 profile.json，見 §4-F6） |
| `kols/index.json` | 前約 3,000 字元＋以腳本取出三位的條目 |
| `kols/iris-chen/profile.json` | 全文 |
| `kols/iris-chen/character.md` | 標題全表＋L1–52、L100–120、L165–246 |
| `kols/iris-chen/content_style.md` | 標題全表＋L1–62、L155–200、L270–380 |
| `kols/iris-chen/generation_notes.md` | 標題全表＋L1–52、L84–130、L448–480 |
| `kols/rainie-hsu/profile.json` | 全文 |
| `kols/rainie-hsu/character.md` | 標題全表＋L1–50 |
| `kols/rainie-hsu/content_style.md` | 標題全表＋L1–32、L96–102、L286–292 |
| `kols/rainie-hsu/generation_notes.md`（121KB） | `##` 標題表＋L1–12、L149–215、L313–345、L365–380、L409–436、L490–560 |
| `kols/cheryl-soh/profile.json`、`character.md`、`content_style.md`、`generation_notes.md` | 全文 |
| `kols/cheryl-soh/identity/identity_master.json`、`_superseded_identity_master.json` | 全文 |
| `BATCH3_FACE_INVARIANT.md`、`FACE_CROP_PIPELINE.md` | 全文 |
| `KOL_TRAINING_SOP.md` | 標題全表＋L1–183、L535–574 |
| `PHOTO_DIRECTION_STANDARD.md` | 標題全表＋L1–30、L120–157 |
| `WARDROBE_SYSTEM.md` | 標題全表＋L1–28、L110–150、L280–314 |
| `CALIBRATION_TEST.md` | 標題全表＋L255–300、L340–375 |
| `BENCHMARK_ACCOUNTS.md` | L1–36 |
| `NEW_20_PERSONAS_PLAN.md` | 標題全表＋L1–90 |
| `review/README.md` | L1–30 |
| `review/soul_pilot/VERDICT_collision_v1.md` | 全文 |
| `review/soul_pilot/SCREEN19_ROOT_CAUSE.md` | 標題全表＋L60–121 |
| `review/soul_pilot/cheryl-soh/VERDICT_v1.md` | L1–40 |
| `review/soul_pilot/cheryl-soh/prompts.json` | 只讀 `_cross_persona_finding` 一個欄位 |
| `review/soul_training/ACCEPTANCE_LOCKED.md` | 標題全表＋L27–75、L140–180 |
| `review/soul_training/RULING_collision_accepted.md` | 標題全表＋L1–30 |

**只列目錄、未開檔**：`kols/`、`review/`、`pilot/`、`review/soul_pilot/`、`review/soul_training/`、三位角色的 `images/` 子目錄（只數檔案數，未開任何圖片／影片）。
**全 repo grep**：`Threads`、`luscena`、`陳依琳`、`face_distinct_from`（只看命中行）。
**未讀**（僅被其他文件引用時提及）：`SEXY_SCENE_LIBRARY.md`、`MODELING_SHOOT_PLAN.md`、`CLAUDE_HANDOFF.md`、`COMPETITOR_sherry_digitalp510.md`、`review/LEDGER.md`、`pilot/*.json`、`business/*`、`clients/*`、`tools/*.py`、所有舞蹈／影片 SOP。

**私人資料處理**：`profile.json`／`character.md` 中的 `account_username`（註冊信箱／帳號用名稱）與 `date_of_birth` 欄位——含私人資料，未轉錄。文件中點名的真人（臉型參考藝人、被認出的真人、benchmark 真人帳號）一律不轉錄姓名或帳號。Soul ID、Job ID、Element ID 與本分析無關，不轉錄。

### 0.2 為什麼選這 3 位角色

| 角色 | 選擇理由 |
|---|---|
| `iris-chen` | **最成熟**：README「新增 KOL 流程」第 5 步（L210）指定她是「目前唯一有完整記錄『一次生成基本就對、身分穩定』成功經驗的案例」；`KOL_TRAINING_SOP.md` L16 標「✅ 完成」；有訓練集、影片、舞蹈紀錄。 |
| `rainie-hsu` | **問題記錄最多**：選角四輪被退、第一版 Soul 因身材不符被棄用（README L64）、被 `PERSONA_CANON.md` 原則六點名為「本 repo 的預設臉」（L264）、在憲章稽核中被列為「只在晚上存在」（L207）。 |
| `cheryl-soh` | **不同原型＋新管線**：Batch 3 的「職業型」人設（空服員）、走 identity_master＋部件裁切＋5 張訓練集＋事前鎖定驗收的新流程，且是實測撞臉（vs `zhiyi-shen`）的當事人。 |

---

## 1. 可沿用的角色資料結構、角色 Bible、內容指南及生成紀錄方式

### 1.1 `kols/schema.json` 欄位（文件聲稱的標準結構）

- **必填頂層**（L6–13）：`id`、`meta`、`identity`、`persona`、`content`、`social`；選填 `ai_assets`、`productions`。
- `meta`：必填 `created_at`、`updated_at`、`status`（enum `active`/`draft`/`archived`）、`category`；選填 `tags`、`reference_profiles`、`canon_version`。
- `identity`：必填 `name`、`handle`、`age`、`ethnicity`、`origin`、`current_location`、`languages`；選填 `date_of_birth`、`appearance`（`height`、`hair`、`eyes`、`style_vibe`、`measurements{height_cm, weight_kg, bust_cm, waist_cm, hip_cm, cup_size, leg_length_cm, body_ratio_note}`、`hair_note`）。
- `persona`：必填 `archetype`、`personality_traits`、`values`、`backstory`、`voice_tone`；選填 `humor_style`、`quirks`、`public_face`。
- `content`：必填 `pillars[{name, description, weight}]`、`formats`、`posting_frequency`、`aesthetic{color_palette, mood, editing_style}`；選填 `brand_do`、`brand_dont`（schema 描述限定「只放真正的紅線」）、`brand_fit_note`（風格偏好，不是禁令）。
- `social`：`display_name`、`creator_category`、`bio`、`account_username`、`platforms{<平台>: {handle, focus, follower_tier}}`（`follower_tier` enum `nano`…`mega`）、`engagement_style`、`community_name`。
- `ai_assets`（L19–48）：預期 `higgsfield_soul_id`、`soul_model`、`soul_status`（enum `pending`/`training`/`ready`/`failed`）、`training_image_count`、`training_images_path`。

**實際檔案超出 schema 的欄位**（在三位的 profile.json 看到、schema 沒定義）：`identity.appearance.face_type`、`figure`、`glasses`、`skin`、`hair_color_current`；`persona.private_side`、`signature_quota`；`meta.batch`；`ai_assets.<版本>.soul_training{status, soul_id, verification, status_definition, …}`。`face_distinct_from` 只在 `kols/nico-tsai/profile.json` 出現（grep 結果），三位都沒有。→ schema 沒有被強制執行（見 §4-F6）。

### 1.2 四個檔案的分工（`README.md` L162–170 ＋ `PERSONA_CANON.md` 原則五 L141–159）

| 檔案 | 職責 | 從三位實例觀察到的內容 |
|---|---|---|
| `profile.json` | 結構化資料；**`content.pillars` 是支柱的單一真理來源**（原則五第 1 條） | 身分、外型硬規格、人格、支柱與比重、品牌紅線、平台、AI 資產與訓練狀態 |
| `character.md` | 角色 Bible：她是誰、身分表、個性、視覺美學、「視覺行為光譜（不是絕對禁止）」、caption 語氣、品牌原則 | Iris 版 500+ 行、含鏡頭公式與服裝公式表；Cheryl 版 134 行、大量欄位直接複製 profile.json |
| `content_style.md` | 執行指南：同步的支柱表、每週發文節奏（按平台）、各支柱的具體 ideas／caption 範例／視覺規格、影片格式、造型四轉盤 | 支柱表帶 `<!-- 由 profile.json 同步，請勿手動編輯 -->` 標記 |
| `generation_notes.md` | 生成歷史：模型、prompt、批次、job、成本、逐張評估、狀態、下一步 | 原則五第 3 條：**歷史紀錄不回頭改寫**，只在檔頭加註 |
| `identity/identity_master.json`（Batch 3 新增） | 身分錨點的出處紀錄 | `status`、`approved_on`、`method`、`file`＋`sha256`、各部件來源與雜湊、完整 prompt、`credits`；被取代的版本以 `_superseded_` 前綴保留並寫明原因 |

其他可借鏡的結構慣例：
- 每份角色檔頭都有「受 `PERSONA_CANON.md` 約束、衝突時憲章優先」的 banner（三位皆有）。
- 憲章原則四 L131–137 把敘述分三類：**身分一致性規格**（硬）／**風格偏好**（`brand_fit_note`）／**真正的紅線**（`brand_dont`）。
- 視覺行為的語彙統一用「預設、多數時候」「不常見（不是不可能）」（原則四 L121–129）。

### 1.3 對 Luscena 的建議（PROPOSED）

1. **沿用四檔分工＋`identity/` 出處紀錄**，但 `profile.json` 是唯一手寫的結構化來源；`character.md`／`content_style.md` 中的同步段落改由腳本生成，並在 CI 檢查「同步段落 = 腳本輸出」。舊專案只靠註解標記，結果不同步（§4-F6）。
2. **schema 改為可強制**：`additionalProperties: false`、把實際使用的 `ai_assets.*.soul_training`／`verification` 結構寫進 schema、狀態用 enum，並在 CI 跑 jsonschema。
3. **新增欄位**：`face_geometry`（可量測的骨架描述，見原則六-A）、`face_distinct_from`（必填，指名最近的對象）、`status_evidence`（每個狀態都要附證據路徑）、`threads`（文字語氣、貼文長度、回覆政策、發文節奏）、`brand_safety`（客戶核准的尺度）、`ai_disclosure`（UNKNOWN，待客戶／法務）。
4. **`generation_notes.md` 維持 append-only，但檔頭的「目前狀態」區塊改由 `profile.json` 自動產生**，避免檔頭與實際狀態矛盾（§4-F7）。失敗嘗試也要記錄，不可只記成功。
5. **註冊帳號、生日、信箱、密碼等不放進 repo**，改存在客戶指定的密碼管理工具；repo 只放公開 handle。

---

## 2. 可沿用的身分一致性、場景／造型變化與素材 QA 方法

### 2.1 身分建立流程（文件化的步驟）

- **兩段式：先選角、再錨定、再訓練**。`kols/rainie-hsu/generation_notes.md` L153：「獨立生成的圖片彼此不共享身分，因此第一階段先產出一小批『候選圖』讓使用者挑出喜歡的臉／風格，確認後才對該張核准圖建立 Reference Element 錨定身分，再擴充成完整訓練集。」
- **人工關卡**：`README.md` L214「停下來，等使用者實際看過這批參考圖並明確確認滿意後，才可以進入下一步」。
- **選角時臉與身材都要核對**：`kols/cheryl-soh/generation_notes.md` L45「選角階段**必須同時核對臉部與身材**——Rainie Hsu 就是只看臉沒核身材，整批訓練圖作廢重做。」
- **建檔照 ≠ 公開造型**：`BATCH3_FACE_INVARIANT.md` L84–85「identity master 是建檔照，不是她的公開造型。建檔照必須露眉」；訓練集大多露眉、只留 4–6 張招牌瀏海（L102–106）。
- **老態與眼神的正面描述**：L144–151（臉頰平滑、眼周無細紋、不要笑；兩眼瞳孔位置與反光點一致）。
- **錨點會「整件複製」**：`KOL_TRAINING_SOP.md` §4（L96–104）同一件衣服的細節會被原封不動複製；§5（L106–109）錨點的髮色細節蓋不掉 → 選角階段就要把衣服與髮色看清楚。

### 2.2 部件裁切管線（`FACE_CROP_PIPELINE.md`）

- 核心結論（L5–16）：四格消融證明「**裁切是必要因素，措辭不是**」；「這個模型不執行否定句。要移除的東西必須在輸入端移除。」
- 四槽位（L33–43）：`FACE_SHAPE_AND_JAW`（4:5）、`EYES_AND_BROWS`（3:1）、`NOSE`（1:1）、`MOUTH`（2:1）；部件槽補灰邊、**絕不拉伸**。
- QA 門檻（L45–54）：`padding_ratio ≤ 0.12`、`yaw_proxy ≤ 0.14`（雙眼 ≤ 0.08）、原圖部位短邊 ≥ 96px、逐槽 bleed 規則；`check_face_crops.py` 擋下引用未過 QA 裁切的角色。
- 唯一鍵 `(source_ref_id, slot, crop_spec_version)`、每檔雜湊 → **可追溯的 provenance** 是值得沿用的做法。
- **重要限制**：臉型槽是身分主導槽（`BATCH3_FACE_INVARIANT.md` L113–136），且整張人像放進臉型槽會「照搬來源本人」（L179–199）。→ 對 Luscena 而言，**任何真人照片都不得作為臉部來源**（§4-F2）。

### 2.3 撞臉篩檢（`PERSONA_CANON.md` 原則六、七；`KOL_TRAINING_SOP.md` L537–561）

- 原則六 L274–278：`face_type` 必須寫**骨架**；必附 `face_distinct_from`；「改妝容、改髮型、改髮色**不能**用來解決撞臉。撞臉只能改骨架。」
- 六-A／B／C（L308–317）：骨架描述要可量測；`face_distinct_from` 必填且指名距離最近者；進庫前跑 0 成本配對距離篩檢。
- 方法（SOP L556–557）：mediapipe landmarks → 置中與 RMS 尺度正規化 → SVD Procrustes 對齊 → 平均 RMS 距離；≤ 0.0220 的配對**遮掉髮型髮色**並排目視。
- 遮髮盲測設計（`review/soul_pilot/VERDICT_collision_v1.md` L14–26）：橢圓遮罩去髮、打亂標籤、答案鍵判定前不讀、兩位用**逐字相同**的驗證 prompt。
- 已接受碰撞時的損害控制（原則七 L340–354）：C-1 髮型成為身分區分要件、不得換成碰撞對象的髮型；C-2 有碰撞關係者**不得同框**。原則七 L335–338 明言「C-1／C-2 不是解決方案」。

### 2.4 訓練後驗證（`review/soul_training/ACCEPTANCE_LOCKED.md`）

- **門檻在看到結果前寫死**（§四 L51–63）：同一人、無漂移、身材符合、不重現訓練集服裝背景、碰撞盲測。
- **驗證 prompt 不得洩題**（§二 L27–38）：不重述五官、不重述三圍、不用訓練集出現過的服裝場景、要寫髮色髮型、每 spec 一張、不 reroll。
- 6 張驗證規格 V1–V6（§三 L40–49）：正面基準／左前 3/4／右前 3/4 非中性表情／全身身材／戶外動態／困難條件自拍（弱光＋低妝＋束髮）。
- **誠實分級**（附記二 L140–178）：19/19 未通過身材門檻、碰撞門檻失敗，故不標 `approved`，改用 `production_ready` 並註明「身材靠 prompt 補、碰撞風險已接受」；`approved` 刻意保留給「真正修完」的狀態。

### 2.5 訓練集與日常素材是兩套規則（`KOL_TRAINING_SOP.md` L120–142）

| | 訓練集 | 日常素材 |
|---|---|---|
| 公共場景背景路人 | 不要（可能被學進身分） | 必須有 |
| 濾鏡 | 幾乎不用 | 自由 |
| 視角 | 他拍為主 | 大量混合 |

L140–142：「Soul 訓練一完成，日常素材必須立刻切回右欄——否則那個『空無一人的台北』會變成這個角色所有素材的共同特徵。」

### 2.6 造型與場景輪替（`WARDROBE_SYSTEM.md`、`PERSONA_CANON.md` 原則二、三）

- 核心診斷（WARDROBE L14–24）：「**當支柱＝活動，服裝與場景就變成活動的附屬品**……每個角色被自己的人設關進了一個房間。」
- 四個獨立轉盤（L110–147）：
  1. 穿搭：每角色 ≥ 8 種風格區間，**連續兩則不可同區間**，招牌風格 ≤ 30%。
  2. 髮型：≥ 5 種，每則明確指定。
  3. 地點層級：每 10 則 A 級 2–3、B 級 4–5、**C 級「完全不美的日常」≥ 2（硬性下限）**。
  4. 微物件：每則 ≥ 2 樣，prompt 具體點名。
- 服裝 prompt 寫滿五層（`kols/iris-chen/content_style.md` L369–375）：上身＋下身＋鞋＋包或外套＋首飾髮飾。
- 標誌性場景配額（憲章原則二 L66–84）：不得寫進人設基調、不得為主支柱、不得 > 25%；判斷句「她一年 365 天會不會有 300 天都長這樣？」
- 髮型可變（原則三 L88–99）：髮色髮型是「現階段」設定；但若有碰撞關係，受原則七 C-1 收緊。
- 同穿搭一日敘事、背景路人四條件（背向／不看鏡頭／失焦／外型區隔）：`kols/iris-chen/generation_notes.md` L469–476 記錄 14/14、7/7 成功（**同一批次 14 張，n 小**）。

### 2.7 素材 QA 清單

- AI 破綻五項（`PHOTO_DIRECTION_STANDARD.md` §五 L122–135）：手指、文字、皮膚、**臉部與背景光線方向一致**、背景拼貼感。
- 日常素材開跑前五項（`KOL_TRAINING_SOP.md` L151–158）：背景路人、具名反射面、曝光犧牲一邊、兩個色溫、C 級地點下限。
- 造型四項（`WARDROBE_SYSTEM.md` §六 L282–289）。
- 服裝覆蓋度要逐張目視：`review/soul_pilot/cheryl-soh/prompts.json` `_cross_persona_finding`：「服裝的覆蓋度與長度不被可靠執行，且偏差方向一致——都往更露、更短」，11 張中 4 張，「單向——沒有出現比指定更保守的案例」。
- 事前訂判定門檻、附「反證表」（`CALIBRATION_TEST.md` §7；L265–271 實例：1 分差低於預設門檻，不下結論）。

### 2.8 對 Luscena 的建議（PROPOSED）

- 沿用：兩段式建角＋人工關卡、identity master 出處 JSON、事前鎖定驗收門檻、遮髮配對篩檢、V1–V6 驗證設計、誠實狀態分級、四轉盤、C 級地點下限、AI 破綻五項、服裝覆蓋度逐張驗收。
- 改寫：所有門檻數值（0.0220、yaw 0.14 等）**在新工具上重新校準**後才採用；QA 清單必須包含「好看／符合客戶審美」「身材」「品牌尺度」三項，不能只有可量測項（§4-F3）。
- 10 位全部在進庫前就做 45 組配對篩檢（10 選 2），而不是像舊專案訓練完 19 位才發現。

---

## 3. 舊專案獨有、不能自動套用到新專案的策略

> **明確聲明：舊專案的性感尺度、全女性配置、國籍配置與平台策略，一律不得自動套用到 Luscena。** 以下每一項若要在 Luscena 使用，都必須由客戶與專案負責人另行決定並寫進 Luscena 自己的規格。

| 類別 | 舊專案的做法（出處） | 為什麼不能直接套用 |
|---|---|---|
| **內容定位與性感尺度** | `README.md` L19：「以模仿日本 AV 女優公開社群帳號的風格為核心方向，打造具有強烈寄生親密感（parasocial intimacy）的虛擬創作者」；`BENCHMARK_ACCOUNTS.md` L18：「非常性感且樂於展示身材……性感身材展示才是首要」；憲章原則一 L28–30：「私底下……展現性感的一面——貼身／性感服裝、Cosplay、內衣、私密自拍」；私下支柱一律最大（25–30%）。 | Luscena 是台灣客戶的 Threads 帳號，品牌尺度未知；舊專案的反差公式與支柱比重是為性感定位設計的。 |
| **性別** | `NEW_20_PERSONAS_PLAN.md` L1「新增 20 位女性 KOL」；README 陣容全為女性。 | Luscena 的性別組成未定（UNKNOWN）。 |
| **國籍／族裔** | `NEW_20_PERSONAS_PLAN.md` §0.7 國籍配比（台 5／日 4／韓 3／中 3／新 2／馬 2／印尼 1）；§0.6「膚色一律白皙、透亮、瓷感」「印尼、新加坡、馬來西亞籍一律設定為華裔……排除 Southeast Asian-leaning features」。 | 這是舊專案的審美決策，且這段共用硬規格被 `SCREEN19_ROOT_CAUSE.md` §五 列為撞臉的共同成因。 |
| **身材硬規格** | 每位都有三圍、罩杯、腿長比例（schema `measurements`）。 | 是否需要身材規格由 Luscena 的人設方向決定；且 Soul V2 實測不繼承身材（`ACCEPTANCE_LOCKED.md` 附記二）。 |
| **平台策略** | `README.md` L194–200：TikTok／IG Reels／X；`BENCHMARK_ACCOUNTS.md` L22–30 加小紅書；憲章原則一的「私底下」指「她自己經營的私人平台」。Threads 只在 `coco-wu`、`sophia-tseng` 的 content_style 以次要平台出現（grep 結果）。 | Luscena 以 Threads 為主，文字比重、互動模式與圖文比例都不同；舊專案沒有可直接沿用的 Threads 策略。 |
| **Benchmark 方式** | 原始 6 位點名真人帳號（含成人影片從業者）作模板；`BENCHMARK_ACCOUNTS.md` L6 自己承認這是「拿真人身分做非經同意的商業模板」，新 5 位已改為風格描述。 | Luscena 不應點名真人作模板。 |
| **變現／商務** | `business/`、`clients/` 目錄存在（未讀）；grep 顯示 `business/pricing-and-packaging.md` 有「FB + IG + Threads」方案、`internal-approval-brief.md` 寫帳號「由客戶名義開通並持有」。 | 未讀全文，**UNKNOWN**；不可推定適用。 |
| **工具與模型** | Higgsfield `soul_2`＋`soul_id`、`seedream_v4_5`、`cinematic_studio_video_v2`、`kling3_0`、`seedance_2_0`、Recraft V4.1（評為不適合）；README L183–190 規則（`multi_shot_mode: auto` 等）；`kols/iris-chen/generation_notes.md` L84–95 的 localStorage 操作法。 | 全是 2026-06～09 的特定工具版本與介面；2026-10 是否仍可用、行為是否相同，未驗證。 |
| **數值門檻與成本** | `KOL_TRAINING_SOP.md` L166–171：seedream 1 credit／張、Soul 訓練 25 credits、soul_2 出圖 0.12／張；撞臉門檻 0.0220（以單一失敗配對 0.0157 校準）；「5 張訓練集足夠」（SOP L574）；Iris 訓練 14 張、Rainie 13 張。 | 這些是特定模型、特定帳號、特定時間的測量值，樣本小（見 §4-F8）。 |
| **審核流程** | Claude ⇄ ChatGPT 交叉覆核、`LEDGER.md` 全結案前不得生成（`README.md` L9–13；`review/README.md`）。 | 「先覆核再生成」的精神可借鏡，但具體流程（手動複製貼上、CHECKPOINT）是舊專案的情境。 |

---

## 4. 過去實際發生的失敗與新專案的防範

### F1. 不同角色撞臉（有量測證據）

- **證據**：
  - `review/soul_pilot/VERDICT_collision_v1.md` L28–43：`cheryl-soh` ↔ `zhiyi-shen` 遮髮盲測 **6/8**，V6 那一對「完全對調」；L61–66：兩位 identity master 距離 0.0157，「比同一人不同張之間的差距還小」。
  - `PERSONA_CANON.md` L290–294：171 組配對中 41 組（24%）≤ 0.0220；19 位中 17 位至少牽涉一組。
  - `PERSONA_CANON.md` L264–271：模型預設美女臉 ≈ `rainie-hsu`，`sophia-tseng` 與 `nico-tsai` 都收斂過去。
  - `KOL_TRAINING_SOP.md` §新增 5 位：Zoe Lai「反覆出現臉部辨識問題（跟其他角色撞臉……）」，整個人設被刪除。
  - `BATCH3_FACE_INVARIANT.md` L120–129：被退的 4 對「太像」全部只共用臉型槽。
- **成因（文件判讀）**：`SCREEN19_ROOT_CAUSE.md` §五：20 位共用同一段 `appearance.skin` 硬規格（同時鎖膚色與五官族裔）＋共用模板，壓過每人一行的 `face_type`；且 19 位都沒有 `face_distinct_from`（原則六補記 L284–285）。
- **處置**：使用者裁定接受風險（`RULING_collision_accepted.md` L3–10），骨架撞臉「仍然存在、仍然沒有修」（憲章 L336–337）。
- **Luscena 防範**：10 位在**生成 identity 前**就寫可量測骨架＋`face_distinct_from`；共用規格只管膚色等非五官項；identity 生成後、訓練前跑 45 組配對篩檢＋遮髮目視；把「不靠髮型區分」設為驗收條件，不重演「髮型承重」。

### F2. 臉部來源帶入真人辨識度

- **證據**：
  - `BATCH3_FACE_INVARIANT.md` L155–161：「臉型槽用到『一眼認得出是哪個真人』的參考圖時，輸出就是那個真人」；有三位角色被認出是來源照本人（其中一位被指認為某真實藝人，文件點名，此處不轉錄）。
  - `kols/cheryl-soh/identity/_superseded_identity_master.json` `_superseded`：「臉型槽附整張人像，輸出照搬了來源照本人。」
  - `FACE_CROP_PIPELINE.md` L58：「原本 15 張**真人照片**」；但 `BATCH3_FACE_INVARIANT.md` L9 規定 19 張臉「一律用 `ref_01`–`ref_15` 這 15 張美女參考圖的五官 remix」——兩份文件結論互相矛盾。
  - `kols/iris-chen/profile.json` `identity.appearance.face_type` 與 `generation_notes.md` L22 直接寫一位台灣真人藝人作臉型參考（不轉錄姓名）。
- **Luscena 防範**：**禁止以任何真人照片、真人姓名或真人帳號作為臉部、身材或風格來源**；臉部來源只用合成且有完整 provenance 的素材；每位 identity 加一道「與公眾人物相似度」人工檢查並留紀錄。此項涉及肖像權與客戶品牌風險，建議請客戶法務確認（UNKNOWN）。

### F3. QA 清單漏掉關鍵維度，導致整批作廢

- **證據**：
  - `kols/rainie-hsu/generation_notes.md` L365–377：2026-07-30 的「誠實視覺評估」檢查了身分、自拍軟化、跨支柱穿搭、妝容，**沒有身材項**；L492：2026-08-05 才發現「身材完全未吃到 94-59-92cm/F 罩杯設定……當初選錨點只核對了臉部/妝容」；`profile.json` `training_images_v1.status: "deprecated"`，已訓練的 Soul 棄用。L505：「換錨點＝換臉」。
  - `BATCH3_FACE_INVARIANT.md` L34–46：裁切 QA「量的是『好不好裁』，沒有任何一項在量『好不好看』」，最後生出被評為「外星人般的醜女」的臉；「每一步單獨看都『通過了檢查』，因為檢查裡沒有美感這一項。」
- **Luscena 防範**：驗收清單在開工前由客戶確認，至少包含「客戶審美」「身材／比例」「品牌尺度」「身分一致」「撞臉」五類；任何自動化 gate 都要附人工審美關卡。

### F4. 身分漂移與「訓練素材鎖死場景」

- **證據**：
  - `CALIBRATION_TEST.md` L273–282：prompt 明寫台北巷弄，輸出卻是首爾街景（韓文招牌）；「場景不是被 prompt 決定的，是被 `soul_id` 帶出來的」。L352–360：明寫不要天空仍「完全被無視」——「`soul_id` 鎖住的不只是國家，是**整個街拍構圖模板**」。
  - `ACCEPTANCE_LOCKED.md` 附記二 L148–153：身材門檻 **19/19 未通過**（Soul V2 不繼承身材與身高），改用 prompt 補，「嬌小感補正尚未驗證」。
  - `KOL_TRAINING_SOP.md` §4、§5：錨點的衣服與髮色細節會被帶下去、prompt 蓋不掉。
- **Luscena 防範**：訓練集刻意分散場景（室內／室外、城市元素），避免單一場景類型佔多數；訓練後的驗證必須包含「訓練集沒出現過的場景類型」；身材若是需求，要有獨立驗收項。

### F5. 人設被鎖在一個職業／一套衣服／一個房間

- **證據**：`PERSONA_CANON.md` §C 表（L201–207）：Coco 宿舍合計 50%、archetype 寫宿舍是「全部場景」；Mia 直播間 30%＋禁止白天戶外；Vicky 健身房 30%；Sophia 五星飯店是「主場」；Rainie「只在晚上存在」。`WARDROBE_SYSTEM.md` L6 使用者原話：「做瑜伽的就只穿韻律衣、喜歡衝浪的就只穿比基尼、遊戲直播主就只戴耳機坐在電腦前。這很不 OK。」
- **仍未完全解決的跡象**：`kols/cheryl-soh/profile.json` 的 `archetype` 與 `public_face` 都是同一句「制服與時差」，支柱有「制服／出勤」20%＋「飯店／各國城市」15%；`NEW_20_PERSONAS_PLAN.md` §0.1（L22–27）仍寫「檯面上：一份正常、可被社會接受的職業」，與憲章 v2「檯面 ≠ 職業」（L32–45）矛盾。
- **Luscena 防範**：支柱以「生活面向」而非「活動／職業」命名；每位都要有房間以外、職業以外的支柱；任何單一場景／服裝類型 ≤ 25%；每週排程檢查連續貼文的場景與造型重複。

### F6. 檔案彼此不同步（本次實際比對結果）

憲章 L241–253 聲稱「全檔同步範圍（2026-08-27 已完成）」，以下是本次比對三位角色找到的具體不一致：

| 角色 | 不一致 | 出處 |
|---|---|---|
| iris-chen | 同步表的比重（25/18/15/15/12/10/5）與同檔下方各支柱段落標題不同：早晨 20%、穿搭 20%、浴室 15%、飯店 15%、健身 10%，另有 profile.json 沒有的「TikTok 熱梗舞／舞蹈影片（20%）」支柱；段落合計 140% | `content_style.md` L12–28 vs L63、L96、L128、L161、L190、L218、L250、L274 |
| iris-chen | 週節奏表仍排「TikTok 熱梗舞」為一個支柱 | `content_style.md` L34–43 |
| iris-chen | 語言：profile.json 有日文（basic），`character.md` 身分表只寫中、英 | `character.md` L40 |
| iris-chen | 中文名在 benchmark 文件寫成「陳依琳」，其他檔案都是「陳芯語」 | `BENCHMARK_ACCOUNTS.md` L33 |
| iris-chen | 私下支柱說「避免沙發（沙發是公開面貌的場景）」，Bible 開場與鏡頭公式卻以沙發為私下場景 | `content_style.md` L186 vs `character.md` L24 與鏡頭公式表 |
| rainie-hsu | 同步表 25/22/20/13/10/10，下方段落為早晨 15%、穿搭 30%、浴室 15%、飯店 15%，另有 profile.json 沒有的「健身／舞蹈有氧（10%）」；段落合計 130% | `content_style.md` L14–31 vs L65、L98、L136、L169、L198、L226、L259 |
| rainie-hsu | 憲章自身矛盾：§A 說 Rainie 改為「白天的她」20%（L187）；§C 表說新增「白天的她」15% 與「酒吧／上班的日子」13%（L207）。profile.json 是前者 | `PERSONA_CANON.md` L187 vs L207 |
| rainie-hsu | 妝容：profile.json `face_type` 寫「NO visible wing or flick at all」；generation_notes 記錄使用者接受「可見眼線甩尾＋飽和珊瑚唇」 | `profile.json` vs `generation_notes.md` L8、L315 |
| rainie-hsu | 訓練集依舊的 30/15/15/15/15/10% 與「居家／空檔」支柱配置，不是 profile.json 現行支柱 | `generation_notes.md` L345、L513 |
| cheryl-soh | 4/5 支柱沒有內容：profile.json 寫「詳見 content_style.md 同名段落」，content_style.md 的同名段落也寫「詳見 content_style.md 同名段落」（循環引用） | `profile.json` `content.pillars`；`content_style.md` L58–92；`character.md` L91–101 |
| cheryl-soh | content_style.md 提到「外出／…」支柱，但她沒有這個支柱（模板殘留） | `content_style.md` L25 |
| 全部 | `canon_version`：iris／rainie 為「v1」，憲章現為 v2 並已加到原則七 | `PERSONA_CANON.md` L7 |
| schema | 以 jsonschema 實測：iris、rainie 的 `social.platforms.twitter_x.follower_tier: "small"` 不在 enum，**驗證失敗**；cheryl 的 `soul_training.status: "production_ready"` 不在 schema 的 `soul_status` enum，但因實際結構與 schema 不符而**未被檢查到** | `kols/schema.json` L31–39、L341–350 |

另：`kols/rainie-hsu/generation_notes.md` L181 記錄更早的同步失敗——「character-sheet 的文字改了，但實際送進模型的 prompt 沒有改」，舊的貓眼眼線／正紅唇字串留在 prompt 本體。

- **Luscena 防範**：同步段落全由腳本產生並在 CI 比對；CI 跑 schema 驗證（`additionalProperties: false`）；支柱比重合計必須 = 100%；prompt 由 `profile.json` 組裝，不手抄外型描述；任何人設改動的 PR 都要附「掃過的檔案清單」。

### F7. 文件聲稱「完成／active／PASS」但證據不足或互相矛盾

| 聲稱 | 實際情況 | 出處 |
|---|---|---|
| 憲章「全檔同步（2026-08-27 已完成）」 | 見 F6，至少兩位的 content_style 段落未同步 | `PERSONA_CANON.md` L241 |
| Rainie generation_notes 檔頭「✅ Soul 訓練已完成（`status: ready`），soul_id 994e… 已可用」 | 同一段落又說 `raw_status` 仍為 `queued`；該 Soul 後來被棄用 | `generation_notes.md` L8；`profile.json` `training_images_v1` |
| Cheryl profile.json `training_images_v1.status: "completed"` | 同一物件的 `note` 寫「PENDING — 尚未執行選角與訓練集生成」 | `profile.json` |
| Cheryl generation_notes「Soul 訓練 ⏸ 待執行」「Soul ID：尚未取得」「生成紀錄（尚無紀錄）」 | profile.json 記錄 2026-09-07 已訓練、6 張驗證完成、`production_ready` | `generation_notes.md` L16、L35、L54 |
| README 把 Batch 3 列為「待訓練／draft」、「其餘 19 位凍結中」、「generation_notes 皆為 PENDING」 | 依 `PERSONA_CANON.md` L280 與 `ACCEPTANCE_LOCKED.md` 附記二，19 位已於 2026-09-07 完成訓練與驗證；`meta.status` 仍為 `draft`、`updated_at` 仍為 2026-08-27 | `README.md` L81–87、L107 |
| `WARDROBE_SYSTEM.md`「✅ 系統有效」 | 依據是 **2 張圖**的實測 | L295–308 |
| Iris 是「唯一完整成功案例」 | 她的 generation_notes 檔頭寫「只記錄確認有效的版本和步驟。錯誤嘗試已略去」——成功紀錄經過篩選，失敗不可查 | `README.md` L210；`kols/iris-chen/generation_notes.md` L8 |
| 單人門檻「通過」 | 盲測與判定由執行者本人做（「我的判定」）；量化交叉檢查反而把 cheryl V3 判得更接近 zhiyi | `VERDICT_collision_v1.md` L30–58；`cheryl-soh/VERDICT_v1.md` |

正面例子（值得沿用）：`ACCEPTANCE_LOCKED.md` 附記二因「寫成 approved 會失實」而另設 `production_ready`；`VERDICT_collision_v1.md` 判定前不讀答案鍵；`CALIBRATION_TEST.md` L269「如果沒有預先訂門檻，我現在就會直接宣布……」。

- **Luscena 防範**：每個狀態值都要附證據路徑（圖檔路徑＋雜湊、驗證報告、平台回傳紀錄）；「完成」只能由非執行者（客戶或指定審核人）核准；狀態以 `profile.json` 為準，其他檔案只引用不重述；失敗紀錄與成功紀錄同等保存。

### F8. 舊模型能力與數值門檻不能直接當真

- **證據**：
  - README L211 以「`seedream_v4_5` 同 prompt 重複生成的身分一致性明顯優於 `soul_2`」為預設規則；但 `kols/rainie-hsu/generation_notes.md` L492 事後寫「`candidate_01`–`04` 是各自獨立生成（無 Reference Element 錨定），身材本來就不是同一套」，L505「是各自獨立生成的 4 個人」。
  - `PHOTO_DIRECTION_STANDARD.md` L7–25 修正說明：「機位＝身高×0.60」「全身一律 85mm」等「都是起點與方向，不是規格」，且「這些知識目前**都還沒有在 Soul 2.0 上被驗證過**」；但同檔 §七 清單（L146–157）仍要求「機位寫了**離地公分數**」「全身是 85mm」，並要求皮膚**不得**寫 `porcelain`——而 Rainie 與 Batch 3 的硬規格正是 `porcelain-toned skin`。
  - 撞臉門檻 0.0220 以單一失敗配對（0.0157）校準（`KOL_TRAINING_SOP.md` L558）。
  - 「5 張訓練集足夠」出自同一模型、同一批（SOP L574）。
  - 服裝覆蓋度執行率低（11 張中 4 張偏露，`prompts.json` `_cross_persona_finding`）；否定句無效、角度寫法被畫成背影（SOP §1、§2）。
- **Luscena 防範**：所有舊數值只當「待驗證假設」；選定 2026-10 實際使用的工具後，先做小樣本校準（事前訂門檻與反證條件），再寫入 Luscena 規格；規格中每個數值附「校準日期、工具版本、樣本數」。

### F9. 規則只存在對話裡，壓縮後遺失

- **證據**：`BATCH3_FACE_INVARIANT.md` L24–28：「這條規則原本只存在於對話裡。中途對話被壓縮過一次……於是後面每一層都建立在錯的素材上。」另 `KOL_TRAINING_SOP.md` L122–126、L146–150：規則早已寫在 `SEXY_SCENE_LIBRARY.md`，但「分散之後就容易在單一批次裡被整段略過」。
- **Luscena 防範**：所有客戶決策與規則寫進 repo（帶日期與決策人），關鍵規則配自動檢查；每批生成前用一份精簡的 checklist，不依賴執行者記得分散在多份文件的規則。

### F10. 共用帳號導致成本無法對帳

- **證據**：`KOL_TRAINING_SOP.md` L566–568：「**絕不看 `balance`**——本批全程有另一位使用者並行使用同一帳號，餘額對帳一次都對不起來」；`kols/rainie-hsu/generation_notes.md` L166、L341、L421–426 多次記錄餘額變化與預估不符。
- **Luscena 防範**：使用專屬工作區或帳號；成本以交易明細對帳，每批記錄預估 vs 實際。

---

## 5. 對 Luscena 專案的具體建議

### 5.1 可沿用（改成 Luscena 版後使用）

- [ ] 四檔分工＋`identity/` 出處 JSON（§1.2）；憲章 banner；三類敘述分法（硬規格／偏好／紅線）。
- [ ] 「不寫絕對禁令」語彙與「365／300 天」判斷句（憲章原則二、四）。
- [ ] 兩段式建角＋人工關卡；選角同時核對臉、身材、審美。
- [ ] 事前鎖定的驗收門檻＋V1–V6 驗證設計＋不洩題規則（`ACCEPTANCE_LOCKED.md` §二～四）。
- [ ] 遮髮配對篩檢流程（方法沿用，門檻重新校準）。
- [ ] 訓練集 vs 日常素材兩欄規則（SOP L130–138）。
- [ ] 四轉盤、C 級地點下限、五層服裝描述、AI 破綻五項、服裝覆蓋度逐張驗收。
- [ ] 誠實狀態分級（`production_ready` vs `approved` 的區分精神）。

### 5.2 必須重寫

- [ ] Luscena 自己的人設憲章：定位、尺度、性別、年齡、族裔、平台都由客戶決定，**不繼承**舊專案的性感定位、全女性、國籍配比與 TikTok／IG／X 平台策略。
- [ ] Threads 專用的內容指南：文字語氣、貼文長度、圖文比例、回覆與互動政策、發文節奏（舊專案沒有可沿用的版本）。
- [ ] schema：加 `face_geometry`、`face_distinct_from`、`status_evidence`、`threads`、`brand_safety`；可強制驗證。
- [ ] prompt 組裝：由 `profile.json` 生成，不手抄；共用規格只管非五官項。
- [ ] 臉部來源政策：零真人來源、合成來源需 provenance。
- [ ] 所有模型名稱、價格、門檻：依 2026-10 實際工具重新校準。

### 5.3 UNKNOWN（需客戶或負責人回覆）

1. 10 位的性別、年齡層、族裔與城市設定；是否全為台灣人設。
2. 品牌尺度（是否允許任何性感內容）與客戶的禁止清單。
3. AI 虛擬身分的揭露方式（Threads／Meta 的 AI 標示政策與台灣相關法規），需法務確認。
4. 2026-10 實際使用的圖像／影片工具，以及是否有類似 Soul 的身分訓練功能。
5. Threads 帳號由誰開通與持有、發文與回覆由誰執行、審核流程。
6. 是否需要影片內容；是否需要跨平台（IG／FB）同步。
7. 預算與每位角色的建置成本上限。
8. 舊專案 `business/`、`clients/` 文件是否與 Luscena 商務模式相關（本次未讀）。
9. 10 位之間允許的相似度底線，以及是否允許兩位同框。
