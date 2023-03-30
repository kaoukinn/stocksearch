import pandas as pd
import numpy as np
import json
import requests

url = 'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20230101&stockNo=2002&response=json&_=1680094519671'

data = requests.get(url).text
json_data = json.loads(data)
Stock_data = json_data['data']
StockPrice = pd.DataFrame(Stock_data, columns = ['Date','成交股數','成交金額','開盤價','最高價','最低價','收盤價','漲跌價差','成交筆數'])

print(StockPrice)