import pandas as pd
import numpy as np
import json
import requests
import datetime
import time


def Get_StockPrice(Symbol, Date):

    url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={Date}&stockNo={Symbol}'
    print(url)
    data = requests.get(url).text
    json_data = json.loads(data)

    Stock_data = json_data['data']

    StockPrice = pd.DataFrame(Stock_data, columns = ['Date','Volume','Volume_Cash','Open','High','Low','Close','Change','Order'])

    StockPrice['Date'] = StockPrice['Date'].str.replace('/','').astype(int) + 19110000
    StockPrice['Date'] = pd.to_datetime(StockPrice['Date'].astype(str))
    StockPrice['Volume'] = StockPrice['Volume'].str.replace(',','').astype(float)/1000
    StockPrice['Volume_Cash'] = StockPrice['Volume_Cash'].str.replace(',','').astype(float)
    StockPrice['Order'] = StockPrice['Order'].str.replace(',','').astype(float)

    StockPrice['Open'] = StockPrice['Open'].str.replace(',','').astype(float)
    StockPrice['High'] = StockPrice['High'].str.replace(',','').astype(float)
    StockPrice['Low'] = StockPrice['Low'].str.replace(',','').astype(float)
    StockPrice['Close'] = StockPrice['Close'].str.replace(',','').astype(float)

    StockPrice = StockPrice.set_index('Date', drop = True)


    StockPrice = StockPrice[['Open','High','Low','Close','Volume','Change']]
    print(StockPrice)
    return StockPrice

if __name__ == '__main__':   
    Symbol = '2330'
    Dates = pd.date_range(start = '2023-01-01', end = '2023-03-01', freq = 'MS').astype(str)

    data = Get_StockPrice(Symbol, Dates[0].replace('-',''))

    for Date in Dates[1:]:
        # print(Date)
        try:
            data = pd.concat([data,Get_StockPrice(Symbol, Date.replace('-',''))], axis = 0)
            time.sleep(5)
        except:
            pass
    print(data)