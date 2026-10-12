# 先鋒四人形象照 v1（2026-10-12）

## 方向變更（製作師 2026-10-12）
- 原本的架構（3 主帳號＋7 流量帳號、導流 LUSCENA）與從它長出來的人設、語氣、題目庫，**全部降為備案**，檔案留在 `production/modeling_runs/2026-10-08_batch1/` 與 `production/content_pack_v1/`，不刪。
- 新方向：十個帳號全部走擦邊，以圖片與 10–15 秒短影片為主；每個人設個性鮮明、不重疊。臉沿用已做身分測試的十個 Soul，臉型不動，髮型可動。
- 十人個性類型（製作師 2026-10-12 確認名單）：1 Wendy Yeo 冷艷女上司／2 Kanon Komori 雙馬尾小惡魔萌妹／3 Vicky Lin 陽光體育系辣妹／4 Nanami Fujiwara 成熟溫柔少婦／5 Somi Oh 天然呆吃貨鄰家妹／6 Mia Huang 貓系撒嬌女友／7 Zhiyi Shen 腹黑眼鏡女秘書／8 Yerin Han 千金大小姐／9 Miu Shiraishi 清冷高嶺之花／10 Emma Kao 熟女御姐。
- 對照頁（型錄主圖＋新個性，私人連結）：https://claude.ai/artifact/DDGr1TcJd71ajSz9DNu1uT
- 底線：十人都是成年人；擦邊＝性感暗示，不露點、不透視、不做性行為暗示動作；守 Threads／Meta 規範與 Higgsfield NSFW 過濾。

## 先鋒四人（差距最大的四種：冷、萌、陽光、柔）

| # | 角色 | 類型 | 身高 | 三圍 | 體型 | 造型變更 |
|---|---|---|---|---|---|---|
| 1 | Wendy Yeo | 冷艷女上司 | 170 | 86/60/90 | 高挑骨感、肩線平、腿長 | 加粗黑方框眼鏡 |
| 2 | Kanon Komori | 雙馬尾小惡魔萌妹 | 155 | 84/58/86 | 嬌小、腰細 | 髮型改雙馬尾（粉髮保留）、小惡魔角髮箍 |
| 3 | Vicky Lin | 陽光體育系辣妹 | 168 | 88/63/92 | 運動型、肩寬、腹肌 | 不動 |
| 4 | Nanami Fujiwara | 成熟溫柔少婦 | 160 | 90/62/91 | 柔軟豐滿 | 年齡改 27；髮型放下微捲 |

三圍以身形描述寫進 prompt，不直接給數字。

## 生成紀錄
- 工具：Higgsfield MCP `generate_image_batch`；模型 `soul_2`（`text2image_soul_v2`），`aspect_ratio=3:4`、`quality=2k`，各附自己的 `soul_id`。無上傳參考圖。

| # | 角色 | job_id | 狀態 | 結果 |
|---|---|---|---|---|
| 201 | Wendy Yeo | `9d1a1d00-43b3-4c2e-a8d2-b92ea009494a` | completed | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_070950_9d1a1d00-43b3-4c2e-a8d2-b92ea009494a.png |
| 202 | Kanon Komori（第一版） | `3e9465b5-a951-4304-a4cb-47d2b9359e34` | **nsfw（被擋，已退點）** | — |
| 212 | Kanon Komori（改寫版） | `dd495b51-1361-474f-8a2a-ad750ff1933f` | completed | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_071403_dd495b51-1361-474f-8a2a-ad750ff1933f.png |
| 203 | Vicky Lin | `51dd9c69-e5f0-4a45-b3c4-d88e5a37a4c4` | completed | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_070952_51dd9c69-e5f0-4a45-b3c4-d88e5a37a4c4.png |
| 204 | Nanami Fujiwara | `fffad79b-2695-40cd-bf4d-8df063c17708` | completed | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_070952_fffad79b-2695-40cd-bf4d-8df063c17708.png |

### 花費
- 本批：5 次生成 × 0.12 − 1 次 NSFW 退點 0.12 ＝ **0.48 點**（交易紀錄 2026-10-12 07:09–07:14 UTC）。
- 餘額 3301.20（10/08 收尾）→ 3255.32（本批後）。差額 45.88 點中只有 0.48 是本批；其餘是 10/09–10/12 帳號上其他用途（Seed Audio、Nano Banana Pro），不是本專案生成。

### NSFW 被擋紀錄
- 202 第一版 prompt 含「跪坐在床上＋choker＋棒棒糖咬在嘴裡＋過膝襪」，被過濾。改寫版：坐床邊、棒棒糖拿手上、拿掉 choker、黑 T 恤＋百褶裙＋及膝襪，通過。
- 經驗：床＋口含物＋頸飾三者疊加容易觸發；拆開一兩項即可。

## prompt 全文

