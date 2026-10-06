# 證據總索引（Evidence Index）

- 更新日期：2026-10-06
- 規則：
  - 每個 EV 編號都對應一個實際打開過的來源；
  - 沒有打開過的來源不列入；
  - 主張要寫「這個來源支持什麼」，不寫來源沒說的推論。
- 編號：
  - EV-C：客戶提供
  - EV-S：LUSCENA 網站
  - EV-R：參考 repo
  - EV-T：Threads 帳號樣本
  - EV-M：Meta 官方
  - EV-X：其他公開來源

## EV-C 客戶提供

| EV | 來源 | 日期 | 支持的主張 |
|---|---|---|---|
| EV-C01 | `brief/source/client_brief_2026-10-06.jpg`（SHA-256 `f2a96368…4173129`） | 2026-10-06 | 全部 CR-xxx 需求（逐字稿見 `brief/CLIENT_IMAGE_TRANSCRIPT.md`） |

## EV-S LUSCENA 網站

詳細說明在 `research/LUSCENA_AUDIT.md` §11，這裡只列索引。

| EV | URL | 查核日期 | 支持的主張 |
|---|---|---|---|
| EV-S01 | https://www.luscena.com/ | 2026-10-06 | 年齡確認、首頁結構、頁尾標語「亞洲最懂你的成人娛樂平台」、營運主體、未登入可見露骨標題、GA4 與 Dcard Pixel |
| EV-S02 | https://www.luscena.com/about | 2026-10-06 | 「現場性愛表演」「私秀表演，視訊聊天」 |
| EV-S03 | https://www.luscena.com/service | 2026-10-06 | 會員制、代幣、一人一帳號、台灣法律與臺中地院、主體名稱不一致 |
| EV-S04 | https://www.luscena.com/privacy | 2026-10-06 | 蒐集項目、僅限 18 歲以上 |
| EV-S05 | https://www.luscena.com/legal-2257-statement | 2026-10-06 | 2257 聲明；保管人地址缺漏 |
| EV-S06 | https://www.luscena.com/live-stream ／ /posts ／ /video ／ /shorts/179 | 2026-10-06 | 內容分類與存取層級 |
| EV-S07 | https://www.luscena.com/Vivian07 ／ /Aurora08 | 2026-10-06 | 創作者頁功能；API 欄位 `is_ai_creator`、價格欄位 |
| EV-S08 | 前端 API `POST /api/payment/gift-pack-items` | 2026-10-06 | 鑽石包的 TWD 與 USDT 價格 |
| EV-S09 | https://support.luscena.com/hc/zh-tw/articles/17843863964303 | 2026-10-06 | 鑽石用途、付款方式、不退款 |
| EV-S10 | https://support.luscena.com/hc/zh-tw/articles/17843848337551 | 2026-10-06 | 內容存取層級；免費直播不用登入 |
| EV-S11 | https://support.luscena.com/hc/zh-tw/articles/17843826762383 | 2026-10-06 | 註冊流程；註冊後要重新登入 |
| EV-S12 | https://support.luscena.com/hc/zh-tw/articles/17843837870479 | 2026-10-06 | 已驗證會員：信用卡扣 1 元 |
| EV-S13 | https://support.luscena.com/hc/zh-tw/articles/17843826753167 | 2026-10-06 | 「給成年人的直播與內容平台」；LP-0 候選 |
| EV-S14 | https://support.luscena.com/hc/zh-tw/articles/17843838026383 | 2026-10-06 | 創作者 App 不在應用程式商店 |
| EV-S15 | https://host.luscena.com/sign/in/contract | 2026-10-06 | 創作者收益說明；同意書年齡條款互相矛盾 |
| EV-S16 | 網路請求紀錄（UTM 測試） | 2026-10-06 | UTM 保留；GA4 與 Dcard 事件 |
| EV-S17 | `research/screenshots/*.png` | 2026-10-06 | 年齡確認、註冊視窗、語言選單 |

## EV-R 參考 repo（唯讀）

來源：https://github.com/pennyhuang-oss/Virtual_KOL_Studio
- 分支：`claude/luscena-kol-initial-draft-et17t8`
- commit：`c6c3512448571846918e99445b8a1e081a45d7e1`，和 `origin/main` 相同
- 完整檔案清單見 `research/REFERENCE_METHODS.md` §0.1

| EV | 檔案 | 支持的主張 |
|---|---|---|
| EV-R01 | `PERSONA_CANON.md` | 撞臉統計（41/171 組）；「撞臉只能改骨架」；人設被鎖在單一場景 |
| EV-R02 | `review/soul_pilot/VERDICT_collision_v1.md` | cheryl ↔ zhiyi 遮髮盲測 6/8 |
| EV-R03 | `BATCH3_FACE_INVARIANT.md`、`FACE_CROP_PIPELINE.md` | 真人來源被認出；QA 缺少審美維度 |
| EV-R04 | `kols/*/content_style.md`、`profile.json` | 支柱比例不同步（合計 140%、130%）；schema 驗證失敗 |
| EV-R05 | `review/soul_training/ACCEPTANCE_LOCKED.md` | 事前鎖定門檻、V1–V6、誠實的狀態分級 |
| EV-R06 | `CALIBRATION_TEST.md` | 指定台北，輸出卻是首爾街景 |
| EV-R07 | `WARDROBE_SYSTEM.md` | 四轉盤；「系統有效」只依據 2 張圖 |

## EV-X 其他公開來源

| EV | URL | 查核日期 | 支持的主張 |
|---|---|---|---|
| EV-X01 | https://cna.com.tw/news/aipl/202608200078.aspx（中央社，2026-08-20） | 2026-10-06（已開啟全文） | 原文：「今年九合一地方選舉11月28日投票，將選出1萬1051名地方公職人員」。文中提到公投案還在審議，**沒有寫公投的投票日**；公投是否同日舉行待查核 |

## EV-T、EV-M（Threads 樣本與 Meta 官方）

這兩類的完整查核紀錄見下方附錄，原文出自 `research/THREADS_RESEARCH.md`。
