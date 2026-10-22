# 先鋒四人身材設定 v2（2026-10-12）

- 決定者：製作師（Vincent）。本檔取代 `REPORT.md`「身材補充」中 Vicky 的那一列；其他三人沿用。
- 規則：數字只寫在文件，prompt 用身形描述，不直接給數字。十人都是成年人。
- 變更紀錄：2026-10-12 Vicky 罩杯 C → E，身形改為前凸後翹明顯的沙漏型（REPORT 追加 27）。2026-10-13 新增 §2.5 美肌程度（依角色區分，REPORT 追加 46、47）。2026-10-21 新增第五人 Rainie Hsu（夜店咖、皮衣；製作師照執行者提案定案）。

## 1. 設定表

| 角色 | 身高 | 三圍 | 上圍／下胸圍 | 罩杯 | 體型 | 狀態 |
|---|---|---|---|---|---|---|
| Wendy Yeo | 170 | 86／60／90 | 86／72 | C（70C） | 高挑骨感、肩線平、腿長 | 沿用 |
| Kanon Komori | 155 | 84／58／86 | 84／68 | D（65D） | 嬌小、腰細 | 沿用 |
| **Vicky Lin** | 168 | **94／63／92** | **94／74** | **E（75E）** | **沙漏型：胸大前凸、腰細、臀圓翹、大腿厚實；運動型、曬色** | **v2（2026-10-12）** |
| Nanami Fujiwara | 160 | 90／62／91 | 90／70 | E（70E） | 柔軟豐滿 | 沿用 |
| **Rainie Hsu** | 167 | **88／57／88** | **88／68** | **E（70E）** | **纖腰長腿、胸型飽滿；骨架細，不走肌肉線條** | **新增（2026-10-21）** |

- Vicky 臀圍：製作師只指示「後翹明顯」，未給數字；表中 92 沿用 v1。執行者提案改 96（PROPOSED，待製作師定）。
- Rainie 與其他人的區隔：Vicky 同樣高挑，但是運動型沙漏、大腿厚實，Rainie 是細骨架、五人裡腰最細；Nanami 同樣 E 罩杯，但是柔軟豐滿，Rainie 較高、較瘦；Wendy 骨感、胸型偏小。生日 2001-11-13（天蠍座，執行者擬、製作師採用），2026-10 時 24 歲。

## 1.5 身形比例參考圖（定稿）

