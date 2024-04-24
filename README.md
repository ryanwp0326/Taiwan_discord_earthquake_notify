# Taiwan_discord_earthquake_notify
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
   - discord_webhook
3. 將discord_webhook的網址以及中央氣象屬的api放進`.config`檔裡面
   ```py
   discord_webhook_url = "https://discord.com/api/webhooks/....."
   earthquake_api = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/..."
   ```
4. 設定地牛wake up發生地震時執行`notify.bat`，並且僅執行一次建議打開

## 執行成果
![image](https://github.com/judeabc20221/Taiwan_discord_earthquake_notify/assets/67894118/c7d3f142-12ee-4280-a04d-5ac0ca89e0e8)
