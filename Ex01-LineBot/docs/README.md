# Line Bot

> 搭建 Line Bot 聊天機器人

# Demo






# Line



# Heroku

## 佈署專案
* 將寫好的應用程式佈署至Heroku
    ```
    $ heroku login  #登入Heroku

    #初始化專案 (just one time)
    $ git init  
    $ heroku git:remote -a bot_sticker.py

    #更新專案
    $ git add .
    $ git commit -m "bot_sticker.py"
    $ git push heroku master
    ```


# 檔案架構

## 檔名：Procfile
* 定義專案程式類型和主程式名稱，讓Heroku知道如何配置與啟動此專案。
* 告訴Heroku如何執行程式
* 檔名P 規定大寫
* Flask網站程式，屬於web類型，執行環境使用gunicorn





## 檔名：requirements.txt
* 列舉執行專案程式所需的程式庫套件和版本
* 描述程式運作時所需要的套件
* 儲存於專案原始碼的根目錄
* 佈署Python前的準備工作：產生requirements.txt檔
  * 安裝佈署專案程式前，需先列舉所需的程式庫名稱和版本。
  * 利用pip工具程式的freeze命令，自動產生專案的相依套件版本清單。


## 檔名：runtime.txt
* 指定專案的執行環境，Ex: Python 3.7.2
* 描述使用的python環境


## 檔名：bot_sticker.py

#### 使用 line-bot-sdk程式庫開發聊天機器人
##### 一個基本的 LINE bot程式，包含 4元素:
* 回應 & 發送訊息 的LinebotAPI (line_bot_api)
* 解讀 & 包裝訊息 的WebhookHandler物件 (handler)
* 接收 LINE伺服器傳入訊息的"/callback"路由
* 捕捉 LINE訊息事件的裝飾器 (decorator)



* 宣告 2個與Line相關的物件:
  1. LinebotAPI :  **操作**訊息 Ex: 回應or發送訊息
  2. WebhookHandler :  **處理**訊息  Ex: 解讀包裝訊息
     (1) 處理"/callback"請求
     (2) 確認請求來源是 LINE訊息服務器的路由程式
     補充: 取出HTTP金鑰欄位 & 內容本體


