# 建模批次報告：2026-10-08 第 1 批（現有 Soul 選角板）

- 批次代號：CAST-SOUL-01
- 執行者：製作師的 Claude 助理
- 工作分支：`producer/modeling-r1`（從 `claude/luscena-kol-initial-draft-et17t8` 的交付版本建立）
- 狀態：**候選階段**。本批只產生並排比較用的中性建角照，沒有選定任何角色、沒有做身分測試、沒有做形象照、沒有訓練。

---

## 1. 讀取的版本與必讀檔案檢查

- 讀取的 commit（完整 SHA）：`ef096d8074eace9b297fb7c2241092a0fbaead73`（`git rev-parse HEAD` 與交接指定版本一致）。
- 交接 prompt【必讀】27 個檔案以 `test -f` 逐一檢查：**27 個全部存在，沒有缺檔**。
  - `review/RESPONSIBILITY_CHANGE_TASK_002_2026-10-07.md`
  - `production/modeling_pack_v1/00_START_HERE.md`、`L01.md`–`L10.md`、`MODEL_AND_WORKFLOW_OPTIONS.md`、`REFERENCE_AND_ACCEPTANCE.md`、`CLIENT_FEEDBACK_2026-10-07.md`
  - `persona_pack_v1/L01.md`–`L10.md`、`00_OVERVIEW.md`、`PRODUCER_REFERENCE_NEEDS.md`

## 2. 本批範圍與依據

### 2.1 製作師的指示（2026-10-08，製作師轉述 Penny 的確認）

1. Higgsfield 帳號（Plus 方案、私人 workspace）與額度可以使用。
2. **帳號上現有的 Soul 角色可以用在 Luscena。**
3. **唯一不能動的規格是製作師提供的架構圖**（標題「目的：在 Threads 建立 10 個帳號的流量矩陣，把流量導向 LUSCENA」）：3 個主帳號（A 兩性話題、B 大尺度 Cos、C 性感身材時尚）＋ 7 個流量帳號（T1 星座命理、T2 迷因梗圖、T3 電玩手遊、T4 AI 科技、T5 運動賽事／啦啦隊、T6 攝影人像、T7 時事新聞；題材機動）、三條設計原則、不開官方帳號。圖上沒有的設定（性別、名字、年齡、長相、造型）都可以改。
4. 製作師選擇**路線 B**：十個格子全部從現有 Soul 挑選，不另外生成男性角色。
5. 十個角色都要做；分批只是順序，不是淘汰。

這些指示是製作師在對話中口頭／文字下達，由執行者記錄；Penny 的確認是製作師轉述，執行者沒有直接向 Penny 查證。

### 2.2 和人設包不同的地方

| 項目 | 人設包（`persona_pack_v1`、`production/modeling_pack_v1`） | 本批做法 | 原因 |
|---|---|---|---|
| 臉的來源 | 十個原創新臉，從零生成；repo 沒有參考圖 | 從帳號現有 35 個 Soul 挑 | 製作師指示 2.1 第 2 點 |
| T2／T3／T4／T6 性別 | 男（L05 阿凱、L06 翔哥、L07 程翊、L09 士哲） | 全部改為女性（現有 Soul 全是女性） | 製作師選路線 B；架構圖沒規定性別 |
| 外型規格 | 各建模頁 B、C 節「必須維持」的身分特徵 | 不套用；改以現有 Soul 的臉為準 | 製作師指示 2.1 第 3 點 |
| 人設文字（名字、背景、§10 限制） | `persona_pack_v1/Lxx.md` | 本批不處理；哪些保留、哪些改寫，待製作師決定 | 不在本批範圍 |

執行者提醒：人設包的 L01–L10 文字人設是客戶在 2026-10-07 接受的；本批的性別與長相改動屬於實質改變。依製作師的說法，架構圖以外的設定可改，執行者照此執行並記錄；是否需要再向客戶說明，由製作師依其與客戶的流程處理。

### 2.3 不變的製作要求

