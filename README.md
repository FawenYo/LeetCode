# LeetCode 解題紀錄

![latest-commit-date](https://img.shields.io/badge/latest--commit--date-2021%2F04%2F11-brightgreen)

## 簡介

本專案為紀錄 LINE 群組 LeetCod刷刷鍋 之LeetCode解題思維。

使用語言為 Python 3.8.3 64-bit 版本。

**目前僅會更新該週必寫&選寫內容**，暫時不考慮附上額外寫的題目！

## 自動取得題目 (Python3)

### 示意圖

![Example Image](https://i.imgur.com/lhOzv5K.png)

### 操作步驟
:heavy_exclamation_mark: 其中 步驟 1 只需下載一次，日後只需重複 步驟2 和 步驟3

1. 下載 `question.py` 和 `model.py` 兩檔案

    您可以使用 `git clone` 指令直接下載專案內容，或者您也可以直接複製 question.py 和 model.py 的內容到自己電腦上 (請注意檔案名稱一定要相同！)

2. 編輯 `question.py`

    請分別設定 Line 143 和 144 `DATE` 和 `OPTIONAL`

    `DATE` 是作業截止日期，格式為 `年-月-日`。

    `OPTIONAL` 為是否要獲取選寫題，預設為 `True`。

3. 執行 `question.py`

    程式會自動創建題目的資料夾，包含 `QUESTION.MD` (題目敘述) 和 `{question}.py` (Python3 程式碼)

    若程式發現該題目資料夾已存在便會自動跳過，不會有複寫到原本內容之疑慮。

## 題目更新紀錄

### 2021/03/28

| 必寫題                                                                                                 | 選寫題                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [1. Two Sum](1.%20Two%20Sum/README.md)<br>[13. Roman to Integer](13.%20Roman%20to%20Integer/README.md) | [7. Reverse Integer](7.%20Reverse%20Integer/README.md)<br>[9. Palindrome Number](9.%20Palindrome%20Number/README.md)<br>[38. Count and Say](38.%20Count%20and%20Say/README.md) |

### 2021/04/04

| 必寫題                                                                                                                     | 選寫題                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [20. Valid Parentheses](20.%20Valid%20Parentheses/README.md)<br>[53. Maximum Subarray](53.%20Maximum%20Subarray/README.md) | [21. Merge Two Sorted Lists](21.%20Merge%20Two%20Sorted%20Lists/README.md)<br>[3. Longest Substring Without Repeating Characters](3.%20Longest%20Substring%20Without%20Repeating%20Characters/README.md)<br>[5. Longest Palindromic Substring](5.%20Longest%20Palindromic%20Substring/README.md) |

### 2021/04/11

| 必寫題                                                                                                                                                                                                                   | 選寫題                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [101. Symmetric Tree](101.%20Symmetric%20Tree/README.md)<br>[104. Maximum Depth of Binary Tree](104.%20Maximum%20Depth%20of%20Binary%20Tree/README.md)<br>[337. House Robber III](337.%20House%20Robber%20III/README.md) | [136. Single Number](136.%20Single%20Number/README.md)<br>[15. 3Sum](15.%203Sum/README.md)<br>[19. Remove Nth Node From End of List](19.%20Remove%20Nth%20Node%20From%20End%20of%20List/README.md) |
