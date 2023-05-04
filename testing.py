from Predicting import HiFinder
def get_sell(ticker,opn):
    past = HiFinder.StanderdStock(ticker) 
    avg, std = past.Low_mean_std()
    print(avg-std)
    print (opn+(avg - std))


get_sell("XELA",.033)