成年外觀、不仿製真人、不做幼態或校園場景、十人靠骨架與五官區隔、保留失敗樣本、記錄實際扣點、不公開「十個帳號是同一團隊」、AI 揭露方式待定、不訓練前先確認條款。本批都適用。

## 3. 實際使用的工具、模型與 prompt

- 工具：Higgsfield MCP（Claude 連接器），工具 `generate_image_batch`、`jobs_wait`、`show_characters`、`balance`、`transactions`。
- 模型：`soul_2`（帳號回傳的模型名稱 `text2image_soul_v2`，顯示名「Higgsfield Soul 2.0」），參數 `aspect_ratio=3:4`、`quality=1.5k`，每張附一個 `soul_id`。
- 參考圖：**沒有上傳任何圖片。** 身分來源全部是帳號既有的 Soul 角色（見第 4 節表）。
- prompt 全文（35 張相同）：

```text
Neutral casting headshot of this woman. Front-facing, eye level, head and shoulders, face filling about 60% of the frame. Hair tucked behind both ears so forehead, both eyebrows and jawline are fully visible. Bare face or very light makeup, no eyeliner, natural lip color. Neutral expression, mouth closed, relaxed. Plain heather-gray crew-neck T-shirt, no jewelry, no glasses. Even soft frontal studio light, no colored light, no strong shadows. Plain medium-gray seamless background. Unretouched realistic photography with natural skin texture. Avoid: beauty filter, heavy makeup, text, watermark.
```

- 提交過程：Plus 方案限制「同時最多 8 個工作」。第一輪 35 個請求送出 21 個、14 個被拒（錯誤訊息 `Rate limit reached: max 8 concurrent job(s) on plus (monthly) plan.`）；之後分兩輪各 7 個補送，全部完成。被拒的請求沒有扣點。

## 4. 參考素材登記：帳號現有 Soul 角色

- 來源：Higgsfield 帳號 workspace `a23d2b05-ab60-43f6-950a-f6b1fe354725` 的 Soul 角色庫，共 36 個，35 個 `ready`、1 個 `failed`（`sofia-hsu-v4`，id `6a214ed3-a62b-4b34-a05b-7433c65ba88d`，未使用）。
- 權利狀態：**依製作師轉述 Penny 的確認，可用於本專案。** 這些 Soul 是在同一帳號訓練的；依 `research/REFERENCE_METHODS.md`，其中 13 個（#20–#35 範圍內的舊名字）來自 Penny 的舊專案 Virtual_KOL_Studio，19 個（名稱含 `soul-v1-5img-20260904`）是 2026-09-04 另一批訓練。訓練素材是否全為生成圖、訓練時的許可狀態，執行者查不到；API 只回傳縮圖，不回傳訓練圖張數（名稱中的 `5img`／`6img` 推測為訓練張數）。
- 用途：本批作為身分來源直接生成；**不另外拿去訓練**。

