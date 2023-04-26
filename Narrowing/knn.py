from sklearn.neighbors import KNeighborsClassifier
import os
import copy
import mypytable as mypy
import numpy as np
from sklearn.model_selection import train_test_split

def knnPicks(yesterday=False):
    stockfiles= os.listdir("/home/cbarker4/Documents/DataScience/StockTrader/Data")
    X_train = []
    Y_train=[]
    X_test=[]
    Y_test=[]
    Xlast=[]
    index = stockfiles.index("todays")
    stockfiles.pop(index)
    # print(len(stockfiles))
    tickers=[]
    count =0
    for j,val in enumerate(stockfiles):
        #Load each stock and remove unnecisary data
        mt = mypy.MyPyTable()
        mt.load_from_file("/home/cbarker4/Documents/DataScience/StockTrader/Data/"+val)
        mt.drop_column('v')
        mt.drop_column('t')
        mt.drop_column('s')
        mt.drop_column('h')
        mt.drop_column('l')
        mt.drop_column('o')
        mt.drop_column(0)

        # Needs enough data to be called on an indevidual stock
        if len(mt.data)<=101:
            # print(count)
            count+=1
        else:
            tickers.append(val)

        
        i = 100

        while i < len(mt.data)-1:
            table = mt.create_sub_table(i-100,i)
            big = table.max()
            little = table.min()
            table = table.normalize(intiger=True)
            
            if yesterday == False:
                if i < (len(mt.data)-2):
                # if i < len(mt.data)-2:
                    X_train.append(copy.deepcopy(table.get_column(0)))
                    # Xlast.append(table.data[-1])
                    num = int(int((((mt.get_row(i+1)[0])-little))/(big-little)*1000)/10)
                    Y_train.append(num)
                else:
                    num = int(int((((mt.get_row(i+1)[0])-little))/(big-little)*1000)/10)
                    temp = copy.deepcopy(table.get_column(0))
                    X_train.append(copy.deepcopy(temp))
                    Y_train.append(num)
                    temp.pop(0)
                    temp.append(num)
                    X_test.append(temp)
            
            else:
                if i < (len(mt.data)-3):
                # if i < len(mt.data)-2:
                    X_train.append(copy.deepcopy(table.get_column(0)))
                    # Xlast.append(table.data[-1])
                    num = int(int((((mt.get_row(i+1)[0])-little))/(big-little)*1000)/10)
                    Y_train.append(num)
                else:
                    num = int(int((((mt.get_row(i+1)[0])-little))/(big-little)*1000)/10)
                    temp = copy.deepcopy(table.get_column(0))
                    X_train.append(copy.deepcopy(temp))
                    Y_train.append(num)
                    temp.pop(0)
                    temp.append(num)
                    X_test.append(temp)

                    
   


            i+=1


    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train,Y_train)
    # print(len(X_train))
    # print(len(X_test))




    for val in X_test:
        Xlast.append(val[-1])
    # print(Xlast)
    y_pred = knn.predict(X_test)
    # print(len(X_test))
    correct = 0
    removed = 0
    falsepos = 0
    pos = 0
    neg=0
    falseneg =0
    bad = []
    good = []
    noChange = []
    print(count)
    print(len(y_pred))
    print(len(tickers))
    print(len(stockfiles))

    for i,val in enumerate(y_pred):       
        if Xlast[i]!=y_pred[i]:
            if Xlast[i] > val:
                bad.append(tickers[i])
            else:
                good.append(tickers[i])        
        else:
            noChange.append(tickers[i])  
    # print(good)         
    # print(len(good))
    return good