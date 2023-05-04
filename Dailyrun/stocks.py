import Portfolio
from Narrowing import knn 
from Narrowing import price
from DataColection import TickerPuller

import mypytable
import copy
from Narrowing import adr
from Narrowing import volume

def run():
    user = Portfolio.portfolio()

    user.cash=100




    colnames = ["Ticker","price_to_buy","owned"]
    outresults = mypytable.MyPyTable()
    outresults.load_from_file("Results/TodayStocks.csv")
    for val in range(5):
        outresults.drop_rows(-1)
        print("Here")
    for val in range(len(outresults.data)):
        outresults.data[val][2] =1 



    recomended= knn.knnPicks()
    up = open("Results/Goingup.txt",'w')  
    rec = copy.deepcopy(recomended)
    for val in rec:
        val = val.replace(".csv","\n")
        up.write(val)
    up.close()





    inbudget = price.inbudget(recomended,user.cash,5)

    good_volume = volume.remove_by_volume(inbudget,250000,250000)

    stocks= adr.best_daily_range(good_volume,5)

    for name in stocks:
        name = name.replace(".csv","")
        outresults.data.insert(0,[name,0,0,0])


    outresults.save_to_file("Results/testing.csv")