| # | Soul 名稱 | soul_id | 本批 job_id | 結果 |
|---|---|---|---|---|
| 1 | `zoey-yeh-soul-v1-5img-20260904` | `feb5f196-a60e-4ef9-9f8e-5daabbdacb52` | `6df15fa0-e4f2-46ed-9f8a-285510c6e6cb` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082301_6df15fa0-e4f2-46ed-9f8a-285510c6e6cb.png) |
| 2 | `yerin-han-soul-v1-5img-20260904` | `8c447a79-769f-4520-a538-cfb48fef6163` | `37842d9b-560e-4ead-a6d8-b6218155d10a` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082300_37842d9b-560e-4ead-a6d8-b6218155d10a.png) |
| 3 | `wendy-yeo-soul-v1-5img-20260904` | `cb91c63f-0fa2-4c8f-94b2-a70a00acdbaf` | `3ae80a53-b8c5-4505-9329-0093084cb99e` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082301_3ae80a53-b8c5-4505-9329-0093084cb99e.png) |
| 4 | `wanyin-jiang-soul-v1-5img-20260904` | `2e7de3f8-63ee-4302-a684-2245f6c54ea1` | `6fed8ba7-db5f-4539-974b-449523714206` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082301_6fed8ba7-db5f-4539-974b-449523714206.png) |
| 5 | `tammy-chou-soul-v1-5img-20260904` | `5069a35a-dd85-4161-8d0f-952bccbe676d` | `1843d3de-50b7-4ce3-b206-75674475a5ae` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083206_1843d3de-50b7-4ce3-b206-75674475a5ae.png) |
| 6 | `sydney-leong-soul-v1-5img-20260904` | `a41d8aab-fe2e-44c0-9d6a-c068565ac800` | `88bbac16-c3e5-4a3a-9cfc-90548d76a702` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083208_88bbac16-c3e5-4a3a-9cfc-90548d76a702.png) |
| 7 | `somi-oh-soul-v1-5img-20260904` | `c7915888-e566-4c9d-bc26-4bf40ab35c4c` | `573297d5-e945-42ed-a92b-09366835aca4` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082302_573297d5-e945-42ed-a92b-09366835aca4.png) |
| 8 | `ruoruo-tang-soul-v1-5img-20260904` | `4dc2bf79-0098-4c2a-b529-2b2b74117c81` | `3b499119-b864-41a1-bf78-81242469b86d` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083207_3b499119-b864-41a1-bf78-81242469b86d.png) |
| 9 | `rin-ayase-soul-v1-5img-20260904` | `34b7fd71-c8dd-4d6a-983e-881b1d012219` | `e3f4b43f-eb8c-43d3-9f75-19f9acee484e` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082302_e3f4b43f-eb8c-43d3-9f75-19f9acee484e.png) |
| 10 | `peggy-lee-soul-v1-5img-20260904` | `3e3f4f72-2a89-4f05-af61-0c6701c97a5c` | `9384b623-f7ca-4fef-b00c-2ab3d785524e` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082301_9384b623-f7ca-4fef-b00c-2ab3d785524e.png) |
| 11 | `nanami-fujiwara-soul-v1-5img-20260904` | `78761266-69ba-47fa-8aeb-39f0aa95998e` | `5bd2ddc2-4af9-4881-9f22-ab7e5b0f809b` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083207_5bd2ddc2-4af9-4881-9f22-ab7e5b0f809b.png) |
| 12 | `miu-shiraishi-soul-v1-5img-20260904` | `270c31fa-afd4-4609-b9d5-7302745f137c` | `e4c1624d-42d6-4f38-be45-6a743a71024a` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082300_e4c1624d-42d6-4f38-be45-6a743a71024a.png) |
| 13 | `kanon-komori-soul-v1-6img-20260904` | `642ba554-6f87-4be9-9aa7-4b66529b4995` | `20402217-8dad-4d59-855b-c9af90d43c68` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082338_20402217-8dad-4d59-855b-c9af90d43c68.png) |
| 14 | `jia-seo-soul-v1-5img-20260904` | `ecf19246-c697-419c-b978-fe9373586c19` | `f19c0721-8912-450c-a1ce-7ee1804ecf4c` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082337_f19c0721-8912-450c-a1ce-7ee1804ecf4c.png) |
| 15 | `emma-kao-soul-v1-5img-20260904` | `4374a074-fb89-45be-b80f-30cd78fea451` | `2e540fbc-c55c-47af-ac2a-0258767e6992` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082339_2e540fbc-c55c-47af-ac2a-0258767e6992.png) |
| 16 | `angeline-kwee-soul-v1-5img-20260904` | `a1802330-65a7-43d7-89d3-84aacca67bfa` | `3b70d793-f8d3-4fdf-8585-980cd8d19278` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083206_3b70d793-f8d3-4fdf-8585-980cd8d19278.png) |
| 17 | `angel-chiu-soul-v1-5img-20260904` | `6e638286-be57-45fa-961e-51bde6cba87f` | `8ca951a1-dc56-4384-9b19-c9e3c6cd8aa1` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082337_8ca951a1-dc56-4384-9b19-c9e3c6cd8aa1.png) |
| 18 | `zhiyi-shen-soul-v1-5img-20260904` | `8b1e0a44-1c7b-4b65-b878-be428d00e4b8` | `0bc68540-2a44-48c3-a773-88bf78c12711` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083207_0bc68540-2a44-48c3-a773-88bf78c12711.png) |
| 19 | `cheryl-soh-soul-v1-5img-20260904` | `6d4c90b5-bd40-4c2c-9c1d-c689702863e1` | `352a5879-7275-4fb5-a1b6-7b33859a258a` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082338_352a5879-7275-4fb5-a1b6-7b33859a258a.png) |
| 20 | `nico-tsai` | `46d1e11e-92a7-4fd7-8776-dcd4e2067627` | `ccc82d2e-e874-441f-a987-3582a0142220` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082339_ccc82d2e-e874-441f-a987-3582a0142220.png) |
| 21 | `sofia-hsu-v4b` | `214931ed-f411-421f-bf13-3c3a8d590ce5` | `103d48d8-ca3a-41a1-a8b2-ed2133bb6d3c` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083207_103d48d8-ca3a-41a1-a8b2-ed2133bb6d3c.png) |
| 22 | `Luna Tanaka v2` | `a3dc13ec-16e7-4990-89c6-9e0461db46ef` | `abd8b297-3461-4616-9929-45e201007ffa` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082338_abd8b297-3461-4616-9929-45e201007ffa.png) |
| 23 | `Rainie Hsu v2` | `a4a000fe-fd96-4c36-97ff-0df9358a9b47` | `9021734e-c0d4-4c2f-b174-12fe0bc79689` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083346_9021734e-c0d4-4c2f-b174-12fe0bc79689.png) |
| 24 | `Vicky Lin` | `bdb1d879-da36-4c1a-bc63-9f5b49a3e94e` | `14d841c1-d3fd-4286-ac91-8750c02033ed` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082339_14d841c1-d3fd-4286-ac91-8750c02033ed.png) |
| 25 | `Sophia Tseng` | `192562bb-ca64-4615-9515-13d34807857c` | `b7de3f95-9eb2-4105-9c02-79da6416c5c8` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082402_b7de3f95-9eb2-4105-9c02-79da6416c5c8.png) |
| 26 | `Coco Wu` | `cf7045dc-4e69-4c56-9621-aa8c40bf39b4` | `83f0a242-ab14-4ee0-88c8-2a022c436eb9` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083345_83f0a242-ab14-4ee0-88c8-2a022c436eb9.png) |
| 27 | `Zoe Lai` | `27f750e6-0d32-43ce-8249-cce94ef835cd` | `001fd7e1-c43f-406f-b6bf-4ad40511924b` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083346_001fd7e1-c43f-406f-b6bf-4ad40511924b.png) |
| 28 | `Rainie Hsu (v1)` | `994e33d2-7df1-47da-8478-7a6fd849fa33` | `2fbbe0bd-ad47-4f2e-bfd4-ce1a26115f86` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082404_2fbbe0bd-ad47-4f2e-bfd4-ce1a26115f86.png) |
| 29 | `Mia Huang` | `e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4` | `55e4e154-95e1-42dc-8b0c-d5107af27bae` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082403_55e4e154-95e1-42dc-8b0c-d5107af27bae.png) |
| 30 | `Camille Dupont` | `f19dafcc-5bc8-4d8f-af1d-ee48084ac398` | `c1609655-6c1b-4463-afb8-41dc14ee89e7` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082402_c1609655-6c1b-4463-afb8-41dc14ee89e7.png) |
| 31 | `Aaliya Rivera` | `97f5c6cd-1c0c-4432-83d0-dd42210ecada` | `59be55ab-62f5-4ae0-b3eb-43b333a724ce` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083346_59be55ab-62f5-4ae0-b3eb-43b333a724ce.png) |
| 32 | `Yuna Kim` | `235794a5-2eff-45fb-91b4-3232910afefa` | `ec1583f2-5d10-4563-82f3-ffdc208df5e1` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083345_ec1583f2-5d10-4563-82f3-ffdc208df5e1.png) |
| 33 | `Ananya Kapoor` | `fac82296-8c69-4c34-b352-1b398c8b8e1c` | `edaea5d3-a01f-48b9-bfac-9165e6a3abf9` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083347_edaea5d3-a01f-48b9-bfac-9165e6a3abf9.png) |
| 34 | `Luna Tanaka (v1)` | `1bfab2ce-cfa5-4026-93fa-e5c91b469c7a` | `fd9853e5-d2c1-4913-a8b7-3cde18e43e82` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_083346_fd9853e5-d2c1-4913-a8b7-3cde18e43e82.png) |
| 35 | `Iris Chen` | `5fe3b6ba-1277-4822-9141-fb06eb3b93a0` | `f7e815ae-f0e4-478d-9916-07fe0d2e76e4` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_082404_f7e815ae-f0e4-478d-9916-07fe0d2e76e4.png) |
## 5. 張數與實際花費

