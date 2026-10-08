# 身分測試 T1–T3（2026-10-08，定案十人）

- 目的：驗證每個 Soul 在正面、3/4 側、側面三個角度是否仍是同一個人（`REFERENCE_AND_ACCEPTANCE.md` §4.1 第 3 項）。
- 工具與模型：Higgsfield MCP `generate_image_batch`，`soul_2`（`text2image_soul_v2`），`aspect_ratio=3:4`、`quality=1.5k`，各人附自己的 `soul_id`（見 `SELECTION_2026-10-08.md`；T1 為 Nanami Fujiwara）。
- 參考圖：無上傳；身分來源只有 Soul。
- 張數：30 張（10 人 × 3 角度），全部完成，無失敗工作。
- 實際扣點：**3.60 點**（30 × 0.12）。餘額 3304.80 → 3301.20。本批累計 **8.04 點**。
- 提交分五輪（方案限制同時 8 個工作）。

## prompt（三個角度只換第一句的角度描述）

```text
Identity check photo of this woman, {angle}. Head and shoulders, eye level. Hair tucked behind both ears so the forehead, eyebrows, ears and jawline are fully visible. Bare face or very light makeup, no eyeliner, natural lip color. Neutral expression, mouth closed, eyes open. Plain heather-gray crew-neck T-shirt, no jewelry, no glasses. Even soft studio light, no colored light, no strong shadows. Plain medium-gray seamless background. Unretouched realistic photography with natural skin texture. Keep her face exactly the same person. Avoid: beauty filter, heavy makeup, text, watermark, UI overlay, closed eyes.
```

- angle 1：`front-facing, looking straight into the camera`
- angle 2：`three-quarter view, head turned about 45 degrees to her own left, eyes toward the camera`
- angle 3：`full profile view, head turned 90 degrees to her own left, showing the left side of her face`

## 生成紀錄

