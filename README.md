# 網頁爬蟲--自動下載google圖片
![image](https://github.com/user-attachments/assets/b8e15ea5-c1d5-422f-89fc-5df62e0cfd1f)

## 關於 網頁爬蟲--自動下載google圖片
- 根據指定關鍵字，自動從google幫你下載相關圖片

## 專案目的
- 藉由自動化操作，節省逐一下載相關圖片的時間

## 專案畫面與功能介紹
### 指定要搜尋的圖片關鍵字
  
```bash
# 關鍵字
keyword = '請輸入關鍵字'
```

<hr>

### 執行程式碼，開始網頁自動化操作
- 系統自動開啟chrome瀏覽器，輸入指定之關鍵字並搜尋，接著跳轉圖片分頁搜尋結果
- 頁面會滑到底2次
- 自動下載頁面上已出現的圖片
  
![image](https://github.com/user-attachments/assets/7b229a8b-9d24-4dcc-b409-9de5b7fc4b8a)

<hr>

### 下載結果
- 系統自動建立以關鍵字為名之資料夾，以存放搜尋後下載完成之圖片
- 下載之圖片以關鍵字加序號命名
  
![image](https://github.com/user-attachments/assets/b8e15ea5-c1d5-422f-89fc-5df62e0cfd1f)


## 安裝
以下皆為於windows環境運行

### 檢查是否有安裝Python，若無，則至官網下載安裝
```bash
py --version
```

### 安裝Python延伸套件

### 檢查是否有安裝pip
```bash
py -m pip --version
```

### 安裝selenium(網頁自動化操作工具)
```bash
py -m pip install selenium
```

### 安裝wget(檔案下載工具)
```bash
py -m pip install wget
```

<!-- ## 資料夾及檔案說明
- -->

<!-- ## 專案技術
- Python v3.12.3
  - selenium
  - wget v3.2 -->

## 專案技術
- 程式語言：Python
- 框架：selenium
- 版本控制：Git

## 聯絡作者
你可以透過email與我聯絡：tamy8677@gmail.com

<i>最後更新：2024.8.5</i>
