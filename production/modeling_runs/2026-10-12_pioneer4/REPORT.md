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

## 追加 15（2026-10-12）：製作師指定以真人照為底，直接改成 Wendy

- 製作師指示：直接用這張（同一張真人照的高清版）去改：1. 臉和頭髮換成現在這個人（Wendy），動作姿勢不改；2. 胸部更明顯；3. 白襯衫扣子太大，改小；4. 絲襪斷掉處接起來；5. 高跟鞋下金色鏈子拿掉。補充：口紅可以留但淡一點；乳溝要露出來。
- 檔案狀況：高清版只以訊息內嵌顯示，沒有以檔案進到執行環境，無法上傳；本輪沿用同一張照片先前上傳的 318×466 版（media `e960969a-31ce-4ee7-84bb-8310a5008742`）。Seedream 輸出 1728×2304，構圖不受影響。
- 做法：Seedream 4.5，image_references ＝ media e960969a，prompt 寫成「以 Wendy（face-only Element）重現此構圖與姿勢」並列出六項更改（身形依 Wendy 設定描述，不是在原照片的身體上加工）。count 2，各 1 點。
- prompt：

```
<<<19f44c28-fb6b-45e1-bd13-6b88a5223dd8>>> is the woman's face. Recreate the reference image with this woman in it, keeping the exact same pose, framing and extreme low camera angle: she leans back in the grey armchair with the dark leather back, right elbow on the armrest and right hand raised to her temple, left hand resting on the other armrest, her right leg extended straight toward the camera with the stockinged foot in the lower-left foreground and the black patent pump hanging from her toes, the other leg bent; the same desk lamp, dark wooden desk, night window with city lights and grey tiled floor. Change these: (1) her face is this woman's face and her hair is silver-grey, worn down in a loose chin-length layered bob, with thick black square-frame glasses; (2) her bust is fuller and clearly visible: the top buttons of the white shirt are undone so the collar opens to show her cleavage; (3) the shirt buttons are small ordinary white shirt buttons, not large gold buttons; (4) her sheer black pantyhose are one continuous seamless layer from under the skirt down to her toes, no cut, no band and no break in the nylon on her thigh; (5) there is no gold chain or ornament under the shoe or on the floor, the shoe is a plain black patent stiletto pump; (6) her lips are red but a slightly lighter, softer red. Expression: eyes open, a cold bored look, gaze lowered toward the camera, lips closed. No handbag on the desk. Legs smooth under the black sheer, no veins. No nudity, no underwear visible. Sharp, in focus. Avoid: large gold buttons, chain, bag, a break or band in the stockings, dark hair, closed eyes, smile, text, watermark.
```

| job | 結果 |
|---|---|
| 239 `0ed3e25b-e829-4776-a9e0-a20c74073774` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_094200_0ed3e25b-e829-4776-a9e0-a20c74073774.png |
| 240 `9c3306ef-143a-48ee-9a4c-abe1a0ef4dac` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_094201_9c3306ef-143a-48ee-9a4c-abe1a0ef4dac.png |

- 看圖：**239 達標**——Wendy 臉＋銀灰髮放下＋黑框眼鏡、姿勢與參考圖一致（手撐太陽穴、腿伸直、鞋掛腳尖）、襯衫開領露乳溝且胸部明顯、小白扣、黑絲連續無斷、無金鍊、桌上包包也消失、口紅較淡、眼睛睜開看鏡頭。缺點：四邊帶一圈細白邊（抄自參考圖的邊框），執行者已裁掉另存；嘴角帶一點點笑意，不算冷。**240 否決**——底部浮水印文字又被抄進來、白邊更明顯。
- 候選定稿改為 **job 239（裁白邊版）**，待製作師確認；表情要再冷一點可再修一輪（以 239 為底、不附真人照）。
- 餘額 3236.24 → 3234.24；本批累計 21.32 點。

### 先鋒四人狀態（追加 15 後）

| 角色 | 狀態 |
|---|---|
| Nanami | 定稿 v1（job 6ed76f6b） |
| Vicky | 空中瑜伽版（job 6e71f97e）待定；是否補臉朝鏡頭版未決 |
| Wendy | **候選定稿 job 239（裁白邊）**，待製作師確認 |
| Kanon | 小惡魔版作廢；地雷系版待出 |

## 追加 16（2026-10-12）：改用 Nano Banana 2.1 做「照片換臉＋細節修正」

