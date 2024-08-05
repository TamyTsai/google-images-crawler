from selenium import webdriver
import time
# Explicit Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Keys 模擬鍵盤
from selenium.webdriver.common.keys import Keys
# 路徑
import os
# 下載爬到的資料
import wget

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# 等待網頁載入
# 等到name屬性值為q的HTML標籤(搜尋輸入框)出現，才繼續執行其他動作
query = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# 清空輸入框預設值
query.clear()

# 關鍵字
keyword = '請輸入關鍵字'

# 於搜尋輸入框輸入關鍵字
query.send_keys(keyword)
# 按下ENTER搜尋
query.send_keys(Keys.RETURN)

# 等待搜尋結果出現(分頁標籤出現)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "YmvwI"))
)

# 點擊圖片分頁
img_query = driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div')
img_query.click()

# 等待跳轉圖片搜尋結果分頁
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "YQ4gaf"))
)


# 視窗捲到底 讓更多圖片被載入 捲2次
for i in range(2):
    # 執行js程式碼
    # 將視窗捲到 x座標為0 y座標為視窗高度處(原點位於視窗左上角)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 等到更多圖片被載入
    time.sleep(5)

# 搜尋結果圖片們
imgs = driver.find_elements(By.CLASS_NAME,'YQ4gaf')

# for img in imgs:
#     print(img.get_attribute('src'))

# 存放下載下來的圖片之資料夾
path = os.path.join(keyword)
# 以搜尋關鍵字為資料夾名稱，建立資料夾(如果資料夾還沒建立的話)
if not os.path.exists(path):
    os.mkdir(path)

count = 0
# for img in imgs:
#     # 路徑 檔案名稱
#     save_as = os.path.join(path, keyword + str(count) + '.jpg')
#     # 下載(圖片網路位置，圖片要下載到本機哪裡)
#     wget.download(img.get_attribute('src'), save_as)
#     count += 1

for img in imgs:
    # 抓取圖片下載URL
    src = img.get_attribute('src')

    # 檢查下載來源URL的有效性
    if src and src.startswith('http'):
        print(f"由此下載圖片: {src}")
        # 路徑 檔案名稱
        save_as = os.path.join(path, keyword + str(count) + '.jpg')
        # 下載(圖片網路位置，圖片要下載到本機哪裡)
        wget.download(src, save_as)
        count += 1
    # 過濾掉非HTTP(S)的連結(開頭非http:資料URL或無效連結)
    else:
        print(f"無效的圖片來源網址: {src}")


time.sleep(60)