- 生成：35 張（35 個 Soul 各 1 張）。交付：35 張（含 2 張失敗樣本，見第 6 節）。
- 實際扣點：**4.20 點**（35 × 0.12）。依據：`balance` 生成前 3309.24 → 生成後 3305.04；`transactions` 列出 35 筆「Higgsfield Soul V2 −0.12」，時間 2026-10-08 08:23–08:33 UTC。
- 本批之前的唯讀查詢（餘額、角色列表、選項、`get_cost` 報價、`ai_influencer_prepare` 報價）沒有扣點。
- 事先查到但本批沒用的報價：AI Influencer 4 張角色表 4.5 點；`nano_banana_pro` 4 張 2 點；`gpt_image_2` 4 張 0.5 點。

## 6. 審查結果（依 `REFERENCE_AND_ACCEPTANCE.md` §4.1，執行者看圖的初步判讀；最後由製作師判定）

### 6.1 失敗樣本

| # | Soul | 問題 | 處理 |
|---|---|---|---|
| 3 | wendy-yeo | 閉眼，無法比對眼型 | 保留；需要時重生 1 張（0.12 點） |
| 24 | Vicky Lin | 閉眼 | 同上 |
| 23 | Rainie Hsu v2 | 半閉眼、頭髮未夾起、帶自拍介面 | 保留；#28 是同一人的 v1，可先用 #28 比對 |