**201 Wendy**
```text
Editorial portrait of this woman as a cold, commanding female executive, 28 years old. Tall, long-legged, flat straight shoulders, slender build. Late night in a high-rise corner office, only one warm desk lamp on, city lights through the floor-to-ceiling window behind her. She sits in a leather executive chair, legs crossed, sheer black stockings, black stiletto pointing toward the camera. Fitted black blazer over a white shirt with the top two buttons undone. Thick black square-frame glasses. Silver-grey short hair slicked back. She holds a pen between two fingers over a document on the desk. Camera slightly below eye level, looking up at her; she looks down at the camera, chin slightly raised, lips closed, no smile. Warm lamp light on one side of her face, the other side in shadow. Realistic, unretouched skin texture, cinematic. No nudity, no see-through fabric. Avoid: smile, text, watermark, UI overlay, social media interface.
```
**212 Kanon（通過版）**
```text
Portrait of this woman as a mischievous, playful girl, 20 years old, clearly adult. Petite build. Pink hair tied in high twin tails. Small black devil-horn headband. Black fitted T-shirt and black pleated mini skirt, black knee-high socks. She sits on the edge of her bed, leaning forward slightly with both hands on the mattress; pink and purple LED strips glow behind her, a wall covered in stickers. A lollipop is held in one hand, not in her mouth. Expression: fake innocence, eyes wide looking at the camera, one corner of the mouth curled up like she just got caught doing something. Camera at eye level. Pink-purple side light, dark surroundings. Realistic photo, natural skin texture. Fully clothed, no cleavage, no see-through fabric. Avoid: school uniform, childlike face, text, watermark, UI overlay, social media interface.
```
**203 Vicky**
```text
Candid gym portrait of this woman as a sunny athletic girl, 25 years old. Athletic build, broad shoulders, visible abs, strong thighs, tanned skin. She just finished training, standing in front of a floor-to-ceiling gym mirror, afternoon sunlight slanting through the window. Black sports bra and high-waisted black shorts, a white towel around her neck that she is using to wipe her neck, a water bottle on the floor beside her. High ponytail, a few sweaty strands stuck to her forehead, sweat sheen on her skin. Expression: big open laugh showing her upper teeth, eyes squinting, as if someone behind the camera just told a joke. Natural side light, realistic unretouched skin. Avoid: posed modeling, text, watermark, UI overlay, social media interface.
```
**204 Nanami**
```text
Intimate portrait of this woman as a gentle, mature young wife, 27 years old. Soft, full-figured build, rounded shoulders, gentle curves. Evening in a Japanese ryokan tatami room, paper shoji door half open to a dark garden, warm paper-lantern light, very soft. She sits sideways at a low table pouring tea, pushing one cup toward the camera. Pale yukata loosened slightly at the collar showing her collarbone, obi tied loosely, as if she just came back from the hot spring. Hair down, softly wavy, tucked behind one ear, ends slightly damp. Expression: a faint gentle smile, eyes on the camera, patient, as if waiting for you to speak. Camera at eye level from the seat across the table, close distance. Realistic, natural skin texture, no added wrinkles. No nudity, no see-through fabric. Avoid: text, watermark, UI overlay, social media interface.
```

## 看圖結果（執行者判讀；由製作師定）

| # | 符合人設？ | 做到的 | 沒做到／要修 |
|---|---|---|---|
| 1 Wendy | 符合 | 黑框眼鏡、銀灰髮、翹腿絲襪、不笑、俯視、桌燈單側光、辦公室夜景 | 畫面有假社群介面（soul_2 通病） |
| 2 Kanon | 大致符合 | 粉色雙馬尾、惡魔角、黑 T＋短裙＋及膝襪、坐床邊、LED 燈、貼紙牆、裝無辜表情 | 棒棒糖還是叼在嘴裡（prompt 寫拿手上）；假介面；成年外觀要製作師再看一次 |
| 3 Vicky | 符合 | 運動內衣＋短褲、毛巾、腹肌、汗、大笑露齒、鏡前、斜射陽光 | 假介面 |
| 4 Nanami | 大致符合 | 浴衣鬆領露鎖骨、倒茶推杯、淺笑、紙燈籠暖光、紙門庭院 | **髮型沒放下**（還是盤起）；畫面中間有假文字；領口開得比預期多，要不要收由製作師定 |

共通：`soul_2` 自動加假社群介面與假文字。定稿前要處理：(a) 換支援 Soul 的另一個模型 `soul_cinematic` 試一次；(b) 或生成後裁切／修圖。

## 下一步（等製作師）
1. 四張哪幾張可以定稿、哪幾張要重出（Nanami 髮型、Kanon 棒棒糖）。
2. 假介面的處理方式。
3. 定稿後：每人 2–3 個短影片動作 motif 與 10–15 秒腳本。

## 追加（2026-10-12，製作師回饋後）

- 製作師：#4 Nanami 可用（假文字為 soul_2 假浮水印，定稿裁切）；#3 Vicky 改成瑜伽褲空中瑜伽、曲線更明顯；#1、#2 待製作師提供參考圖再修。
- **213 Vicky 空中瑜伽**：job `6e71f97e-bda2-4884-ba59-f99acec2f3c5`，completed，0.12 點。結果：https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_072032_6e71f97e-bda2-4884-ba59-f99acec2f3c5.png
  - 做到：白色吊床倒掛後彎、深色瑜伽褲＋運動內衣、腰臀腿曲線、閉眼微笑、午後窗光。
  - 沒做到：臉是側面倒掛，辨識度低（身分特徵看不清）；假介面仍在（上下各一條）。
  - 建議：當「身材照」用可以；當頭像或代表照要再出一張臉朝鏡頭的體式（例如吊床坐姿劈腿、或後彎時臉轉向鏡頭）。
- prompt：
```text
Full-body photo of this woman practicing aerial yoga, 25 years old, athletic and curvy build, defined waist, full hips and strong thighs, tanned skin. A bright high-ceiling yoga studio, white aerial silk hammock, soft afternoon window light. Dark high-waisted yoga leggings and a matching dark sports bra, fitted to show her figure. She hangs in an inverted backbend: the hammock wrapped around her hips and thighs, back arched, head tilted back, one arm reaching toward the floor, legs extended in a graceful line. High ponytail falling down. Expression: eyes closed, a relaxed soft smile, effortless. Camera at mid height from the side, slightly low, showing the full curve of her back and hips. Natural light, realistic unretouched skin, subtle sweat sheen. Fully clothed athletic wear, no nudity, no see-through fabric. Avoid: text, watermark, UI overlay, social media interface, extra limbs.
```
- 本批累計：0.60 點。

## 追加 2（2026-10-12）：風格與 Nanami 重寫

- 製作師：整體太寫實，要「美顏相機感」（皮膚滑、柔焦、暖粉）；之後 prompt 拿掉 unretouched／natural skin texture。
- 製作師要求之後改用 Seedream。查證：Soul 只綁 soul_2／soul_cinematic；Seedream 要改用 Element（帳號裡十人都已有 Element，含 face-only 版）。價格：Seedream 4.5 與 5.0 Lite 各 1 點／張、5.0 Pro 2.5 點／張（soul_2 為 0.12）。**尚未切換，等製作師決定。**
- 製作師確認十人類型 v2 後，先鋒四人：Wendy、Kanon（地雷系）、Vicky（空中瑜伽）、Nanami。