- 製作師看 239／240 後：「還是不太一樣」，並問能否用 Higgsfield 介面「點之前生成的圖、按 Reference」來做。執行者說明：MCP 的 `image_references` 放 job ID 就是同一個動作；差別在 Seedream 是「參考後重畫」，整張會漂。改試編輯型模型。
- 模型選擇：`models_explore` 推薦裡可吃多張參考、強調保留原圖的有 FLUX 3 Image、GPT Image 2.5、Nano Banana 2.1、Ideogram 4.5；選 **Nano Banana 2.1**（Google；多圖參考、以保留原圖著稱；GPT 對擦邊內容審查嚴，先不用）。
- 輸入：第一張 ＝ 製作師照片（media `e960969a`，318×466），第二張 ＝ job 229（Wendy 臉、銀髮、眼鏡的來源）。不用 Element 標記。2k、thinking high、aspect auto、count 2。**每張 2 點**（餘額 3234.24 → 3230.24）。
- prompt：

```
Edit the first image. Keep everything in the first image exactly as it is: the pose, the hand at her temple, the other hand on the armrest, the legs and feet, the shoe hanging from her toes, the grey armchair, the desk, the lamp, the night window, the tiled floor, the framing and the low camera angle. Make only these changes: (1) replace the woman's face, hair and eyewear with those of the woman in the second image: her face, her silver-grey hair worn down in a loose chin-length layered bob, and her thick black square-frame glasses; (2) make her bust fuller and more prominent, and open the top of the white shirt one more button so her cleavage is clearly visible; (3) replace the large gold shirt buttons with small plain white shirt buttons; (4) make the black sheer pantyhose one continuous smooth layer over both legs, removing the lighter band and the break on her thigh; (5) remove the gold chain hanging under the shoe; (6) keep the red lipstick but make it a slightly lighter, softer red; (7) remove the handbag on the desk at the right edge. Photorealistic, clean, sharp. No text, no watermark, no border.
```

| job | 結果 |
|---|---|
| 241 `07afa7a5-3493-436f-b861-ba54e76ada70` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_094648_07afa7a5-3493-436f-b861-ba54e76ada70.png |
| 242 `6bbcfa9d-c10c-4800-a992-d7a04b5937e9` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_094649_6bbcfa9d-c10c-4800-a992-d7a04b5937e9.png |

- 看圖：兩張幾乎等於原照片的構圖——椅子、燈、桌、窗、地板、手撐太陽穴、另一手扶手、腿伸直、鞋掛腳尖全部保留；換成 Wendy 臉＋銀灰 bob＋黑框眼鏡；乳溝露出、胸部更明顯；小白扣；黑絲連續無斷；金鍊拿掉；包包拿掉；口紅較淡；眼睛睜開看鏡頭。241 表情冷淡，242 嘴角微笑。輸出 1696×2486，無白邊、無浮水印文字。
- 結論：「以指定照片為底、只改指定部位」用 Nano Banana 2.1 比 Seedream 準得多；之後同類需求建議走 Nano Banana（2 點／張），Seedream 留給「重畫新構圖」，soul_2 留給「只要本人、不需參考圖」。
- 候選定稿改為 **job 241**（或 242，由製作師選），取代 239。
- 本批累計 25.32 點。

### 先鋒四人狀態（追加 16 後）

| 角色 | 狀態 |
|---|---|
| Nanami | 定稿 v1（job 6ed76f6b） |
| Vicky | 空中瑜伽版（job 6e71f97e）待定；是否補臉朝鏡頭版未決 |
| Wendy | **候選定稿 job 241／242（Nano Banana 2.1，以製作師照片為底）**，待製作師選 |
| Kanon | 小惡魔版作廢；地雷系版待出 |

## 追加 17（2026-10-12）：Wendy 定稿 242，裸露皮膚的美肌稍微收回

- 製作師決定：**242 定稿**。要求：皮膚紋理現在美肌太多，修回來一點，但只修裸露在外的皮膚（臉、頸、胸口、手臂、手）；腿和腳不要動（之前的美肌主要是為了腿的青筋與肌肉紋理）。
- 做法：Nano Banana 2.1，image_references ＝ job 242，兩個程度各一張：243 輕（slightly more natural）、244 中（clearly more natural, photographic）。2k、thinking high、aspect auto，各 2 點。
- prompt（243；244 只把紋理那句改成 `give it a clearly more natural, photographic skin texture: visible fine pores, natural skin detail, realistic subsurface tone and gentle highlights, like a good portrait photo with light retouching, still flattering`）：