### 6.2 共通問題

- `soul_2` 偏 UGC 風格，約 20 張出現假的社群平台介面、浮水印或假文字（prompt 已寫 avoid 仍出現）。這不影響看臉，但形象照階段要換模型或加強排除，否則違反 §4.1 第 8 項「畫面沒有可讀的假文字」。
- 2026-09-04 那批（#1、#2、#5、#6、#8、#10、#11、#13、#14、#16、#17）彼此相近：鵝蛋臉、大雙眼皮眼、小鼻、相近下顎，符合舊專案紀錄的「模型預設美女臉」收斂現象。**這一群最多只能選 1–2 個**，而且要和其他入選者並排再比一次。
- 同一人多版本：#23／#28（Rainie Hsu）、#22／#34（Luna Tanaka）、#21 與失敗的 sofia-hsu-v4。選用時各只算一個身分。
- 看起來偏年輕：#22 Luna v2、#26 Coco Wu、#29 Mia Huang。入選的話成年外觀檢查要更嚴。
- 非東亞外貌：#30 Camille Dupont、#31 Aaliya Rivera、#33 Ananya Kapoor。架構圖沒有限制族裔；人設包以台灣為背景。用不用由製作師決定。

### 6.3 執行者看到的區隔度較高的臉（供挑選參考，不是定案）

#4 wanyin-jiang（長臉、眼窩深）、#7 somi-oh（圓臉、單眼皮感、淺髮）、#9 rin-ayase（圓柔、眼小）、#12 miu-shiraishi（混血感、眉色淺）、#15 emma-kao（長臉、眼細、成熟）、#18 zhiyi-shen（曬色、方下顎）、#19 cheryl-soh（白皙、下顎線明顯、唇豐）、#20 nico-tsai（圓潤、鄰家）、#21 sofia-hsu-v4b（微曬、臉寬、眼細）、#27 Zoe Lai（成熟、臉寬、有膚質）、#32 Yuna Kim（窄臉）、#34 Luna v1（圓臉成熟）、#35 Iris Chen（溫暖、親切）。

