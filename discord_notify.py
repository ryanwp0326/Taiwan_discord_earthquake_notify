import sys
import requests
import time
import os
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed

# 總等待秒數會是 wait_time * wait_seconds
# 有感地震發生後 等候地震報告的次數
wait_time = 30
# 每次未等到地震報告後 下一次抓取的間隔
wait_seconds = 30

# 拿取現在最新的地震報告id
def get_last_num():
    try:
        with open( "last_id.txt", 'r' ) as file:
            id = int( file.read() )
            return id
    except Exception as e:
        return None

# 將地震報告id更新
def write_last_num( id: int ):
    try:
        with open( "last_id.txt", 'w' ) as file:
            file.write( str( id ) )
    except Exception as e:
        return None

if __name__ == "__main__":
    load_dotenv()
    # discord webhook
    discord_webhook_url = os.getenv( "discord_webhook_url" )
    # 氣象資料開放平台api
    earthquake_data_url = os.getenv( "earthquake_api" )
    earthquake_data_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=" + earthQuake_data_url + "&limit=10&format=JSON"
    city = os.getenv( "city" )
    area = os.getenv( "area" )

    magnitude = str( sys.argv[1] ).replace( "+", "強" ).replace( "-", "弱" )
    second = str( sys.argv[2] )
    msg = f"{city}{area}預估震度：{ magnitude }級地震\n到達時間：{ second }秒"
    webhook = DiscordWebhook( url = discord_webhook_url, content = msg )
    execute = webhook.execute()

    # 更新檔案中的上個地震id
    response = requests.get( earthquake_data_url )
    if response.status_code == 200 :
        data = response.json()
        if data is not None and data["success"] == "true":
            now_data = data["records"]["Earthquake"][0]
            now_id = now_data["EarthquakeNo"]
            write_last_num( now_id )

    # 在新報告產生前 拿取上次地震的id
    last_id = get_last_num()
    for i in range( wait_time ):
        last_id = get_last_num()
        response = requests.get( earthquake_data_url )

        if response.status_code == 200 :
            data = response.json()

            if data is not None and data["success"] == "true":
                # 拿取目前最新的地震資訊
                now_data = data["records"]["Earthquake"][0]
                now_id = now_data["EarthquakeNo"]

                # 代表地震報告還未產生 先等候一段時間再抓取
                if now_id == last_id:
                    print( f"地震報告尚未發布，{wait_seconds}秒後再抓取一次\n" )
                    time.sleep( wait_seconds )
                # 新的報告已產生
                else:
                    embed = DiscordEmbed(
                        title = "地震報告",
                        description = now_data["ReportContent"],
                        color = 1940253,
                    )
                    embed.set_image( url = now_data["ReportImageURI"] )
                    embed.set_author( name = "地震速報", icon_url = "https://i.imgur.com/6I4Z7Rq.png" )
                    webhook = DiscordWebhook( url = discord_webhook_url )
                    webhook.add_embed( embed )
                    execute = webhook.execute()
                    write_last_num( now_id )
                    break
