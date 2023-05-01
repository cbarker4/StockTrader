"""
Calculate the average daily range
formula:
sum the values of how much an asset moved from the high to low in a day for 21 days and then divide by 21
"""
import mypytable
from operator import itemgetter



def best_daily_range(stocks,amount_of_stocks,days=None):
    avg = []
    for i,val in enumerate(stocks):
        mt = mypytable.MyPyTable()
        mt.load_from_file("Data/" + val)
        diffrence = []
        if len(mt.data)>22:
            if days== None:
                start = -1
            else:
                start = mt.get_row_index(6,days[i])
                print(start)
            j=0
            while j > -21:
                row = mt.get_row(start -j)
                
                diffrence.append(row[2]-row[3])
                j-=1
            
            avg.append([sum(diffrence)/len(diffrence),i])

    avg = sorted(avg,key=itemgetter(0),reverse=True)
    
    for f,val in enumerate(avg):
        print(val[0],stocks[avg[f][1]])

    
    good =[]
    for val in range(amount_of_stocks):
        good.append(stocks[avg[val][1]])

    return good
        
    
    

            

