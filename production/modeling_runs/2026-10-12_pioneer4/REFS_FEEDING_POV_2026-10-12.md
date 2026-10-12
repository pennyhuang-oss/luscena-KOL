# 參考素材登記：「餵鏡頭吃東西」（2026-10-12）

- 用途：Nanami（成熟溫柔少婦）餐桌餵食形象照的構圖參考。
- 規則（`REFERENCE_AND_ACCEPTANCE.md` §2）：所有含真人的圖**只當方向參考**（鏡位、手的位置、表情），**不放進生成輸入、不用於訓練**。
- 查核日：2026-10-12。網路搜尋結果：真正「第一人稱被餵」的照片在圖庫裡很少；多數是第三人稱情侶互餵。小紅書／IG 上的「男友視角餵食」多為個人貼文，無授權，只記連結不下載。

## A. 免費授權（Pexels License：可商用、免署名；仍不放進生成）

| # | Pexels ID | 內容 | 和目標的距離 |
|---|---|---|---|
| 1 | 6429506 | 情侶在床上共吃外帶麵，女方用筷子餵男方 | 第三人稱側拍 |
| 2 | 6429489 | 同上另一張 | 第三人稱 |
| 3 | 5088437 | 廚房裡女方餵男方 | 第三人稱、遠 |
| 4 | 4308157 | 女方用湯匙餵男友，笑 | 第三人稱，表情可參考（眼瞇帶笑） |
| 5 | 5225489 | 手餵男方熱狗 | 手從畫面外伸入，半 POV |
| 6 | 4833623 | 手餵男方披薩特寫 | 手從畫面外伸入，半 POV |
| 7 | 6578844 | **越肩視角**：女方拿食物伸向背對鏡頭的男方 | **最接近**：鏡頭在被餵者後方，女方手伸向前 |
| 8 | 7555854 | 女方餵男方炸物 | 第三人稱 |
| 9 | 5225283 | **越肩視角**：男方餵女方 | 鏡位可參考（反向） |
| 10 | 4989361 | 兩位女生野餐互餵 | 第三人稱 |

網址格式：`https://www.pexels.com/photo/<ID>/`。對照圖存在執行者端（`refs_sheet.jpg`），未提交 repo。

## B. 付費圖庫（只看預覽，不下載、不使用）

- Getty 1346386632「Feeding My Boyfriend Pizza」：說明文字明寫 **point of view shot**，女方的手拿披薩伸向鏡頭（被餵者視角）。https://www.gettyimages.com/detail/photo/feeding-my-boyfriend-pizza-royalty-free-image/1346386632
- Getty 859936596／860715352「Point of view of mom feeding baby with a spoon」：POV 鏡位示範（湯匙朝鏡頭），主題不同但鏡頭語言一樣。
- Getty「Woman feeding noodles with chopsticks to friend」系列（1487387558、2153542546、2249763709）：筷子夾麵伸向對方的手勢。
- Alamy 273203796：女生拿筷子直視鏡頭、手指指向鏡頭，正面直視的構圖。

## C. 免費素材站（需到站內搜尋；本次抓取被擋）

- 写真AC「あーん」搜尋：https://www.photo-ac.com/main/search?q=%E3%81%82%E3%83%BC%E3%82%93 （站內說明：個人商用皆可免費；需確認最新條款）
- Mixkit 免費影片：女生對著手機鏡頭玩筷子 https://mixkit.co/free-stock-video/a-cheerful-woman-play-with-the-chopsticks-to-the-camera-51245/ （Mixkit License 可商用）
- Pinterest 靈感板（無授權，只看）：Feeding Each Other https://www.pinterest.com/ideas/feeding-each-other/923670857619/ ；Feeding Someone Pose Reference https://www.pinterest.com/ideas/feeding-someone-pose-reference/951749213449/

## D. 從文章整理的「餵鏡頭」拍法（文字，可直接進 prompt）

- 鏡頭當男友：「把鏡頭當作是男友、閨蜜一樣互動……喂鏡頭吃一口」（beauty321 餐廳拍照 Pose 7）。
- 男友視角＝俯拍 25–45°：男生比女生高，從上往下看，人會顯得嬌小（壹讀「男友視角」）。
- 鏡頭略高於眼睛，雙手或食物往鏡頭送，視線看鏡頭（LINE Today 男友視角 10 招）。
- 食物當前景：手機 0.5 倍廣角、鏡頭離食物 5–10 cm，食物佔畫面下方三分之二，人放畫面中央避免廣角變形（韓國「食物視角」拍法）。

**prompt 要點**：`personal perspective / POV of the person being fed`、`camera slightly above her eye level looking down 30°`、`her hand with chopsticks extended straight toward the lens, food large in the foreground, slightly out of focus`、`other hand cupped under the chopsticks`、`eyes on the lens`。

## 來源
- https://www.beauty321.com/post/49005
- https://today.line.me/tw/v3/article/rm1gRjj
- https://read01.com/2GRaDzM.html
- https://www.pexels.com/search/feeding%20boyfriend/
- https://www.gettyimages.com/photos/woman-feeding-noodles-with-chopsticks
