# 執行者規則（給 Claude）

## 每一輪的最終回報，結尾一定要附「給 ChatGPT 主管的覆核 prompt」

- 每次提交、推送後的最終回報，最後一段固定是完整的主管覆核 prompt，用**一個** ```text 程式碼區塊包住全文，讓 Penny 一鍵複製。
- 不用等 Penny 提醒。大改、局部補正、小修都一樣，每一輪都要附。
- prompt 必須自成一體（主管只看這段也能開始覆核），至少包含：
  1. Repo、分支、本次 HEAD SHA、內容 commit SHA、上一次主管覆核的 commit SHA，以及看改動用的 `git diff <基準> <HEAD>`；
  2. 本輪範圍與限制：Penny 指示的重點、本輪沒做的事、全部是 PROPOSED、Penny 未回答不等於同意、主管不代替 Penny 選角；
  3. 必讀檔案與章節；
  4. 執行者回報的驗證證據，並註明「請獨立核對，不要直接採信」；
  5. 執行者自列的未解事項；
  6. 逐項要主管判定的問題（PASS／REVISE／BLOCK＋理由＋要改的地方）；
  7. 輸出方式：回寫檔名、commit 回同一分支、不 force push、不改寫既有 commit；無法 commit 時輸出完整 Markdown，由 Penny 貼回 repo。
- prompt 裡的 SHA 一律用推送後實際查到的值（`git rev-parse HEAD` 與遠端一致之後）。

## 其他固定規則

- 不修改主管覆核文件（`review/REVIEW_RESPONSE_*`）；不 force push，不改寫歷史。
- 完成指定範圍後停下，等 Penny 與主管；不自行進入製作或發布。
- 其餘規則見 `README.md` 的「Repo 規則」。
