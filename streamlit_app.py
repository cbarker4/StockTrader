import streamlit as st
from DataColection import TickerPuller
import mypytable
import plotly.graph_objects as go
import pandas as pd
import time 
# st.write("""
# # Stock Trader



# ## Recomended stocks to trade: 
# """)


st.set_page_config( 
    page_title="Hello",
    page_icon="👋",
)
# st.sidebar.success("Select a demo above.")
page = st.sidebar.selectbox('Select page',['Predictor','Trader']) 
if page =='Trader':
    st.write("# Stock Trader")
    st.write("## Recomended stocks to trade: ")
    mt = mypytable.MyPyTable()
    # todayfile = open("Results/TodayStocks.txt")
    # todaysStocks = todayfile.readlines()
    last_pull = open("Results/pulltime.py").readline()
    print(last_pull)
    mt.load_from_file("Results/TodayStocks.csv")

    todaysStocks = mt.get_column("Ticker")
    first = True
    for i,val in enumerate(mt.data):   ### TODO: fill this file with the five stock that the model returns
        # st.write(val[0].replace(".csv",""))
        # mt = mypytable.MyPyTable()
        if True:
            try:
                print(TickerPuller.twenty_four(val[0].replace(".csv","")) )
                time.sleep(1.1) 
        
    
        
        
                df = pd.read_csv("Data/todays/"+val[0] + ".csv")

                fig = go.Figure(data=[go.Candlestick(x=df['t'],
                            open=df['o'],
                            high=df['h'],
                            low=df['l'],
                            close=df['c'])])
                        
                if val[2] == 1 and first:
                    st.write("## Stocks to sell if bought yesterday")
                    first = False
                st.write(val[0].replace(".csv","")) 
                st.plotly_chart(fig)
                if val[2] == 0:
                    st.write("Price to buy in at: " + str(val[1]))

            
                
                if val[2] == 1:
                    st.write("Price to Sell at: " + str(val[3]))
                
            except:
                pass    
        
                

else:   
    st.write("### What stock would you like to know if it will go up")
    text = st.text_input("Enter ticket ex. AAPL")
    out = False
    if text:
        stocks = open("Results/Goingup.txt").readlines()
        for val in stocks:
            if text in val:
                st.write("This stock will go up")
                out= True
                break
        if not out:
            st.write("Your Guess is better than ours we promis")
        



      
    # plt.figure()
    

 
    

 
        
    