```
Edit the image. Keep everything exactly as it is: the pose, composition, framing, lighting, the white shirt, the black skirt, the hair, the glasses, the lipstick, the chair and the room, and especially the legs, feet and black stockings, which must not be touched at all. Make only one change: the bare skin of her face, neck, upper chest, arms and hands currently looks over-smoothed by a beauty filter; restore a slightly more natural skin texture there: fine pores and subtle natural skin detail with gentle highlights, still clean, flattering and photogenic, not harsh. Do not change the shape of her face or body, do not change the legs, feet or stockings, do not add blemishes, wrinkles or veins. No text, no watermark.
```

| job | 程度 | 結果 |
|---|---|---|
| 243 `eb647a2b-8283-4c62-ae16-f90691ce07f0` | 輕 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_095242_eb647a2b-8283-4c62-ae16-f90691ce07f0.png |
| 244 `aae13955-0338-4dec-aa46-c387b581a5d5` | 中 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_095307_aae13955-0338-4dec-aa46-c387b581a5d5.png |

- 看圖（臉與胸口 100% 裁切比對 242／243／244）：243 臉部出現細微毛孔與自然光澤、胸口略增紋理，整體仍乾淨；244 毛孔與皮膚細節明顯，臉頰與胸口帶油光感。兩張的腿、絲襪、鞋、構圖與 242 完全一致，沒有被動到。
- 餘額 3230.24 → 3226.24；本批累計 29.32 點。

## 定稿（2026-10-12，製作師決定）：Wendy

- **Wendy Yeo（冷艷女上司）形象照 v1 ＝ job 242 系列**（Nano Banana 2.1，以製作師提供的照片為底換臉與修細節，追加 16）；皮膚修正版 **243（輕）／244（中）由製作師選程度**，選定後即為最終檔。1696×2486，無白邊、無浮水印，可直接發布或裁切。
- 素材登記：底圖為製作師提供的真人照（來源與權利不明），製作師於追加 14 決定直接使用、由平台把關；輸出人物為 Wendy 虛擬角色（臉與髮型來源 job 229）。發布前的權利風險由製作師與客戶承擔，執行者已記錄並說明。
- 工具分工（本日結論）：以指定照片為底只改部位 → Nano Banana 2.1（2 點）；重畫新構圖 → Seedream 4.5＋Element（1 點）；只要本人、不需參考圖 → soul_2（0.12 點）。

### 先鋒四人狀態（追加 17 後）

| 角色 | 狀態 |
|---|---|
| Nanami | 定稿 v1（job 6ed76f6b） |
| Vicky | 空中瑜伽版（job 6e71f97e）待定；是否補臉朝鏡頭版未決 |
| Wendy | **定稿 v1 ＝ 242 系列；皮膚程度 243／244 待製作師選** |
| Kanon | 小惡魔版作廢；地雷系版待出 |

## 追加 18（2026-10-12）：皮膚紋理改以 Nanami 定稿為基準

- 製作師看 243／244 後：「再回來一點，拿另外一張定稿的皮膚來做對照，以那張為基準。」即以 Nanami 定稿 v1（job `6ed76f6b-0059-45b3-a17a-e272175ae5b3`，soul_2）的皮膚質感為目標。
- 做法：Nano Banana 2.1，image_references ＝ job 242（底圖）＋ job 6ed76f6b（只作皮膚質感參考，prompt 明寫不抄臉、髮、衣、背景）。只改裸露皮膚，腿、腳、絲襪不動。2k、thinking high、count 2，各 2 點。
- prompt：

```
Edit the first image. Keep everything in the first image exactly as it is: the woman's identity and face shape, her silver-grey hair, glasses, lipstick, the pose, composition, framing, lighting, the white shirt, the black skirt, the chair and the room, and especially the legs, feet and black stockings, which must not be touched at all. Make only one change: the bare skin of her face, neck, upper chest, arms and hands is over-smoothed by a beauty filter; re-render that bare skin so its texture matches the skin of the woman in the second image: the same level of natural skin detail, fine pores, soft natural highlights and realistic skin tone that the second image has, no more smoothed and no more textured than that. Use the second image only as the reference for skin texture; do not copy her face, features, hair, clothes or background. Do not change the shape of her face or body, do not change the legs, feet or stockings, do not add blemishes, wrinkles or veins. No text, no watermark.
```

| job | 結果 |
|---|---|
| 245 `1fb9395e-351f-41be-888f-a8d0c2ab8339` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_095552_1fb9395e-351f-41be-888f-a8d0c2ab8339.png |
| 246 `5d8380cf-3862-4228-a101-6e63d4da94b9` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_095553_5d8380cf-3862-4228-a101-6e63d4da94b9.png |

