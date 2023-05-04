import streamlit as st
from DataColection import TickerPuller
import mypytable
import plotly.graph_objects as go
import pandas as pd
st.write("""
# Stock Trader



Recomended stocks to trade: 
""")
mt = mypytable.MyPyTable()
# todayfile = open("Results/TodayStocks.txt")
# todaysStocks = todayfile.readlines()
last_pull = open("Results/pulltime.py").readline()
print(last_pull)
mt.load_from_file("Results/TodayStocks.csv")

todaysStocks = mt.get_column("Ticker")
for val in todaysStocks:   ### TODO: fill this file with the five stock that the model returns
    st.write(val)
    mt = mypytable.MyPyTable()
    if False:
        TickerPuller.today(val.replace(".csv",""))
    # mt.load_from_file("Data/todays/"+val)
    # price = {}

  
    df = pd.read_csv("Data/todays/"+val)

    fig = go.Figure(data=[go.Candlestick(x=df['t'],
                open=df['o'],
                high=df['h'],
                low=df['l'],
                close=df['c'])])
    

       

    
    # plt.figure()
    

 
    

    st.plotly_chart(fig)
        
    
