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

print(time.mktime(today.timetuple()))

res = finnhub_client.stock_candles('AAPL', 'D',lastYearUnix,todayUnix)
df = pd.DataFrame(res)
df.to_csv("First_Data.csv")


distanceBettweenYears= 1679986800-1648450800
print(distanceBettweenYears)

