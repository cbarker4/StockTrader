import mypytable
from Predicting import HiFinder
from DataColection import TickerPuller
import time



def run():
    open = 86400

    outresults = mypytable.MyPyTable()




    stocks = []
    outresults.load_from_file("Results/TodayStocks.csv")
    for row in outresults.data:
        if row[2] == 0:
            stocks.append(row[0])


    for name in stocks:
        TickerPuller.pull_hi(name)
        time.sleep(1.1)
        print(name)

        # outresults.data.insert(0,[name,str(start - (avg - std)),0])
        mt = mypytable.MyPyTable()
        mt.load_from_file("Data/todays/"+name)
        # print(mt)
        start = mt.get_column('o')[0]
        past = HiFinder.StanderdStock(name)

        avg = past.Low_mean_std()[0]
        std = past.Low_mean_std()[1]
        # print(avg,std)
        # mockrun = mt.get_column('o')
        # start = mockrun[0]
        outresults.data.insert(0,[name,str(start - (avg - std)),0,str((start - (avg - std))*1.1)])
        # mockrun.pop(0)


    # outresults.save_to_file("Results/testing.csv")
