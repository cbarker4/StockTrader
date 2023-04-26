import finnhub
import json 
import datetime
import time
import pandas as pd
def today(ticker):
    list_text = open("/home/cbarker4/Documents/DataScience/StockTrader/AccountFile.json",'r').readlines()
    json_text = ""
    for val in list_text:
        json_text= json_text + val
    keys = json.loads(json_text)

    finnhub_client = finnhub.Client(api_key=keys["finnkey"])
    today = datetime.date.today()
    todayUnix=int(time.mktime(today.timetuple()))
    86400
    yesterdayUnix= todayUnix - 86400

    res = finnhub_client.stock_candles(ticker, '1',yesterdayUnix,todayUnix)
    df = pd.DataFrame(res)
    df.to_csv("Data/todays/"+ticker+".csv")