| 角色 | 角度 | job_id | 結果 |
|---|---|---|---|
| A Wendy Yeo | 正面 | `0b64c3a7-99a6-40ef-89d6-da8f1e8066d4` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_093948_0b64c3a7-99a6-40ef-89d6-da8f1e8066d4.png) |
| A Wendy Yeo | 3/4 側 | `08f16aaa-4f30-48c7-8616-d11698f30337` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_093947_08f16aaa-4f30-48c7-8616-d11698f30337.png) |
| A Wendy Yeo | 側面 | `6e9f772d-878d-43c9-9708-2dd77992d43b` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_093948_6e9f772d-878d-43c9-9708-2dd77992d43b.png) |
| B Kanon Komori | 正面 | `ecf6739f-d24c-483a-884a-6536d2155152` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_093948_ecf6739f-d24c-483a-884a-6536d2155152.png) |
| B Kanon Komori | 3/4 側 | `94fd7535-4060-4ad0-8f9c-ecda70c0bcd5` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_093947_94fd7535-4060-4ad0-8f9c-ecda70c0bcd5.png) |
| B Kanon Komori | 側面 | `29e551fc-14a3-46ea-81aa-542e6f3dd8d9` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_093949_29e551fc-14a3-46ea-81aa-542e6f3dd8d9.png) |
| C Vicky Lin | 正面 | `0dee3f04-b1b6-4bc3-95f1-75af6a1f3d26` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_093947_0dee3f04-b1b6-4bc3-95f1-75af6a1f3d26.png) |
| C Vicky Lin | 3/4 側 | `d7d002ac-b1e7-4da6-8d89-8e193010193d` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094117_d7d002ac-b1e7-4da6-8d89-8e193010193d.png) |
| C Vicky Lin | 側面 | `5f1c24b6-f297-4d05-ae1a-86d5fc5eb34b` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094119_5f1c24b6-f297-4d05-ae1a-86d5fc5eb34b.png) |
| T1 Nanami Fujiwara | 正面 | `c619a3eb-69e3-4d89-9907-a8796de72ddd` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094118_c619a3eb-69e3-4d89-9907-a8796de72ddd.png) |
| T1 Nanami Fujiwara | 3/4 側 | `e6c3d9ce-0aac-467f-aa2b-a07ae9886268` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094117_e6c3d9ce-0aac-467f-aa2b-a07ae9886268.png) |
| T1 Nanami Fujiwara | 側面 | `05c0a8fc-9622-4853-8d34-219011dcfd34` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094119_05c0a8fc-9622-4853-8d34-219011dcfd34.png) |
| T2 Somi Oh | 正面 | `522e5018-f9f1-4332-8c82-f3e058a46241` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094118_522e5018-f9f1-4332-8c82-f3e058a46241.png) |
| T2 Somi Oh | 3/4 側 | `fd0f4358-b81b-4e90-86b2-1d05cfc1ddde` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094120_fd0f4358-b81b-4e90-86b2-1d05cfc1ddde.png) |
| T2 Somi Oh | 側面 | `7f72c60b-1937-4b02-91aa-7db3aff21cc1` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094249_7f72c60b-1937-4b02-91aa-7db3aff21cc1.png) |
| T3 Mia Huang | 正面 | `5f7dd962-b0fd-45b7-b36c-8ac1abe804f0` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094247_5f7dd962-b0fd-45b7-b36c-8ac1abe804f0.png) |
| T3 Mia Huang | 3/4 側 | `80442a89-90ff-4a52-b0e4-40defbac960d` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094248_80442a89-90ff-4a52-b0e4-40defbac960d.png) |
| T3 Mia Huang | 側面 | `5472a7a1-63e6-4f72-bcac-04d35fdad0e1` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094249_5472a7a1-63e6-4f72-bcac-04d35fdad0e1.png) |
| T4 Zhiyi Shen | 正面 | `d484ae92-b469-45ec-baa5-9953b407435b` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094249_d484ae92-b469-45ec-baa5-9953b407435b.png) |
| T4 Zhiyi Shen | 3/4 側 | `4c451d36-e0c6-4935-b7c0-100de15e1499` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094248_4c451d36-e0c6-4935-b7c0-100de15e1499.png) |
| T4 Zhiyi Shen | 側面 | `5b03ec2e-9cac-4a86-ba6d-139b723459d1` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094248_5b03ec2e-9cac-4a86-ba6d-139b723459d1.png) |
| T5 Yerin Han | 正面 | `58392c3a-1caa-4e3d-8fa9-6e80fd81eb7b` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094527_58392c3a-1caa-4e3d-8fa9-6e80fd81eb7b.png) |
| T5 Yerin Han | 3/4 側 | `faef2011-ae35-46fb-a672-d1cbfbf441e2` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094527_faef2011-ae35-46fb-a672-d1cbfbf441e2.png) |
| T5 Yerin Han | 側面 | `8c26e99b-e7f2-4a3f-91fe-bcad9c3d9bec` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094526_8c26e99b-e7f2-4a3f-91fe-bcad9c3d9bec.png) |
| T6 Miu Shiraishi | 正面 | `0eba74e1-fa36-4663-b381-4fc2620a3ab8` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094528_0eba74e1-fa36-4663-b381-4fc2620a3ab8.png) |
| T6 Miu Shiraishi | 3/4 側 | `7d72d6d9-2d8e-49b4-b1d2-0f2cf727fb5f` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094528_7d72d6d9-2d8e-49b4-b1d2-0f2cf727fb5f.png) |
| T6 Miu Shiraishi | 側面 | `2be4b6ce-71b2-4b59-93c1-ce3cda30aa45` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094527_2be4b6ce-71b2-4b59-93c1-ce3cda30aa45.png) |
| T7 Emma Kao | 正面 | `33fd40ff-95aa-4bfd-9cb5-cfde60f8979d` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094528_33fd40ff-95aa-4bfd-9cb5-cfde60f8979d.png) |
| T7 Emma Kao | 3/4 側 | `d44eb850-f689-41b0-8062-0c9e88f5d384` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094703_d44eb850-f689-41b0-8062-0c9e88f5d384.png) |
| T7 Emma Kao | 側面 | `824918b2-d219-462f-80f3-dac1214bd3cf` | [圖](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20261008_094702_824918b2-d219-462f-80f3-dac1214bd3cf.png) |

## 看圖結果（執行者人工判讀；最後由製作師判定）

