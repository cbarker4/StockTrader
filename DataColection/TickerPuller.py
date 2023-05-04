"""
Caleb Barker
3/27/2023
This file is going to be pulling data from finhub: https://finnhub.io/dashboard 
I have a key stored in a file called AccountFile account_file is a tracked version 
so that it is easier to replicate if you want

Uses UNIX TIME STAMP 
c: Close 
h: High
l:low
o:Open
s:Status
t:Timestamp
v:Volume

Requirements:
finnhub-python
"""


import finnhub
import json
import pandas as pd 
import datetime 
import time
import math


# distanceBettweenYears= 1679986800-1648450800
def lastYearOfData(ticker):
    """
    input: Stock ticker string 
    output: A CSV of that stocks data for the last year
    """
    unixYear= 31536000
    list_text = open("AccountFile.json",'r').readlines()
    json_text = ""
    for val in list_text:
        json_text= json_text + val
    keys = json.loads(json_text)

    finnhub_client = finnhub.Client(api_key=keys["finnkey"])
    today = datetime.date.today()
    todayUnix=int(time.mktime(today.timetuple()))
    lastYearUnix= todayUnix - unixYear

    res = finnhub_client.stock_candles(ticker, 'D',lastYearUnix,todayUnix)
    df = pd.DataFrame(res)
    df.to_csv("Data/"+ticker+".csv")

def today(ticker,daysago=0):
    list_text = open("AccountFile.json",'r').readlines()
    json_text = ""
    for val in list_text:
        json_text= json_text + val
    keys = json.loads(json_text)

    finnhub_client = finnhub.Client(api_key=keys["finnkey"])
    today = datetime.date.today()
    todayUnix=int(time.mktime(today.timetuple()))
    todayUnix = todayUnix - (86400 * daysago)
    yesterdayUnix= todayUnix - 86400 

    res = finnhub_client.stock_candles(ticker, '1',yesterdayUnix,todayUnix)
    df = pd.DataFrame(res)
    df.to_csv("Data/todays/"+ticker+".csv")

def thisday(ticker,todayUnix):
    list_text = open("AccountFile.json",'r').readlines()
    json_text = ""
    for val in list_text:
        json_text= json_text + val
    keys = json.loads(json_text)

    finnhub_client = finnhub.Client(api_key=keys["finnkey"])
    today = datetime.date.today()
    # todayUnix=int(time.mktime(today.timetuple()))
    # todayUnix = todayUnix - (86400)
    yesterdayUnix= todayUnix + 86400 
    print("Day:",end=" ")
    print((math.floor(todayUnix/86400)+4 )% 7)
    if ((math.floor(todayUnix/86400)+4 )% 7) == 5:
        yesterdayUnix = (86400 *3) + yesterdayUnix
    if ((math.floor(todayUnix/86400)+4 )% 7) == 6:
        yesterdayUnix = (86400 *2) + yesterdayUnix
    if ((math.floor(todayUnix/86400)+4 )% 7) == 7:
        yesterdayUnix = (86400 *1) + yesterdayUnix

    res = finnhub_client.stock_candles(ticker, '1',todayUnix,yesterdayUnix)
    # print(res)
    df = pd.DataFrame(res)
    df.to_csv("Data/todays/"+ticker+".csv")


def twenty_four(ticker):
    list_text = open("AccountFile.json",'r').readlines()
    json_text = ""
    for val in list_text:
        json_text= json_text + val
    keys = json.loads(json_text)

    finnhub_client = finnhub.Client(api_key=keys["finnkey"])
    today = datetime.date.today()
    todayUnix=int(time.mktime(today.timetuple()))
    todayUnix = int(time.time())
    yesterdayUnix= todayUnix - 86400 

    res = finnhub_client.stock_candles(ticker, '1',yesterdayUnix,todayUnix)
    df = pd.DataFrame(res)
    df.to_csv("Data/todays/"+ticker+".csv")
    return True




def pull_hi(ticker):
    if ".csv" in ticker:
        ticker = ticker.replace(".csv","")


    list_text = open("AccountFile.json",'r').readlines()
    json_text = ""
    for val in list_text:
        json_text= json_text + val
    keys = json.loads(json_text)

    finnhub_client = finnhub.Client(api_key=keys["finnkey"])
  
    todayUnix= int(time.time())
    todayUnix = 1683212400 - 86400
   
    yesterdayUnix= todayUnix - (3600*3) 

    res = finnhub_client.stock_candles(ticker, '1',yesterdayUnix,todayUnix)
    df = pd.DataFrame(res)
    df.to_csv("Data/todays/"+ticker+".csv")
    
    pass
# def todays_data_till_now():
#     list_text = open("AccountFile.json",'r').readlines()
#     json_text = ""
#     for val in list_text:
#         json_text= json_text + val
#     keys = json.loads(json_text)

#     finnhub_client = finnhub.Client(api_key=keys["finnkey"])
#     today = datetime.date.today()
#     todayUnix=int(time.mktime(today.timetuple()))
#     todayUnix = todayUnix - (86400)
#     yesterdayUnix= todayUnix - 86400 

#     res = finnhub_client.stock_candles(ticker, '1',yesterdayUnix,todayUnix)
#     df = pd.DataFrame(res)
#     df.to_csv("Data/todays/"+ticker+".csv")
    




# all_tickers = open("DataColection/nasdaq_tickers.txt").readlines()
# start = open("DataColection/lastpulled.txt").read()
# print(start)
# skip = True
# for val in all_tickers:
#     if start in val:
#         print("val")
#         skip = False
   
#     if not skip:
#         try:
#             val = val.replace("\n","")
#             lastYearOfData(val)
#             open("DataColection/lastpulled.txt",'w').write(val)
#             time.sleep(1.1)
#             print(val)
#         except:
#             pass