- 看圖（100% 裁切：Nanami 基準／242／245／246 的臉與胸口）：245 臉、頸、胸口有細毛孔與膚色層次，最接近 Nanami 那種自然手機照質感；246 略滑一點、帶一點光澤。兩張的身分、髮、眼鏡、口紅、腿、絲襪、鞋、構圖與 242 完全一致，Nanami 的臉沒有被抄進來。
- 餘額 3226.24 → 3222.24；本批累計 33.32 點。
- 定稿更新：**Wendy 形象照 v1 ＝ 242 系列，皮膚版本 245／246 由製作師選**（243／244 作廢備查）。

### 先鋒四人狀態（追加 18 後）

| 角色 | 狀態 |
|---|---|
| Nanami | 定稿 v1（job 6ed76f6b） |
| Vicky | 空中瑜伽版（job 6e71f97e）待定；是否補臉朝鏡頭版未決 |
| Wendy | **定稿 v1 ＝ 242 系列；皮膚版本 245／246 待製作師選** |
| Kanon | 小惡魔版作廢；地雷系版待出 |

## 追加 19（2026-10-12）：磨皮再退更多（顆粒感）

- 製作師看 245／246 後：「兩張都還是磨皮磨太兇，再修回來更多，仔細看顆粒感。」
- 做法：Nano Banana 2.1，image_references ＝ job 245（底圖）＋ job 6ed76f6b（Nanami 定稿，只作皮膚顆粒參考）。只改裸露皮膚；腿、腳、絲襪不動。2k、thinking high，兩個強度各一張、各 2 點。
- prompt（247「強」）：

```
Edit the first image. Keep everything in the first image exactly as it is: the woman's identity and face shape, her silver-grey hair, glasses, lipstick, the pose, composition, framing, lighting, the white shirt, the black skirt, the chair and the room, and especially the legs, feet and black stockings, which must not be touched at all. Make only one change: the bare skin of her face, neck, upper chest, arms and hands is still far too smooth, airbrushed like a beauty filter. Re-render that bare skin as real, unretouched skin, matching the skin grain of the woman in the second image: clearly visible pores on the nose, cheeks, forehead, neck and chest, natural skin micro-texture, fine photographic grain, soft natural highlights and realistic uneven skin tone, as seen at 100% zoom in an unretouched phone photo. No airbrushing, no beauty filter, no plastic or waxy look. Use the second image only as the reference for skin grain and pores; do not copy her face, features, hair, clothes or background. Do not change the shape of her face or body, do not change the legs, feet or stockings, do not add blemishes or wrinkles. No text, no watermark.
```

- prompt（248「更強」）：同上，但皮膚句改為 `Replace that bare skin with raw, completely unretouched real skin, matching and slightly exceeding the skin grain of the woman in the second image: strongly visible pores across the nose, cheeks, forehead, chin, neck, chest and arms, pronounced natural skin micro-texture, visible fine photographic grain and sensor noise, realistic uneven skin tone with faint natural redness, subtle fine lines where skin naturally creases, matte skin with only natural sheen, as in a raw high-resolution photo with zero retouching. Absolutely no airbrushing, no beauty filter, no smoothing, no plastic or waxy look.`（仍寫 do not add acne or blemishes）。

| job | 強度 | 尺寸 | 結果 |
|---|---|---|---|
| 247 `8fdc1ad2-a0f3-4a84-b65b-f874e650ca8f` | 強 | 1696×2486 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_095953_8fdc1ad2-a0f3-4a84-b65b-f874e650ca8f.png |
| 248 `6232cd67-bf0f-48ab-93c3-a4e89e420de5` | 更強 | 1792×2390 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_095959_6232cd67-bf0f-48ab-93c3-a4e89e420de5.png |

- 看圖（100% 裁切：Nanami 基準／245／247／248）：**247** 臉、頸、胸口毛孔與顆粒清楚、膚色有層次、仍有自然光澤，身分、髮、眼鏡、口紅、腿、絲襪、鞋、構圖與 242 完全一致。**248** 顆粒更重，但模型違反指令加了雀斑斑點，且輸出被重新裁成 3:4（1792×2390），構圖跑掉，**否決**。
- 經驗：Nano Banana 寫到「raw / sensor noise / zero retouching」會開始加斑點並改尺寸；「clearly visible pores + fine photographic grain + do not add blemishes」是可控上限。再要更粗，建議改用後製在皮膚區加顆粒，而不是再推模型。
- 餘額 3222.24 → 3218.24；本批累計 37.32 點。
- 定稿更新：**Wendy 形象照 v1 ＝ 242 系列，皮膚版本建議 job 247**，待製作師確認（245／246 備查，243／244／248 作廢）。

### 先鋒四人狀態（追加 19 後）

