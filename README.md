# 俄羅斯方塊棋盤分析器 - 初始版本

## 項目簡介

這是一個用於分析類似俄羅斯方塊遊戲棋盤和方塊的Python程序的初始版本。目前，該程序僅實現了棋盤定義和各種方塊形狀的初始化功能。

## 當前功能

- 自定義棋盤狀態輸入
- 預定義多種方塊形狀
- 嘗試擺放積木

## 使用方法

-  注意！當前程序可能無法正常使用
1. 運行程序
2. 按提示輸入當前棋盤狀態（8x8的0和1組成的字符串）
3. 程序會初始化棋盤和預定義的方塊形狀
4. 程序會自動偵測可擺放位址

## 主要函數

- `init()`: 初始化預定義的方塊形狀
- `set_pan()`: 設置初始棋盤狀態
- `can_place`:尋找可擺放位址

## 預定義方塊類型

程序目前包含以下類型的預定義方塊：
- 方形方塊（如：3x3, 2x2, 1x1）
- I型方塊（各種長度）
- L型方塊（包括鏡像和旋轉變體）
- T型方塊
- 水平線型方塊（各種長度）

## 注意事項

- 這是初始版本，僅包含基本的棋盤和方塊定義功能
- 當前版本不包含遊戲策略分析功能

## 後續計劃

未來版本將實現方塊放置邏輯和最佳位置分析功能。

## 貢獻

歡迎提出建議或改進意見。您可以來分享您的想法。

- discord:`shihte`