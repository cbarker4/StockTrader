import os
import pandas as pd
import numpy as np
import mypytable as mypy
from sklearn.model_selection import train_test_split
import copy


class StanderdStock:
    def __init__(self,stockname=None):
        self.mt = mypy.MyPyTable()
        if stockname!= None:
            if ".csv" in stockname:
                self.mt.load_from_file("/home/cbarker4/Documents/DataScience/StockTrader/Data/"+stockname)
            else:
                self.mt.load_from_file("/home/cbarker4/Documents/DataScience/StockTrader/Data/"+stockname + ".csv")
            # self.mt.drop_column('v')
            # self.mt.drop_column('t')
            # self.mt.drop_column('s')
            # self.mt.drop_column('o')
            # self.mt.drop_column(0)
        
    def Hi_mean_std(self):
        open = self.mt.get_column('o')
        high = self.mt.get_column('h')
        results = []
        X = []
        for i,val in enumerate(open):
            X.append(high[i]-val)
        results.append(sum(X)/len(X))
        results.append(np.std(X))
        return results
    
    def Low_mean_std(self):
        open = self.mt.get_column('o')
        low = self.mt.get_column('l')
        results = []
        X = []
        for i,val in enumerate(open):
            X.append(low[i]-val)
        results.append(sum(X)/len(X))
        results.append(np.std(X))
        return results
    
    def load_stock(self,stockname): 
        self.mt = mypy.MyPyTable()
        if stockname!= None:
            if ".csv" in stockname:
                self.mt.load_from_file("/home/cbarker4/Documents/DataScience/StockTrader/Data/"+stockname)
            else:
                self.mt.load_from_file("/home/cbarker4/Documents/DataScience/StockTrader/Data/"+stockname + ".csv")
            # self.mt.drop_column('v')
            # self.mt.drop_column('t')
            # self.mt.drop_column('s')
            # self.mt.drop_column('o')
            # self.mt.drop_column(0)

        


     