| 角色 | 狀態 |
|---|---|
| Nanami | 定稿 v1（job 6ed76f6b） |
| Vicky | 空中瑜伽版（job 6e71f97e）待定；是否補臉朝鏡頭版未決 |
| Wendy | **定稿 v1 ＝ 242 系列；皮膚版本建議 247，待製作師確認** |
| Kanon | 小惡魔版作廢；地雷系版待出 |

## 追加 20（2026-10-12）：Wendy 定稿 247；Nanami 定稿去假社群介面；最終檔進 repo；交接

- 製作師決定：**Wendy 形象照 v1 定稿 ＝ job 247**（`8fdc1ad2-a0f3-4a84-b65b-f874e650ca8f`）。
- 製作師要求：前一張定稿（Nanami v1，job 6ed76f6b，soul_2 自帶假社群介面）把浮水印拿掉；最終檔先上傳 GitHub；接著開新 session 交接。
- Nanami 去介面：Nano Banana 2.1，image_references ＝ job 6ed76f6b，2k、thinking high，2 點。prompt：

```
Edit the image. Remove all the social-media interface overlays: the round avatar icon and the username text at the top left, the small square icon at the top right, the round avatar icon and the text at the bottom left, and the paper-plane send icon at the bottom right. Fill those areas seamlessly with the surrounding background (the ceiling and wall at the top, the table, bowls and plates at the bottom). Keep everything else in the image exactly as it is: the woman, her face, expression, hair, pose, the chopsticks and food, her clothing, the room, the framing and colors. No text, no icons, no logos, no watermark, no border.
```

| job | 結果 |
|---|---|
| 249 `f99e1364-a8c9-46a6-8a1b-f8fdb93e7ad5` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_100422_f99e1364-a8c9-46a6-8a1b-f8fdb93e7ad5.png |

- 看圖（前後並排＋上下邊 100% 裁切）：上下四個圖示與文字全部清除並補上天花板、牆面、桌面與盤子；人物、表情、筷子、食物、構圖不變；輸出 1792×2390（同 3:4，放大到 2k）。
- 最終檔進 repo（JPEG 品質 95、全解析度；PNG 原檔以上表 URL 為準）：
  - `finals/wendy_v1_job247_8fdc1ad2.jpg`（1696×2486）
  - `finals/nanami_v1_job249_f99e1364_clean.jpg`（1792×2390）
- 交接文件：`HANDOFF_2026-10-12.md`（現況、工具結論、製作師決定、下一步、新 session 權限）。
- 允許清單再補：SendUserFile、ToolSearch、WebFetch／WebSearch、Read／Glob／Grep、git checkout／switch／merge／stash／rm／mv、mv、rm -f、tr、xargs、date、which、pwd、true（共 59 條）。
- 餘額 3218.24 → 3216.24；本批累計 39.32 點（10/12 全日：3253.84 → 3216.24，37.60 點，與逐輪加總差異為 Seedream 姿勢圖等已記錄項目的四捨五入）。

### 先鋒四人狀態（追加 20 後）

| 角色 | 狀態 | 最終檔 |
|---|---|---|
| Nanami | **定稿 v1 去介面版 job 249** | `finals/nanami_v1_job249_f99e1364_clean.jpg` |
| Wendy | **定稿 v1 job 247** | `finals/wendy_v1_job247_8fdc1ad2.jpg` |
| Vicky | 空中瑜伽版（job 6e71f97e）待定；是否補臉朝鏡頭版未決 | — |
| Kanon | 小惡魔版作廢；地雷系版待出 | — |

## 追加 21（2026-10-12，新 session）：Wendy 定稿的臉是否跑掉——用 Soul 對照

- 製作師指示：先用 Soul，確認 Wendy 定稿（job 247）的臉有沒有跑掉。
- 做法：`soul_2`＋Wendy `soul_id` `cb91c63f-0fa2-4c8f-94b2-a70a00acdbaf`，出兩張與定稿同造型的近景（銀灰 bob 放下、黑框眼鏡、紅唇、白襯衫、辦公室夜景、鏡頭略低俯視），3:4、2k，count 2，各 0.12 點。再加上 10/08 身分測試正面照（job `0b64c3a7`）當基準，與 job 229（Seedream＋Element）、job 242（Nano Banana 真人照為底）、job 247（定稿）做臉部 100% 裁切並排。
- prompt：