### Nanami 餐桌餵食（三版，都用 soul_2）
| job | 要求 | 結果 |
|---|---|---|
| 214 `7df501ab-7d17-4bf6-a61c-2161a2a5e53b` | 居家餐桌、筷子餵鏡頭、嘴「啊」、美顏感 | 動作有、嘴張太大像驚訝；背景仍偏日式（榻榻米）；偏糊 |
| 215 `54a8849b-acfb-4be4-a93e-ca28aee93f35` | 清晰、台式公寓、筷子向前、眼瞇帶笑 | 清晰、公寓背景對；筷子沒伸向鏡頭；露齒笑非「啊」；頭髮沒放下微捲 |
| 216 `20e0a6dd-2072-4f1e-a2e6-ad30cf8ce186` | 俯角露上圍、細肩帶無袖、背景減雜物、手直伸到鏡頭、另一手接、眼瞇嘴「啊」 | 俯角＋上圍＋細肩帶＋手直伸到鏡頭：對。左手沒放筷子下方；眼睛沒瞇、嘴閉著；背景仍有烤箱與榻榻米 |

- 觀察：這個 Soul 對「榻榻米」有偏好（訓練圖應該多在旅館），三版都自己加；soul_2 對「嘴型」與「另一手位置」的指令跟隨弱。換 Seedream＋Element 可能改善，待測。
- 每張 0.12 點；本批累計 0.96 點（含 NSFW 退點後）。

## 追加 3（2026-10-12）：Seedream 4.5 ＋ Element 對照

- 製作師同意測一張。模型 `seedream_v4_5`（quality basic），prompt 開頭放 `<<<03dccd7d-7193-432a-8827-7919…>>>`（Nanami 的 Element `nanami-fujiwara-soul-v1-5img-20260904`，id `03dccd7d-7193-432a-8827-3f518ffc1cff`），其餘 prompt 與 soul_2 第 3 版相同。
- job `c3a8cce7-5e81-44b2-b6cd-ac6fa1aa4dab`，completed，1 點，輸出 1728×2304。結果：https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_075731_c3a8cce7-5e81-44b2-b6cd-ac6fa1aa4dab.png
- 餘額 3255.32 → 3253.84（1.48 ＝ Seedream 1 ＋ soul_2 四張 0.48）。本批累計 1.96 點。

| 項目 | soul_2 第 3 版（0.12） | Seedream 4.5＋Element（1.0） |
|---|---|---|
| 臉像不像 | 很像（Soul 多張訓練） | 像七成：輪廓與眼神接近，臉頰更圓、眼型略不同，偏「通用美女」 |
| 榻榻米／日式 | 又出現 | **沒有**：白牆、白磁磚 |
| 俯角、露上圍、細肩帶 | 對 | 對 |
| 手直伸到鏡頭 | 對 | 對 |
| 另一手在筷子下方 | 沒有 | **有** |
| 眼微瞇 | 沒有 | 沒有 |
| 嘴「啊」 | 閉嘴笑 | 微張、小「啊」 |
| 假社群介面 | 有 | **沒有** |
| 清晰度 | 2k | 4K 級，更銳利 |

- 結論：Seedream 指令跟隨與畫質明顯好、沒有假介面、沒有榻榻米；代價是臉的精準度下降、價格 8 倍。
- 下一步建議：用 Seedream 當正式出圖模型，身分靠「Element ＋ 多張參考圖」補強——把各人 soul_2 身分測試的正面照（job id）一起放進 `image_references`，看臉能不能拉回來。

## 追加 4（2026-10-12）：純文字生圖驗 prompt（不用 Soul／Element）

- 製作師要求：先不用角色建模，純 t2i 在 Seedream 與 GPT 各出一張，驗「餵鏡頭」prompt 本身對不對。
- prompt 依 `REFS_FEEDING_POV_2026-10-12.md` §D 的公式寫：POV、鏡頭略高俯 30°、右手直伸到鏡頭、筷子夾菜在前景、左手在筷子下接、眼瞇帶笑、嘴小「啊」、台式公寓餐桌、細肩帶背心、美顏感。

| job | 模型 | 狀態 | 結果 |
|---|---|---|---|
| 401 `f45039f6-367e-4957-8fbf-4dfb28577db0` | seedream_v4_5 basic | completed（1 點） | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_082439_f45039f6-367e-4957-8fbf-4dfb28577db0.png |
| 402 `e22a4a0e-b790-4976-9874-1816ed7775f7` | gpt_image_2 high 1k | **nsfw（被擋）** | — |
| 403 `8659ca6b-1454-4df4-a310-dfaa6e601af7` | gpt_image_2 high 1k，拿掉 cleavage／prominent bust 字眼 | **nsfw（仍被擋）** | — |

- Seedream 401 看圖：POV 成立；右手直伸到鏡頭、筷子夾菜佔前景、左手掌心朝上在下方接、眼睛瞇、暖色美顏感、白牆白磁磚、細肩帶背心——都對。沒對的：嘴是露齒笑不是「啊」；鏡頭偏低（略仰）不是俯 30°；前景手部透視極端、筷子握法怪；牆上有粉紅色光。
- GPT Image 2 兩次都被 NSFW 擋（第二次已把身材字眼拿掉仍擋），這個「細肩帶＋餵食 POV＋美顏」的概念在 GPT 上過不了；要驗 GPT 得把衣服改成完全保守（T 恤），但那就不是同一張圖。
- 結論：prompt 在 Seedream 上成立，可以進入「加 Element 維持身分」的階段；GPT 不適合這條線。

## 追加 5（2026-10-12）：Nanami 餵食 第 4 版（soul_2）

- 製作師提供一張 photoAC 浮水印參考圖（真人，戴兔耳連帽衣、用湯匙把食物送向鏡頭、嘴張圓「啊」）。**只取手與嘴型，轉成文字描述；圖片未下載、未放進生成。**（登記補進 `REFS_FEEDING_POV_2026-10-12.md` B 類：付費／授權圖只看不用。）
- 製作師指示：改回 soul_2（Seedream 太廣角）；桌上食物再豐盛一點。
- job 217 `c55ea75e-41a3-448e-93c1-6898551f6b7c`，`soul_2` 2k，0.12 點。結果：https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_083125_c55ea75e-41a3-448e-93c1-6898551f6b7c.png
- 看圖：嘴圓「啊」、上排牙微露 ✅；右手拿筷子把五花肉送向鏡頭、手不誇張 ✅；50mm 無廣角 ✅；桌上五道菜 ✅；頭髮放下微捲 ✅（前三版都沒做到）；細肩帶低領 ✅；臉是 Nanami ✅。沒做到：左手放在桌上沒接筷子；右側仍有廚房爐具；假社群介面照舊。
- 目前四版中最接近定稿。
- 本批累計（含退點）：soul_2 7 張 0.84 ＋ Seedream 2 張 2.0 ＝ **2.84 點**。

