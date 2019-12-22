import pandas as pd
import oandapy
import datetime
from datetime import datetime, timedelta
import pytz

account_id = '3622295'
api_key = '69347320cb5ea6ead051e52e7cdcd39f-7bb97a70d113451bddbba9f33feaef79'

oanda = oandapy.API(environment="practice", 
                    access_token=api_key)
res = oanda.get_prices(instruments="USD_JPY")
print(res)

def iso_to_jp(iso):
    date = None
    try:
        date = datetime.strptime(iso, '%Y-%m-%dT%H:%M:%S.%fZ')
        date = pytz.utc.localize(date).astimezone(pytz.timezone("Asia/Tokyo"))
    except ValueError:
        try:
            date = datetime.strptime(iso, '%Y-%m-%dT%H:%M:%S.%f%z')
            date = date.astimezone(pytz.timezone("Asia/Tokyo"))
        except ValueError:
            pass
    return date

def date_to_str(date):
    if date is None:
        return ''
    return date.strftime('%Y/%m/%d %H:%M:%S')

 
print(iso_to_jp(res['prices'][0]['time']))

# 1分足に変更してレートを取得してみる
res_hist_1m = oanda.get_history(instrument="USD_JPY", granularity="M1")
 
# データフレーム形式へ変換
res_hist_1m = pd.DataFrame(res_hist_1m['candles'])
 
# 日付をISOから変換
res_hist_1m['time'] = res_hist_1m['time'].apply(lambda x: iso_to_jp(x))
res_hist_1m['time'] = res_hist_1m['time'].apply(lambda x: date_to_str(x))
 
# 最初の5行を確認してみよう
print(res_hist_1m)