## 7. 執行者的配對建議（依架構圖的格子；每格 2–3 個候選，由製作師或客戶選）

| 格子 | 架構圖的人設 | 建議候選 | 說明 |
|---|---|---|---|
| A 兩性話題 | 敢聊、說真話的女生 | #15 emma-kao、#4 wanyin-jiang、#32 Yuna Kim | 成熟、眼神穩的臉 |
| B 大尺度 Cos | 性感 Cos 角色（扮演） | #19 cheryl-soh、#12 miu-shiraishi、#28 Rainie v1 | 五官立體，戴假髮、上舞台妝後仍認得出 |
| C 性感身材時尚 | 身材好、懂穿搭（本人） | #18 zhiyi-shen、#21 sofia-hsu-v4b、#28 Rainie v1 | 健康曬色；#28 與 B 互斥，只能用在一格 |
| T1 星座命理 | 愛算命的女生 | #9 rin-ayase、#25 Sophia Tseng、#35 Iris Chen | 柔和、溫暖 |
| T2 迷因梗圖 | 梗圖小編 | #20 nico-tsai、#26 Coco Wu、#7 somi-oh | 鄰家、親切；#26 要過成年檢查 |
| T3 電玩手遊 | 課金玩家 | #7 somi-oh、#29 Mia Huang、#13 kanon-komori | #29 要過成年檢查 |
| T4 AI 科技 | 愛玩新工具的科技宅 | #32 Yuna Kim、#16 angeline-kwee、#14 jia-seo | 俐落、冷靜 |
| T5 運動賽事／啦啦隊 | 職棒、NBA 球迷 | #21 sofia-hsu-v4b、#18 zhiyi-shen、#10 peggy-lee | 曬色、健康；與 C 互斥 |
| T6 攝影人像 | 外拍攝影師 | #27 Zoe Lai、#34 Luna v1、#4 wanyin-jiang | 成熟、有膚質 |
| T7 時事新聞 | 吃瓜第一線 | #35 Iris Chen、#15 emma-kao、#2 yerin-han | 精明、親切 |

規則：同一個 Soul 只能用在一格；#23／#28、#22／#34 各算一人；§6.2 的「相近群」最多選 1–2 個。十個定案後要做全部 45 組的撞臉並排比較。

## 8. 採用的身分參考圖 A／B

**尚未選定。** 本批沒有鎖定任何角色；A（臉）、B（全身）要等製作師或客戶從第 7 節挑選後才建立。

## 9. 需要製作師決定的事

1. 十個格子各選哪一個 Soul（或退回要求重生／改用 AI Influencer 新生）。
2. 候選由製作師自己選，還是交客戶選；交客戶的話用什麼格式。
3. 圖片檔要不要提交到 repo（本批只提交文字與連結；對照表 JPG 存在執行者端，可以補交）。
4. #3、#24 要不要重生。
5. 非東亞外貌的三個 Soul 要不要納入候選。
6. 選定後的人設文字（名字、背景、§10 限制）怎麼處理：沿用人設包改性別、重寫、或由製作師另提。
7. 每批點數上限（本批執行者自設 100 點封頂，實際用 4.20 點）。

## 10. 需要客戶確認的事（依製作師與客戶的流程）

- T2／T3／T4／T6 由男性改為女性（和客戶 2026-10-07 接受的人設不同）。
- 十個角色改用現有 Soul 的臉，不是人設包的新臉。
- 架構圖本身沒有要改的地方；以上兩點是圖上沒有、依製作師說法可改的設定。

## 11. 本批沒有做的事

沒有訓練 Soul、沒有建立 Element、沒有上傳任何圖片、沒有做身分測試或形象照、沒有修改 `persona_pack_v1/` 與 `review/`、沒有推到 main 或別人的分支、沒有建立社群帳號或發布任何內容。