## 追加 6（2026-10-12）：Nanami 餵食 第 5 版（soul_2）

- 製作師要求：補左手在筷子下方、右手像參考圖伸直、眼睛微瞇。
- job 218 `6ed76f6b-0059-45b3-a17a-e272175ae5b3`，`soul_2` 2k，0.12 點。結果：https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_083541_6ed76f6b-0059-45b3-a17a-e272175ae5b3.png
- 看圖：嘴「啊」✅、桌菜✅、臉✅；**左手舉起但在肩旁，沒在筷子下**；右臂彎曲在畫面左上，沒伸直向鏡頭；眼睛大睜沒瞇；背景右側爐具、洗衣機又出現。整體比第 4 版退步。
- 結論：soul_2 連續五版都做不到「左手接筷子下方」「眼微瞇」這兩個細節，再抽只是碰運氣。
- 建議改走「以第 4 版為底做局部修改」：用 Seedream 4.5 的 image_references 把第 4 版（job c55ea75e）當輸入，指令只改左手位置與眼神，臉和其餘畫面沿用，1 點。這樣臉是 Soul 的、細節是 Seedream 改的。
- 本批累計 2.96 點。

## 定稿（2026-10-12，製作師決定）

- **Nanami Fujiwara（成熟溫柔少婦）形象照 v1 定稿：第 5 版**，job `6ed76f6b-0059-45b3-a17a-e272175ae5b3`（`soul_2`，2k，1536×2048）。
  https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_083541_6ed76f6b-0059-45b3-a17a-e272175ae5b3.png
- 製作師接受此版（左手未在筷子下、眼未瞇、背景有家電），不再修。
- 已知待處理：soul_2 的假社群介面需裁切後才能發布。
- 身分參考圖 A（臉）仍以 `2026-10-08_batch1` 的 Soul 為準；本張為第一張定稿形象照。

### 先鋒四人狀態
| 角色 | 狀態 |
|---|---|
| Nanami | **定稿 v1（job 6ed76f6b）** |
| Vicky | 空中瑜伽版（job 6e71f97e）待定；是否補臉朝鏡頭版未決 |
| Wendy | 第一版（job 9d1a1d00）待製作師參考圖後修 |
| Kanon | 小惡魔版作廢；地雷系版待出 |

## 身材補充（2026-10-12）

四人罩杯（亞洲尺碼，胸圍減下胸圍推算；數字只寫進文件，prompt 用身形描述）：

| 角色 | 身高 | 上圍／下胸圍 | 罩杯 |
|---|---|---|---|
| Wendy Yeo | 170 | 86／72 | C（70C） |
| Kanon Komori | 155 | 84／68 | D（65D） |
| Vicky Lin | 168 | 88／74 | C（75C） |
| Nanami Fujiwara | 160 | 90／70 | E（70E） |

- 十人裡目前沒有「巨乳小隻馬」。執行者提案 Mia Huang（152、65G）或 Somi Oh（156、F）；**製作師：先鋒四人以外的身材之後再決定，暫不定。**

## 追加 7（2026-10-12）：Wendy 第 2 版（依製作師參考圖）

- 製作師提供一張「高傲女上司」參考圖（真人：極低角度仰拍、翹腿、高跟鞋紅底往鏡頭送、無袖高領合身上衣、短裙、絲襪、手撐太陽穴、紅唇、俯視）。**只轉成文字描述，圖片不進生成。**
- job 221 `62cc9212-b3f4-4707-a1a1-6d97b947679a`，`soul_2` 2k，0.12 點。結果：https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_084315_62cc9212-b3f4-4707-a1a1-6d97b947679a.png
- 看圖：低角度 ✅、翹腿 ✅、紅底高跟鞋在前景 ✅、無袖深藍高領 ✅、灰短裙 ✅、手撐太陽穴 ✅、黑框眼鏡 ✅、銀灰短髮 ✅、鍊帶包 ✅、辦公室磁磚地 ✅、俯視不笑 ✅。和參考不同：沒有絲襪（光腿）；鞋穿在腳上沒有勾著晃；眼神偏淡不夠「輕蔑」；假社群介面照舊。
- 本批累計 3.08 點。

## 追加 8（2026-10-12）：Wendy 第 3 版

- 製作師要求：一定要黑絲襪；白襯衫、胸口微開露一點；角度更低（快看到內褲的感覺，但不露）；辦公室；不要包。
- job 222 `3e4426a0-89a1-4215-b653-6a1ce91b5f79`，`soul_2` 2k，0.12 點。結果：https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_084728_3e4426a0-89a1-4215-b653-6a1ce91b5f79.png
- 看圖：黑絲襪 ✅、白襯衫解三顆露乳溝 ✅、黑鉛筆裙 ✅、翹腿 ✅、黑框眼鏡／銀灰髮 ✅、辦公室（玻璃隔間、辦公桌）✅、手撐太陽穴 ✅。沒做到：**包包又出現**（prompt 寫 avoid handbag 仍出現）；角度只比第 2 版低一點，不到「快看到裙底」；鞋沒往鏡頭送；嘴角微微有笑意；假介面照舊。
- 本批累計 3.20 點。

## 追加 9（2026-10-12）：Wendy 用「自家生成的姿勢圖」當參考，兩條路並排

- 製作師要求：角度更低（盡量仿參考圖）、拿掉包包、主管辦公室、腿部肌肉紋理不要明顯；Soul 能不能給參考圖模仿——兩條路都跑。
- 規則：製作師提供的真人參考圖不進生成；改用**自家純文字生成的姿勢圖**當參考（本專案生成，權利清楚）。
- 另：依製作師要求新增 `.claude/settings.json` 允許清單（Higgsfield 工具、curl、python3、git），之後 session 不再逐一詢問。

