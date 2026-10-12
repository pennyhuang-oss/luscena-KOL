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
