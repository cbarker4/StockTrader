Testing = True

from DataColection import TickerPuller
import time
from Narrowing import knn




def main():

    all_tickers = open("DataColection/nasdaq_tickers.txt").readlines()
    if not Testing:
        """
        Bellow here we call and than procede to update all of our data from the stock market 
        """
        for val in all_tickers:
            try:          
                val = val.replace("\n","")
                TickerPuller.today(val)
                open("DataColection/lastpulled.txt",'w').write(val)
                time.sleep(1.1)
                print(val)
            except:
                pass
    


    """
    Using KNN I can narrow down the stock market to about 200 stocks 
    that i cna say 70 % will go up the next day 
    
    """
    if Testing:
        recomended = knn.knnPicks(yesterday=True)
    else:
        recomended = knn.knnPicks()
    print(recomended)
    
    if Testing:
        pass
    


if __name__ == "__main__":
    main()