| job | 路線 | 模型／輸入 | 扣點 | 結果 |
|---|---|---|---|---|
| 501 `f898b8e2-b6c6-4b46-b176-1fe9bbe5e28e` | 姿勢圖 | seedream_v4_5 純文字（無身分） | 1 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_085118_f898b8e2-b6c6-4b46-b176-1fe9bbe5e28e.png |
| 223 `00c5551c-679c-468f-8a8f-0e75e6b569f0` | A | soul_2 ＋ Wendy Soul ＋ 姿勢圖（medias image ×1） | 0.12 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_085227_00c5551c-679c-468f-8a8f-0e75e6b569f0.png |
| 224 `9c56f81e-9ff9-49ca-a758-f144ef4fb8b6` | B | seedream_v4_5 ＋ Wendy face-only Element `19f44c28-fb6b-45e1-bd13-6b88a5223dd8` ＋ 姿勢圖（image_references） | 1 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_085234_9c56f81e-9ff9-49ca-a758-f144ef4fb8b6.png |

- 姿勢圖本身：貼地仰角、鞋勾著往鏡頭、黑絲襪、白襯衫、主管辦公室夜景、無包、腿平滑——構圖已達標。
- **A 路（soul_2＋參考圖）失敗**：畫面與服裝抄了參考圖，但臉變成參考圖那位（黑長髮、無眼鏡），Soul 身分與「銀灰短髮、黑框眼鏡」的 prompt 都被參考圖蓋掉。證實 Soul 附參考圖時 prompt 與身分會失效。
- **B 路（Seedream＋Element＋參考圖）成功**：構圖幾乎等於姿勢圖（極低角度、鞋在前景、黑絲襪、白襯衫、無包、辦公室夜景、腿平滑），且銀灰短髮＋黑框眼鏡＋紅唇都在。臉在畫面裡小，身分精準度待放大核對。
- 結論：之後「要照參考圖構圖」的需求走 B 路；「不需要參考圖」的走 soul_2。
- 本批累計 5.32 點。

## 追加 10（2026-10-12）：Wendy 兩個髮型版本（以製作師選的構圖為底）

- 製作師選中的是 A 路那張（job 223：黑長直、無眼鏡、構圖最好），要求：拿掉腳上金鍊與青筋、肌肉紋理不要明顯（美肌）；再多露一點（胸口、裙下）；眼鏡加回；髮色做兩版比較（銀灰短髮 vs 黑長直）。
- 做法：Seedream 4.5，image_references ＝ job 223 當底圖，prompt 放 Wendy face-only Element，只改指定項目。各 1 點。

| job | 版本 | 結果 |
|---|---|---|
| 225 544d45d7-cafb-46aa-9aa7-32e31f541b59 | 銀灰短髮＋眼鏡 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_090015_544d45d7-cafb-46aa-9aa7-32e31f541b59.png |
| 226 894ee9e9-d3b2-46e2-a0f4-43e2247f785d | 黑長直＋眼鏡 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_090015_894ee9e9-d3b2-46e2-a0f4-43e2247f785d.png |

- 看圖：兩版都做到：眼鏡、無金鍊、腿平滑無青筋、胸口多開一顆、裙上移露出蕾絲襪口、內褲藏在陰影、鞋在前景、冷眼俯視。臉：銀髮版較接近 Wendy 身分照；黑長直版臉略長。
- 餘額 3253.84 → 3248.24；本批累計 7.32 點。版本由製作師選。

## 追加 11（2026-10-12）：Wendy 銀灰髮版放下頭髮＋兩種手勢

- 製作師選中銀灰短髮版（job 225）的構圖，要求：頭髮放下來、不要盤起；手勢改成「手放胸口」或「像在辱罵下屬」；表情再更高傲；腿的肌肉紋理再更美肌。
- 做法：Seedream 4.5，image_references ＝ job 225 當底圖，prompt 放 Wendy face-only Element `19f44c28-fb6b-45e1-bd13-6b88a5223dd8`，只改髮型、手勢、表情、腿。3:4、basic，各 1 點。
- prompt（227；228 只把手勢那句換成 `her right hand rests flat on her chest just below the collarbone with fingers spread, drawing the eye to her open collar`）：

```
<<<19f44c28-fb6b-45e1-bd13-6b88a5223dd8>>> is the woman's face. Keep the reference image's composition, extreme low camera angle, crossed legs with the stiletto in the foreground, office at night, white shirt with cleavage, short black skirt with the lace tops of her sheer black stockings showing, thick black square-frame glasses, red lips. Change only these: her silver-grey hair is worn down and loose, a chin-length layered bob falling around her face, not slicked back, not tied; her right hand is raised with the index finger pointing down at the camera as if scolding a subordinate, her left hand rests on the armrest; her expression is more arrogant and contemptuous: chin raised high, eyes half-lidded looking down her nose at the camera, lips closed with a faint sneer; her legs are completely smooth and soft with an even beauty-filter finish, no veins, no muscle definition, no texture through the stockings; smooth glowing skin everywhere. No handbag, no anklet. Sharp, in focus. No nudity, no see-through fabric, no underwear visible. Avoid: hair tied or slicked back, smile, veins, muscular legs, anklet, handbag, text, watermark.
```

| job | 手勢 | 結果 |
|---|---|---|
| 227 `7b475d71-6b7b-4968-8271-527174c84862` | 右手食指朝鏡頭往下指（辱罵下屬） | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_090602_7b475d71-6b7b-4968-8271-527174c84862.png |
| 228 `ac63e50a-09f9-45e0-8e42-0b76f14c2da2` | 右手平放胸口（鎖骨下方，紅指甲） | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_090603_ac63e50a-09f9-45e0-8e42-0b76f14c2da2.png |