| 角色 | 判定 | 說明 |
|---|---|---|
| A Wendy Yeo | **過** | 三個角度同一人；眼細長、顴骨、下顎線一致 |
| B Kanon Komori | **過** | 三個角度同一人 |
| C Vicky Lin | **過** | 三個角度同一人；膚色與唇形一致。側面圖頭上多了墨鏡（prompt 寫 no glasses 仍出現），不算身分漂移 |
| T1 Nanami Fujiwara | **過** | 三個角度同一人 |
| T2 Somi Oh | **過** | 三個角度同一人；髮色一致 |
| T3 Mia Huang | 過（註記） | 正面與 3/4 一致；側面眉毛變粗、臉頰較瘦，仍可認為同一人。之後側面鏡位要多看一次 |
| **T4 Zhiyi Shen** | **不過** | **正面與 3/4 側是另一個人**：膚色變白、五官變成混血感、淺色眼珠；側面才回到建角照（#18）的曬色與方下顎。這個 Soul 會在兩個身分之間跳 |
| T5 Yerin Han | **過** | 三個角度同一人 |
| T6 Miu Shiraishi | 可疑 | 正面與 3/4 和建角照（#12）一致（混血感、淺眉）；側面鼻型與眉毛偏東亞、眉色變深，像另一個人。側面要重測 |
| T7 Emma Kao | **過** | 三個角度同一人 |

共通現象：`soul_2` 幾乎每張都加上假的社群介面、帳號名、按鈕（prompt 寫 avoid 仍出現）。身分測試不受影響，但形象照階段必須處理（換模型、或生成後裁切）。

## 建議（由製作師決定）

1. **T4 Zhiyi Shen**：這個 Soul 不穩，不建議直接用。兩個做法：(a) 再生 3 張正面看是不是偶發（0.36 點）；(b) 直接換人，有 Soul 的替代：Angel Chiu（#17）、Cheryl Soh（#19）、Sophia Tseng（#25）。執行者傾向 (b)，因為就算這次穩，之後出圖每張都要盯。
2. **T6 Miu Shiraishi**：側面再生 2 張確認（0.24 點）。穩就過；不穩就限制側面鏡位或換人。
3. 其他八人通過，可以進形象照。

## 與人設包建議不同的地方

- 人設包建議低方案 T1–T3、中方案 T1–T8（含表情變化）。本批只做 T1–T3 三個角度，沒有做表情與造型變化；通過不代表換裝、換妝後也穩，那在形象照階段逐張檢查。

## 給主管覆核的 prompt（依 repo `CLAUDE.md` 規則存檔，不在對話中貼出）

```text
【Luscena KOL 建模 第 1 批 補充 3：身分測試 T1–T3】
- Repo：https://github.com/pennyhuang-oss/luscena-KOL；分支 producer/modeling-r1
- 本次 HEAD 與內容 commit：見本檔所在 commit（git log -1 -- production/modeling_runs/2026-10-08_batch1/IDENTITY_TEST_2026-10-08.md）
- 上一次主管覆核 commit：9b540cb4174d6ad52ba079fb1dd141503cbd98b4；本批前一次回報 HEAD：a7cc212e81cfd5d28e44a38470d6cb7697c652fb
- 範圍：30 張身分測試圖與人工判讀；沒有形象照、訓練、帳號。全部 PROPOSED；T4、T6 的處理待製作師決定；主管不代替製作師選角。
- 必讀：本檔全文；SELECTION_2026-10-08.md；REFERENCE_AND_ACCEPTANCE.md §4.1 第 3 項、§4.2。
- 驗證證據（請獨立核對）：30 個 job_id 與結果連結在本檔表格；餘額 3304.80 → 3301.20。
- 未解：T4 Soul 不穩；T6 側面可疑；soul_2 的假介面問題；表情與造型變化尚未測。
- 請判定：Q1 判讀方式（人工三角度）是否足以作為通過依據；Q2 T4 的處理建議（換人 vs 重測）是否合理；Q3 形象照階段對假介面的處理要求；Q4 是否應補表情變化測試再進形象照。
- 輸出：review/REVIEW_RESPONSE_MODELING_R1_BATCH1_IDTEST.md，commit 回同一分支，不 force push，不改既有 commit。
```