```
Close-up portrait of this woman, head and shoulders filling the frame, 28 years old. Silver-grey hair worn down in a loose chin-length layered bob, thick black square-frame glasses, soft red lips. White shirt with the collar open. Office at night, a warm desk lamp on one side, city lights blurred behind her. Camera below her eye level looking up; she looks down at the camera with a cold, bored expression, eyes open, chin raised slightly, lips closed, no smile. Face sharp and in focus, large in the frame. Keep her face exactly the same person. Smooth flattering skin. Avoid: smile, closed eyes, text, watermark, UI overlay, social media interface.
```

| job | 結果 |
|---|---|
| 250 `e3d0ca3e-8fa5-42b3-8d53-7bcc4cf35795` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_101124_e3d0ca3e-8fa5-42b3-8d53-7bcc4cf35795.png |
| 251 `c01de148-d6da-4fc1-8a3f-8b408237fc2d` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_101124_c01de148-d6da-4fc1-8a3f-8b408237fc2d.png |

- 看圖（執行者判讀，由製作師定）：**定稿 247 的臉已偏離 Soul**。
  - Soul 基準（身分照＋250／251 三張一致）：臉型較長的鵝蛋臉、顴骨平寬、眉形自然平直、杏眼中等大小有雙眼皮、鼻樑中等寬、下唇飽滿、下巴圓潤。soul_2 加了眼鏡與銀髮之後仍是同一個人，Soul 本身穩。
  - job 229（Seedream＋face-only Element）：已開始偏——眼睛變細長帶眼線、下巴變尖，偏「通用美女」，約七成像（與追加 3、9 的觀察一致）。
  - job 242 → 247（Nano Banana，以真人照為底換臉）：偏得更多——下半臉變短、臉變圓、眼睛更細且上挑、下巴尖成 V 形、嘴唇變薄、臉頰較飽滿；是真人照原本那位與 Wendy 的混合，估約五到六成像。皮膚修正（243–247）沒有再改變五官。
  - 結論：跑掉的主因是「以真人照為底換臉」這一步（Nano Banana 保留了原照片的臉部結構），Seedream 那一步也先丟了一部分。
- 可行的修法（提案，等製作師決定，未執行）：
  1. Nano Banana 2.1：以 247 為底，第二張放 job 250 或 251（Soul 近景）當臉的來源，指令「只把臉換成第二張的人，髮型、眼鏡、姿勢、衣服、背景全部不動」，2 點／張。保留定稿構圖，臉拉回 Soul。
  2. 若 1 仍不夠像：先用 soul_2 出一張同角度（低角度俯視）的臉，再用它當第二張參考做 1。
  3. 重新定義：接受 247 為 Wendy 的新臉（之後所有 Wendy 圖都以 247 當臉參考而非 Soul）。不建議，因為 Soul 才是十人身分測試與型錄的基準，且 247 的臉來自權利不明的真人照。
- 對照圖：執行者端 `wendy_face_check_sheet.jpg`（六格臉部裁切），已傳給製作師，不進 repo。
- 餘額 3216.24 → 3216.00；本批累計 39.56 點。

### 先鋒四人狀態（追加 21 後）

| 角色 | 狀態 | 最終檔 |
|---|---|---|
| Nanami | 定稿 v1 去介面版 job 249 | `finals/nanami_v1_job249_f99e1364_clean.jpg` |
| Wendy | 定稿 v1 job 247，**臉與 Soul 不符，待製作師決定是否拉回** | `finals/wendy_v1_job247_8fdc1ad2.jpg` |
| Vicky | 空中瑜伽版（job 6e71f97e）待定 | — |
| Kanon | 小惡魔版作廢；地雷系版待出 | — |

## 追加 22（2026-10-12）：Wendy 定稿換臉回 Soul（方法 1）

- 製作師決定：用追加 21 的方法 1——以 job 247 為底、第二張放 job 250（soul_2 近景）當臉來源，把臉換回 Soul。
- 做法：Nano Banana 2.1，image_references ＝ job 247（底圖）＋ job 250（臉來源），2k、thinking high、aspect auto，count 2，各 2 點。prompt 明寫只換臉、保留髮型／眼鏡／口紅色／視線／表情／姿勢／衣服／背景／身體皮膚紋理，並具體描述 Soul 的五官特徵（較長鵝蛋臉、圓下巴非 V 形、顴骨平寬、眉平直、杏眼雙眼皮、下唇飽滿、淡妝無濃眼線）。
- prompt：