- 看圖：兩張都做到：頭髮放下（銀灰、及下巴的層次短髮）、黑框眼鏡、白襯衫開領露乳溝、極低角度翹腿、鞋在前景、腿平滑無青筋、表情比 225 高傲（下巴抬高、嘴角輕蔑）。**跑掉的地方：黑絲襪沒了**——227 變成白色／極淡的絲襪，228 變成膚色絲襪，兩張都只剩黑蕾絲襪口。推測是 prompt 裡「no texture through the stockings、completely smooth」被模型理解成把黑絲去掉。「高傲」程度中等，還不到冷笑輕蔑。
- 處理：以 227、228 各自當底圖再修一次，prompt 只改「黑色透膚絲襪＋黑蕾絲襪口，從襪口到鞋內都是黑絲」，其他全部保留（見追加 12）。
- 餘額 3248.24 → 3246.24；本批累計 9.32 點。

### 製作師問：Seedream 是不是比單純用 Soul 更能接受參考圖？

- 是。依追加 9 的並排測試：`soul_2`＋Soul＋參考圖（job 223）會把參考圖的人臉與服裝整個抄過來，Soul 身分和 prompt 裡的銀髮、眼鏡全部失效；Seedream 4.5＋`image_references`（job 224、225–228）幾乎照抄構圖，臉靠 face-only Element 撐住（約七成像，臉小時要放大核對）。
- 分工：要照參考圖構圖、或要在既有圖上做局部修改 → Seedream 4.5＋Element＋image_references（1 點／張）；不需要參考圖、只要本人 → `soul_2`＋soul_id（0.12 點／張，身分最準，但細節指令常不聽、會加假社群介面）。

## 追加 12（2026-10-12）：Wendy 兩種手勢補回黑絲襪

- 目的：修正追加 11 跑掉的黑絲襪（製作師在追加 8 的硬性要求），其他全部保留。
- 做法：Seedream 4.5，image_references 分別 ＝ job 227、job 228（各自當底圖），prompt 放 Wendy face-only Element，指令只改絲襪。3:4、basic，各 1 點。
- prompt（229；230 的手勢句改為 `the right hand resting flat on her chest just below the collarbone with fingers spread`，並多寫 `red nails`）：

```
<<<19f44c28-fb6b-45e1-bd13-6b88a5223dd8>>> is the woman's face. Keep the reference image exactly as it is: same composition, extreme low camera angle, crossed legs with the black stiletto in the foreground, office at night with city lights, white shirt open at the collar with cleavage, short black skirt, thick black square-frame glasses, red lips, silver-grey hair worn down in a loose chin-length layered bob, the right hand raised with the index finger pointing down at the camera as if scolding a subordinate, the left hand on the armrest, the same arrogant expression with chin raised and a faint sneer. Change only one thing: she is wearing sheer black nylon thigh-high stockings with black lace tops; the black sheer covers both legs from the lace tops all the way down to her feet inside the black stilettos; the legs under the black sheer are completely smooth and glossy with an even beauty-filter finish, no veins, no muscle definition. No nudity, no underwear visible. Sharp, in focus. Avoid: white stockings, nude-colored stockings, bare legs, veins, muscular legs, handbag, anklet, text, watermark.
```

| job | 手勢 | 底圖 | 結果 |
|---|---|---|---|
| 229 `4659f3ca-4f88-40a5-87a8-1515c388345a` | 右手食指朝鏡頭往下指（辱罵下屬） | job 227 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_091230_4659f3ca-4f88-40a5-87a8-1515c388345a.png |
| 230 `d5520708-61a4-4d07-9fcf-eb516befd8c9` | 右手平放胸口（鎖骨下方，紅指甲） | job 228 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_091234_d5520708-61a4-4d07-9fcf-eb516befd8c9.png |

- 看圖：兩張黑色透膚絲襪＋黑蕾絲襪口都回來了，從襪口到鞋內都是黑絲；腿平滑無青筋；頭髮放下、黑框眼鏡、白襯衫開領、極低角度、鞋在前景、辦公室夜景都與 227／228 一致。229 的指人手勢比 227 更往前伸向鏡頭，仍是食指朝下；230 除絲襪外與 228 幾乎相同。表情維持追加 11 的程度（下巴抬、嘴角輕蔑），沒有再加強。
- 經驗：要保留絲襪時，prompt 不能寫「no texture through the stockings」這類會被當成「去掉絲襪」的句子；改寫成「the legs under the black sheer are smooth」才穩。
- 餘額 3246.24 → 3244.24；本批累計 11.32 點。

### 先鋒四人狀態（追加 12 後）

| 角色 | 狀態 |
|---|---|
| Nanami | 定稿 v1（job 6ed76f6b） |
| Vicky | 空中瑜伽版（job 6e71f97e）待定；是否補臉朝鏡頭版未決 |
| Wendy | **候選定稿：job 229（指責下屬）／job 230（手放胸口），由製作師選手勢**；表情是否再加強待製作師 |
| Kanon | 小惡魔版作廢；地雷系版待出 |

## 追加 13（2026-10-12）：Wendy 依製作師第二張參考圖改手、腳、表情

- 製作師提供第二張「女上司」參考圖（真人照：坐辦公椅、右手撐太陽穴、左臂放扶手、一腿伸直向鏡頭、黑絲、高跟鞋從腳跟滑落掛在腳尖、紅唇、俯視冷淡）。要求：手、腳、表情照參考；襯衫開口與扣子維持 229／230 現狀。**圖片只轉成文字，不進生成**（真人、權利不明；依 2026-10-08 交接規則：權利不清或真人的參考圖不進生成與訓練）。
- 製作師指示：之後固定用 Seedream 4.5＋Wendy face-only Element（製作師稱「Seedream 加 Soul」），做完臉跑掉再細修。
- 做法：Seedream 4.5，image_references 分別 ＝ job 229、230 當底圖，prompt 放 Element，只改姿勢與表情。3:4、basic，各 1 點。
- prompt（231；232 相同，只多寫 `red nails`）：

