# 地震通知程式 搭配地牛Wake Up以及中央氣象署api
一個簡易的地震通知程式
配合地牛wake up，在收到地震預警後將訊息傳送到Discord，並在該地震的報告產生後也傳到Discord當中

使用Discord Webhook，在地震將要發生時傳預警訊息到Discord文字頻道
之後再透過中央氣象屬提供的api來將該次地震報告傳送

## 使用方法
1. 安裝python3以及地牛wake up
2. 需要有以下套件：
   - sys
   - requests
   - time
   - os
   - io
   - datetime
   - discord
   - discord_webhook
   - python_dotenv
3. 將discord_webhook的網址以及中央氣象署的api還有城市資訊放進`.env`檔裡面
   ```py
   discord_webhook_url = https://discord.com/api/webhooks/.....
   earthquake_api = CWB-...
   city = 花蓮縣
   area = 花蓮市
   ```
   * discord_webhook在伺服器->整合->Webhook可以建立 並且他只會傳送訊息到指定的文字頻道
   ![image](https://github.com/judeabc20221/Taiwan_discord_earthquake_notify/assets/67894118/6c8bea43-4c3e-4c4a-9cc5-f76dce66c1e1)

   * 中央氣象署註冊網址：https://pweb.cwa.gov.tw/emember/register/authorization
   * 註冊後從這裡登入：https://opendata.cwa.gov.tw/userLogin
     - 點擊取得授取碼即可拿到api金鑰

   城市對應在地牛wake up所選的區域
   ![image](https://github.com/judeabc20221/Taiwan_discord_earthquake_notify/assets/67894118/82bfbc16-66b2-404e-85bf-98c6f22c813f)

5. 設定地牛wake up發生地震時執行`notify.bat`，並且僅執行一次建議打開

## 執行成果
![image](https://github.com/judeabc20221/Taiwan_discord_earthquake_notify/assets/67894118/37f721d2-1b52-471d-9c5f-7f7ba24bf211)