```
Edit the first image. Keep everything in the first image exactly as it is: the composition, framing and extreme low camera angle, the pose with her right hand raised to her temple and her left hand on the armrest, her extended right leg with the black stiletto hanging from her toes, the sheer black stockings, the white shirt with its open collar and cleavage, the black skirt, the grey armchair, the desk, the lamp, the night window, the tiled floor, the lighting and colors, and the skin texture of her body. Make only one change: replace her face with the face of the woman in the second image, so that it is clearly the same person as the second image: the same face shape (a longer oval face with a soft rounded chin, not a pointed V chin), the same broad flat cheekbones, the same straight natural eyebrows, the same almond-shaped eyes with double eyelids and the same eye size and spacing, the same nose, the same full lips especially the full lower lip, the same jawline. Keep the second image's natural light makeup level: no heavy eyeliner, no cat-eye. Keep from the first image her silver-grey chin-length bob hairstyle, her thick black square-frame glasses, her soft red lipstick color, her head angle and the direction of her gaze looking down at the camera, and her cold, bored expression with lips closed and no smile. The face must match the first image's lighting, skin tone and skin grain so it blends naturally. Do not copy the second image's hair, clothes, pose, background or framing. No text, no watermark, no border.
```

| job | 尺寸 | 結果 |
|---|---|---|
| 252 `db476121-db57-44d4-b2a8-aee03466ba3b` | 1792×2390（被重裁成 3:4，取景略寬，沒有切掉東西） | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_101659_db476121-db57-44d4-b2a8-aee03466ba3b.png |
| 253 `9079d418-1ee7-4762-9b9c-891287180943` | 1696×2486（與 247 完全同尺寸） | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_101700_9079d418-1ee7-4762-9b9c-891287180943.png |

- 看圖（臉部 100% 裁切與 Soul 250、247 並排；全圖 247／252／253 並排）：
  - **252**：臉明顯拉回 Soul——較長的鵝蛋臉、圓下巴、眉平直、杏眼雙眼皮、下唇飽滿，淡妝；銀灰 bob、黑框眼鏡、紅唇、俯視冷淡表情、手撐太陽穴都保留；腿、絲襪、掛腳尖的鞋、椅子、燈、窗全部不變。代價：輸出被重裁成 3:4，畫面比 247 略寬（左側多露一點桌子）。執行者判讀約八到九成像 Soul。
  - **253**：尺寸與 247 完全一致，但臉只拉回一半——眼睛仍偏細、下巴仍偏尖，介於 247 與 Soul 之間，約七成像。
  - 身體皮膚紋理：兩張與 247 一致，未被磨回去；252 的臉部皮膚比身體略平滑一點。
- 建議：**以 252 取代 247 為 Wendy 定稿**（臉是 Soul 本人），待製作師確認。若製作師要 247 的原尺寸，可以 252 為底再跑一次 Nano Banana 只要求 1696×2486 取景，或直接把 252 裁成 1696×2486（左右各裁約 48px，不影響主體）。
- 餘額 3216.00 → 3212.00；本批累計 43.56 點。

### 先鋒四人狀態（追加 22 後）

| 角色 | 狀態 | 最終檔 |
|---|---|---|
| Nanami | 定稿 v1 去介面版 job 249 | `finals/nanami_v1_job249_f99e1364_clean.jpg` |
| Wendy | **候選定稿 v2 ＝ job 252（臉回 Soul）**，待製作師確認後換掉 finals | `finals/wendy_v1_job247_8fdc1ad2.jpg`（臉偏離 Soul，待替換） |
| Vicky | 空中瑜伽版（job 6e71f97e）待定 | — |
| Kanon | 小惡魔版作廢；地雷系版待出 | — |

## 定稿（2026-10-12，製作師決定）：Wendy v2 ＝ job 252

- **Wendy Yeo（冷艷女上司）形象照定稿改為 v2 ＝ job 252**（`db476121-db57-44d4-b2a8-aee03466ba3b`，Nano Banana 2.1，以 247 為底、臉換回 Soul job 250），1792×2390，取代 v1（job 247）。
- 最終檔：`finals/wendy_v2_job252_db476121.jpg`（JPEG 品質 95、全解析度；PNG 原檔以追加 22 的 URL 為準）。v1 檔 `finals/wendy_v1_job247_8fdc1ad2.jpg` 保留備查，不再使用（臉偏離 Soul）。
- 身分鏈：Soul `cb91c63f`（10/08 身分測試通過）→ job 250（soul_2 近景）→ job 252 的臉。構圖、身體、場景沿自 job 242–247（底圖為製作師提供的真人照，權利不明，追加 14 製作師決定直接使用）。
- 未做：沒有裁回 1696×2486（製作師未要求）；臉部皮膚與身體的平滑度差異未再處理。

### 先鋒四人狀態（Wendy v2 定稿後）

