import pandas as pd

stock = "2330"

url = "https://goodinfo.tw/tw/StockDetail.asp?STOCK_ID=" + stock

getdata = pd.read_html(
    url, # 想爬取的網址
    encoding='utf-8',  #如何編碼爬取下來的資料
    header=0,
)
print(getdata)