```
<<<19f44c28-fb6b-45e1-bd13-6b88a5223dd8>>> is the woman's face. Keep the reference image: the same woman, the same office at night with the desk lamp and city lights, the same white shirt with its collar open exactly as it is now (the same buttons undone, the same amount of cleavage, do not change the shirt), the same short black skirt, the same sheer black thigh-high stockings with black lace tops, the same black stilettos, the same silver-grey hair worn down in a loose chin-length bob, the same thick black square-frame glasses, the same red lips, the same extreme low camera angle from the floor. Change only her pose and her expression: she leans back in the office chair with her right elbow on the armrest and her right hand raised to her temple, index and middle fingers resting against the side of her head; her left forearm lies along the other armrest with the hand hanging relaxed over its end; her right leg is extended straight toward the camera so her foot in the sheer black stocking fills the lower-left foreground, the black stiletto slipped off her heel and dangling from her toes; her left leg is crossed underneath, that foot still in its stiletto. Her expression is cold, bored contempt: head tilted slightly to the side, chin up, eyes narrowed looking down her nose at the camera, red lips closed, no smile. Legs smooth and glossy under the black sheer, no veins, no muscle definition. No nudity, no underwear visible. Sharp, in focus. Avoid: smile, pointing finger, hand on chest, both shoes fully on, bare legs, shirt buttoned differently, handbag, anklet, text, watermark.
```

| job | 底圖 | 結果 |
|---|---|---|
| 231 `ca65f299-b7a7-4323-add2-3efcc0df7583` | job 229 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_091726_ca65f299-b7a7-4323-add2-3efcc0df7583.png |
| 232 `f130c333-387e-40cd-ace2-bbc483c23db1` | job 230 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_091731_f130c333-387e-40cd-ace2-bbc483c23db1.png |

- 看圖：**231 達標**——右手撐太陽穴（指尖在鏡腳旁）、左臂沿扶手垂放、右腿伸直向鏡頭、高跟鞋從腳跟滑落掛在腳尖、黑絲＋蕾絲襪口、襯衫開口與扣子同 229、銀灰髮放下、黑框眼鏡、表情冷淡帶輕蔑。**232 失敗**——黑絲又變膚色、椅側多出黑色包包、鞋穿在腳上沒有掛著；表情雖更仰更傲，整體不合格。
- 經驗：以 230（手放胸口）為底做大幅改姿勢，模型容易連配件一起改掉；之後改姿勢一律以 229／231 這條線為底圖。
- 候選定稿改為 **job 231**（取代追加 12 的 229／230 手勢選擇），待製作師確認；表情要更輕蔑可再修一輪。
- 餘額 3244.24 → 3242.24；本批累計 13.32 點。

### 製作師問：用 Seedream 為什麼不把參考圖直接放進去？

- Seedream 技術上可以收參考圖（image_references，追加 9 已證實）。沒放是因為這張是真人照片、權利不明：交接規則是「權利不清或真人的參考圖不進生成與訓練」，也避免觸及 Higgsfield 對真人肖像的條款。
- 替代做法（追加 9 用過）：把參考圖轉成文字，先用純文字生成一張自家姿勢圖（無身分、權利清楚，1 點），再把它當 image_references 餵給 Seedream＋Element。這次純文字直接改就達標，沒多花這一步；之後若文字改不到位，就補這一步。
- 若製作師要改這條規則（例如確認照片是自家拍攝、模特兒已同意），請明說；我會把決定與依據寫進報告後再執行。

### 權限提示（製作師再問）

- 允許清單在 `.claude/settings.json`（commit 6675c99 起，本次再補 git fetch／pull／branch／ls-remote／show、curl、head、tail、find、cut、echo、sort、file、du）。雲端 session 只在開始時讀這個檔，所以本 session 仍會問；**從 `producer/modeling-r1` 分支新開 session 才生效**（main 上沒有這個檔）。
- 模式選單選「自動」提示最少；「接受編輯」只免問檔案修改。

## 追加 14（2026-10-12）：製作師決定把真人參考圖直接餵進 Seedream；以 231 為底改腿腳與眼神

### 決定紀錄
- 製作師指示（原話）：「你不要自己擋，你把權限都交給 Higgsfield。」即：參考圖是否能用由平台把關，執行者不再依「真人／權利不清的參考圖不進生成」自行攔下。此決定由製作師做出，執行者已說明該規則來源與風險（追加 13）。
- 參考圖登記：`wendy_ref2_producer.png`（318×466，製作師 2026-10-12 提供的真人照，來源與權利不明），上傳 Higgsfield media `e960969a-31ce-4ee7-84bb-8310a5008742`，只作姿勢／眼神參考，臉由 Wendy face-only Element 取代。平台未拒絕上傳與生成。圖檔不進 repo。
- 製作師要求：以 231 為底；腿腳姿勢要與參考圖一樣；眼神往下、往正前方，等於往前下方俯視。

### 第 1 輪：233／234（231 ＋ 真人照，count 2，各 1 點）
- medias：image_references ＝ job 231（底圖）、media e960969a（姿勢參考）。
- prompt：

```
<<<19f44c28-fb6b-45e1-bd13-6b88a5223dd8>>> is the woman's face. The first reference image is the base: keep it as it is: the same woman, her silver-grey hair worn down in a loose chin-length bob, thick black square-frame glasses, red lips, the white shirt with its collar open exactly as it is (the same buttons undone, the same cleavage, do not change the shirt), the short black skirt, the sheer black thigh-high stockings with black lace tops, the black stilettos, her right hand raised to her temple with the elbow on the armrest, her left arm resting on the other armrest, the office at night with the desk lamp and city lights, the same extreme low camera angle from the floor. The second reference image is only a pose reference: copy from it exactly the position of her legs and feet: which leg is extended straight toward the camera, the angle of that leg, the foot in the sheer black stocking pointed at the camera in the lower-left foreground with the black stiletto slipped off her heel and hanging from her toes, and the position of the other leg and foot; and copy its gaze: her eyes cast downward, looking straight ahead and down at the camera below her, eyelids lowered, cold and bored, head upright and facing forward, not tilted. Do not copy the second image's face, clothes, chair or room. Legs smooth and glossy under the black sheer, no veins, no muscle definition. No nudity, no underwear visible. Sharp, in focus. Avoid: smile, eyes looking up or to the side, head tilted, both shoes fully on the feet, bare legs, nude stockings, shirt buttoned differently, handbag, text, watermark.
```

| job | 結果 |
|---|---|
| 233 `580fa048-7af9-40f2-961d-9f8145d2a797` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_092941_580fa048-7af9-40f2-961d-9f8145d2a797.png |
| 234 `8f854570-872a-476f-bf4f-3bbeff27949a` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_092941_8f854570-872a-476f-bf4f-3bbeff27949a.png |

