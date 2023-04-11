
from sklearn.neighbors import KNeighborsClassifier
import os
import copy
import mypytable as mypy
import numpy as np
from sklearn.model_selection import train_test_split


for best in range(41,100):
    print(best)
    stockfiles= os.listdir("/home/cbarker4/Documents/DataScience/StockTrader/Data")
    X_train = []
    Y_train=[]
    X_test=[]
    Y_test=[]
    Xlast=[]


    for j,val in enumerate(stockfiles):
        # print(val)
        

        mt = mypy.MyPyTable()
        mt.load_from_file("/home/cbarker4/Documents/DataScience/StockTrader/Data/"+val)
        mt.drop_column('v')
        mt.drop_column('t')
        mt.drop_column('s')
        mt.drop_column('h')
        mt.drop_column('l')
        mt.drop_column('o')

        mt.drop_column(0)
        
        i = best

        while i < len(mt.data)-1:
            

            table = mt.create_sub_table(i-best,i)
            big = table.max()
            little = table.min()
            try:
                table = table.normalize(intiger=True)
            except:
                break
            

        
            # print(table.data[0])

            if i < (len(mt.data)/8)*7.5:
            # if i < len(mt.data)-2:
                X_train.append(copy.deepcopy(table.get_column(0)))
                # Xlast.append(table.data[-1])
                num = int(int((((mt.get_row(i+1)[0])-little))/(big-little)*1000)/10)
                Y_train.append(num)
            else:
                    X_test.append(copy.deepcopy(table.get_column(0)))
                    # Xlast.append(table.data[-1])
                    num = int(int((((mt.get_row(i+1)[0])-little))/(big-little)*1000)/10)
                    Y_test.append(num)


            i+=1


    # X = np.array(X)
    # Y = np.array(Y)

    # count = 0
    # X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=.25 ,random_state=10)
    # print(X_train)
    # data = list(zip(X_train,Y_train))
    for neighbors in range(1,7):
        knn = KNeighborsClassifier(n_neighbors=neighbors)
        knn.fit(X_train,Y_train)
        # print(len(X_train))
        # print(len(X_test))

        for val in X_test:
            Xlast.append(val[-1])
        # print(Xlast)
        y_pred = knn.predict(X_test)
        correct = 0
        removed = 0
        falsepos = 0
        pos = 0
        neg=0
        falseneg =0
        for i,val in enumerate(Y_test):
            if Xlast[i]!=y_pred[i]:
                if Xlast[i] > val:

                    if Xlast[i]>y_pred[i]:
                        pos+=1
                        correct+=1
                    else :
                        neg+=1
                        falseneg+=1
                
                else:
                    if Xlast[i]<y_pred[i]:
                        correct+=1 
                        neg+=1
                    else:
                        pos+=1
                        falsepos+=1
            else:
                removed+=1
        out = open("/home/cbarker4/Documents/DataScience/StockTrader/Optimisation/Results/knn.csv",'a')
        out.write(str(best)+",")
        out.write(str(neighbors)+",")
        out.write(str(correct / (len(y_pred)-removed)))
        out.write(",")
        out.write(str((pos-falsepos)/pos))
        out.write(",")
        out.write(str((neg-falseneg)/neg))
        out.write("\n")
        out.close()