之後出圖要對身形比例時，以這裡的圖為準。檔案在 `社群媒體/身形參考/`，備份在 `Documents\Luscena_KOL_定稿備份\身形參考\`。

| 角色 | 正面 | 側面 | 定稿 | 做法 |
|---|---|---|---|---|
| Kanon Komori | `kanon_body_front_job5e868709.jpg` | `kanon_body_side_job4805c7a7.jpg` | 製作師 2026-10-22 | 先出側面（Nano Banana Pro＋Kanon v4 Element、文字比例規格），再以側面當參考生成正面（REPORT 追加 284～291） |
| Vicky Lin | — | — | 製作中 | REPORT 追加 285～293 |
| Wendy Yeo | — | — | 製作中 | REPORT 追加 285～288 |
| Nanami Fujiwara | `nanami_body_front_job693e4809.jpg` | 候選 `42685e11`（待製作師定） | 正面：製作師 2026-10-22 | 先畫比例線稿（頭高為單位，依已發文圖 3D 量測＋製作師修正肩／小腿／腰，v3），線稿＋253n 臉用 Seedream 5.0 Flash 轉真人，再用 Flash 把胸縮到 E；側面以正面定稿當參考用 Flash 生成（REPORT 追加 280～297） |

- 已知小差異（製作師接受）：Kanon 正面兩眼下各有一顆痣（設定只有一顆），用來對身形時不影響。

## 2. Vicky 的 prompt 身形描述（v2，定稿 job 309 用的寫法）

- 整體：`dramatic hourglass figure, athletic and curvy`
- 胸：`very large, full, round E-cup bust that projects far forward from her ribcage, filling and stretching the sports bra, top of the cleavage visible`
- 腰：`small, tight waist`
- 臀腿：`very full, round, high, lifted hips and buttocks; thick, strong, smooth thighs`
- 皮膚：`tanned skin with a light sweat sheen, beauty-camera smooth skin`
- 色氣路線（與 Wendy／Nanami 區隔）：健康的色氣——曬色、汗、線條、力量感；不走媚。
- 寫法注意：描述身形，不寫種族；胸部描述避免與「床、口含物、頸飾」疊加（NSFW 觸發，見追加 1）。

## 2.5 美肌程度（2026-10-13，製作師決定：依角色區分）

- 製作師在三個選項中選了第 3 個：不把四人統一成同一級，而是每個角色固定一級，同一角色的每張圖都要一致。已定稿的圖都不動。
- 量測方法與數值見 `REPORT.md` 追加 46 B（臉頰細紋理值，數字越低越平滑；只作輔助，以製作師目測為準）。

| 角色 | 級別 | 依據（定稿） | 細紋理值 | 理由 |
|---|---|---|---|---|
| Wendy Yeo | 輕美肌 | job 252 | 約 10 | 現況；成熟、冷感，保留質感 |
| Vicky Lin | 輕美肌 | job 314、319 | 約 10 | 健康曬色路線，看得到汗與毛孔才像運動的人 |
| Kanon Komori | 重磨皮 | job 404 | 約 4 | 地雷系本來就流行重磨皮、瓷娃娃感 |
| Nanami Fujiwara | 重磨皮 | job 253n | 約 5 | 現況；柔焦、溫柔感 |
| Rainie Hsu | 輕美肌 | 尚無定稿（形象照待出） | — | 夜店燈光下保留質感，和 Wendy、Vicky 同一級 |

prompt 寫法：
- **輕美肌**（已用在 Vicky 316～319）：`Skin finish: a light phone beauty filter only. Skin looks smooth, even and clean, but fine natural pores are still faintly visible on the cheeks, nose and forehead, like an iPhone photo with light retouching. Not airbrushed, not plastic, not waxy; no film grain and no noise.`
- **重磨皮**（PROPOSED，尚未單獨測試；Kanon 404、Nanami 253n 當時沒有寫皮膚描述）：`Skin finish: a strong beauty-camera filter. Flawless, porcelain-smooth, softly glowing skin with no visible pores, even tone, gentle soft-focus glow, like a Korean/Japanese beauty app selfie. Keep the face sharp: eyes, lashes, brows and lips stay crisp; no film grain and no noise.`

注意：
- 修改既有圖時，不要用 Nano Banana 去「加毛孔」，很容易加過頭，變成油光、斑點、顯老（Nanami 253s1 作廢，追加 46）。
- 以螢幕截圖當底圖時，要先處理網點，否則網點會被當成皮膚質感（Vicky 315～318，追加 46）。
- 新圖出完，臉頰細紋理值和該角色的依據定稿差太多（例如輕美肌低於 7 或高於 14、重磨皮高於 7），要在 REPORT 註記。

## 3. 與其他文件的關係

- `REPORT.md`「身材補充」：Vicky 那一列已被本檔取代，其餘有效。
- `REPORT.md` 追加 27：變更的原始紀錄。
- `ARCHETYPES_v2_2026-10-12.md`：十人個性類型，不含身材。
- 六人（Somi、Mia、Zhiyi、Yerin、Miu、Emma）身材仍未設定（製作師：之後再定）。
- 第五人 Rainie Hsu（2026-10-21 製作師選定，型錄夜生活／派對女王，Soul `Rainie Hsu v2`）：身材見 §1、美肌見 §2.5；prompt 身形描述待形象照定稿後補。

## 2.6 Nanami 的身形比例與 prompt 身形描述（2026-10-22，依線稿 v3 與正面定稿）

- 比例（頭高＝1）：身高 7.3 頭；肩關節寬 1.45（0.67×軀幹長 2.15）；髖關節寬 1.10；胸最寬 1.52（略寬於肩）；腰 0.92（0.6×臀）；臀最寬 1.54；髖關節離地 52%、胯下 47%；腿（髖→踝）3.50；大腿 1.62、小腿 1.88（小腿＝1.16×大腿）。線稿：執行者端 nsketch/nanami_proportion_sketch_v3.png（REPORT 追加 289）。
- 出圖對身形時：圖 2 放 `社群媒體/身形參考/nanami_body_front_job693e4809.jpg`（只當身形參考，不取衣服／背景）；prompt 身形描述：
  - 整體：`soft, curvy, voluptuous hourglass figure; not slim, not athletic`
  - 肩：`soft, narrow, slightly sloping feminine shoulders, narrower than the bust`
  - 胸：`very full, round, natural E-cup bust, projecting clearly forward, much wider than the waist`（不寫「heavy／頭大／深乳溝」，會被擋）
  - 腰臀：`small soft waist (about 0.6 of the hip width), strong hourglass; round, full, fleshy hips about as wide as the bust`
  - 腿：`long legs, hip joint at just over half her height; lower legs slightly longer than the thighs; soft full thighs tapering to slender calves and fine ankles`
  - 皮膚：重磨皮（§2.5）。