- 看圖：腿伸直向鏡頭、腳底朝鏡頭 ✅；但**眼睛閉成一條線**、**鞋子整隻掉在地上**（234 還多一條金鍊）；而且把參考圖的灰色扶手椅、磁磚地、桌邊包包、**底部浮水印文字**一起抄過來。製作師看圖回饋：眼睛變閉起來、鞋子跑掉，鞋要「一半套在上面」。

### 第 2 輪：235／236（233 ＋ 真人照，count 2，各 1 點）
- 只改兩處：眼睛睜開、視線往前下方看鏡頭；鞋半套在腳尖。prompt 另要求去包包、去底部文字。

```
<<<19f44c28-fb6b-45e1-bd13-6b88a5223dd8>>> is the woman's face. The first reference image is the base: keep it as it is: the same woman, her silver-grey hair worn down, thick black square-frame glasses, red lips, the white shirt with its collar open exactly as it is (the same buttons undone, do not change the shirt), the short black skirt, the sheer black thigh-high stockings with lace tops, her right hand raised to her temple, her left hand resting on the armrest, the chair, the room, the night window, the desk lamp, the same extreme low camera angle, her right leg extended straight at the camera with the stockinged foot large in the lower-left foreground, her left foot in its black stiletto on the floor. Change only two things, using the second reference image as the guide for both: (1) her eyes are open with the irises clearly visible, gaze lowered, looking straight ahead and down at the camera below her, eyelids relaxed, not closed, not squinting, a cold bored look, lips closed; (2) the black stiletto of the extended right foot is half on: her toes are still inside the front of the shoe, the heel of her foot has slipped out of the back, and the shoe hangs tilted downward from her toes with its stiletto heel pointing at the floor; the shoe is not lying on the floor and not fully on. No handbag or bag anywhere, no chain, no text or caption anywhere in the image. Legs smooth under the black sheer, no veins. No nudity, no underwear visible. Sharp, in focus. Avoid: closed eyes, squinting, smile, shoe lying on the floor, shoe fully on the foot, bare feet without stockings, bag, chain, text, watermark.
```

| job | 結果 |
|---|---|
| 235 `d7b97fde-ec8a-4f5d-b391-82bdc2bf88cc` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_093311_d7b97fde-ec8a-4f5d-b391-82bdc2bf88cc.png |
| 236 `aa0112c7-3de3-4a70-b135-2cd057f2a9ec` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_093311_aa0112c7-3de3-4a70-b135-2cd057f2a9ec.png |

- 看圖：眼睛睜開、往前下方看 ✅；**鞋仍在地上**（236 翻倒）；只要真人照還在 medias 裡，底部浮水印文字和包包就一直被抄回來。

### 第 3 輪：237／238（235 為底，不再附真人照，count 2，各 1 點）
- 只用文字描述「鞋從腳跟滑出、掛在腳尖、鞋跟朝下懸空」，並要求去包包、去底部文字。

```
<<<19f44c28-fb6b-45e1-bd13-6b88a5223dd8>>> is the woman's face. Keep the reference image as it is: the same woman, her silver-grey hair worn down, thick black square-frame glasses, red lips, her open eyes looking down at the camera, the white shirt with its collar open exactly as it is (do not change the shirt), the short black skirt, the sheer black thigh-high stockings with lace tops, her right hand at her temple, her left hand on the armrest, the grey armchair, the desk lamp, the night window, the tiled floor, the extreme low camera angle, her right leg extended straight toward the camera with the stockinged foot in the lower-left foreground, her left foot in its black stiletto on the floor. Change only this: the black stiletto pump that was lying on the floor is now hanging from her extended right foot: her toes are inside the front of the pump, the back of the pump has slipped off her heel, and the pump dangles from her toes, pointing down toward the floor with its thin heel hanging in the air; nothing lies on the floor in front of her. Also remove the bag on the desk at the right edge and remove the caption text along the bottom edge; the bottom of the image is just the tiled floor. Legs smooth under the black sheer, no veins. No nudity, no underwear visible. Sharp, in focus. Avoid: shoe lying on the floor, shoe fully on the foot, closed eyes, smile, bag, chain, text, caption, watermark.
```

| job | 結果 |
|---|---|
| 237 `a382f3ff-dbba-46f2-9389-d23e65359a94` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_093614_a382f3ff-dbba-46f2-9389-d23e65359a94.png |
| 238 `6d28e309-e05c-4a6f-a4ae-05a40948df65` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_093611_6d28e309-e05c-4a6f-a4ae-05a40948df65.png |

- 看圖：**237 達標**——鞋掛在伸出的腳尖、鞋跟朝下懸空、眼睛睜開往前下方俯視、底部文字與包包都消失、黑絲與襯衫未動、手撐太陽穴。238 鞋也掛在腳尖，但地上多出一隻鞋。
- 與 231 相比的差異（來自真人照）：椅子從辦公椅變成灰布扶手椅＋深色皮椅背、地板變磁磚；製作師看第 1 輪時未反對，暫視為接受，若要換回辦公椅可再一輪。

### 經驗
- 真人照當第二張參考：姿勢抄得到，但椅子、地板、包包、**浮水印文字**也會一起進來；要用時盡量用無浮水印、背景乾淨的圖，或抄完姿勢後再做一輪「不附參考圖」的清理。
- 「鞋半套在腳尖」靠參考圖兩輪都沒成，改成純文字描述（toes inside the front of the pump, back slipped off the heel, pump dangles from her toes, heel hanging in the air）一輪就成。
- 「eyes cast downward, eyelids lowered」會被做成閉眼；要寫「eyes open, irises visible, gaze lowered」。

- 候選定稿改為 **job 237**，待製作師確認。
- 餘額 3242.24 → 3236.24（本段 6 點）；本批累計 19.32 點。

### 先鋒四人狀態（追加 14 後）

| 角色 | 狀態 |
|---|---|
| Nanami | 定稿 v1（job 6ed76f6b） |
| Vicky | 空中瑜伽版（job 6e71f97e）待定；是否補臉朝鏡頭版未決 |
| Wendy | **候選定稿 job 237**，待製作師確認 |
| Kanon | 小惡魔版作廢；地雷系版待出 |