| 角色 | 狀態 | 最終檔 |
|---|---|---|
| Nanami | 定稿 v1 去介面版 job 249 | `finals/nanami_v1_job249_f99e1364_clean.jpg` |
| Wendy | **定稿 v2 job 252** | `finals/wendy_v2_job252_db476121.jpg` |
| Vicky | 空中瑜伽版（job 6e71f97e）待定 | — |
| Kanon | 小惡魔版作廢；地雷系版待出 | — |

## 追加 23（2026-10-12）：Vicky 劈腿形象照 第 1 版（依製作師參考圖）

- 製作師指示與規格（先確認再出圖）：參考圖為皮拉提斯教室一字馬對鏡自拍（製作師提供，橫幅 1170×800，含 kbj98.com／SULTLLUV 浮水印，來源與權利不明；依追加 14 決定直接餵平台，由平台把關）。要求：不拿手機、自然在做運動；改 3:4 直幅，用斜角讓腿不被切；前凸後翹；上衣照 job 203（黑色運動內衣）、下身黑色微透瑜伽褲；表情專注帶一點笑；髮型照 job 203 高馬尾。
- 參考圖上傳：media `1216a1cc-6c92-42f0-ad58-3185fe532b78`（`vicky_ref_split.jpg`），圖檔不進 repo。
- Vicky 的 Element：`Vicky Lin` `325284ce-670c-4efd-a8a9-2773ad0c53f7`（帳號裡沒有 Vicky 的 face-only 版）。
- 做法：Seedream 4.5 basic、3:4、count 1、1 點。image_references ＝ media 1216a1cc（姿勢與場景）＋ job 203 `51dd9c69`（臉、髮型、上衣）。prompt：

```
<<<325284ce-670c-4efd-a8a9-2773ad0c53f7>>> is the woman in this photo. Portrait-orientation 3:4 photo of her doing a full front split on a purple yoga mat in a bright Pilates studio, as in the first reference image: the same studio with the wooden reformer, frosted glass partitions, Bosu ball and the pink and yellow exercise balls, soft daylight. Use the first reference only for the pose and the room. Change the camera: shoot from the front-side at about a 45-degree diagonal, camera at hip height, so that her split legs run diagonally across the frame from the lower-left foreground toward the upper right and both legs are fully inside the frame, nothing cropped. No phone, no mirror selfie: she is simply stretching, both hands resting on the mat in front of her front leg, upper body turned slightly toward the camera. Her figure is curvy and athletic: full bust pushed forward, lower back arched inward, round lifted hips, strong smooth thighs, tanned skin. She looks like the woman in the second reference image: the same face, the same high ponytail with a few loose strands, the same black scoop-neck sports bra. Bottom: black high-waisted yoga leggings in a thin slightly sheer stretch fabric with a soft matte sheen, opaque enough that no skin or underwear shows through. Expression: focused on the stretch with a small soft smile, eyes toward the camera. Beauty-camera look: smooth glowing flattering skin, soft warm light, slightly airy highlights. Sharp, in focus. Avoid: phone, mirror, selfie, text, watermark, logo, caption, UI overlay, social media interface, see-through fabric, nudity, extra limbs, cropped feet.
```

| job | 尺寸 | 結果 |
|---|---|---|
| 301 `620c6307-4d0e-48a7-95b5-7648708de519` | 1728×2304 | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261012_105521_620c6307-4d0e-48a7-95b5-7648708de519.png |

- 看圖：做到——一字馬、沒有手機與鏡子、手撐墊子、黑運動內衣、黑色微透瑜伽褲（腿上有薄透光澤）、高馬尾、教室與器材（reformer、Bosu、粉黃球）、紫墊、沒有浮水印、沒有假介面。沒做到——**鏡位仍是側面平拍，腿橫向貫穿畫面，左右兩隻腳都被切掉**（這是本輪主要要求）；表情是露齒大笑，不是「專注帶一點笑」；前凸後翹程度中等。
- 臉（與 Soul 身分照、job 203 並排 100% 裁切）：眉型、眼型、曬色、唇形接近，執行者判讀約七到八成像；臉在畫面裡小，膚色比 Soul 略淺、唇略薄。可用 Nano Banana 以 job 203 當臉來源換回。
- 下一步提案（待製作師）：第 2 版把鏡位寫得更具體——鏡頭放在她前腿腳尖的斜前方、略高於地面，前腿腳在畫面下方前景、後腿往畫面深處延伸，兩腳都在框內；表情改寫為 `lips closed, faint smile, eyes on the camera, focused`。仍用 Seedream＋Element＋同兩張參考，1 張 1 點。
- 餘額 3212.00 → 3211.00；本批累計 44.56 點。
