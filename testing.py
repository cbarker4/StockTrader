todayfile = open("Results/TodayStocks.txt")
todaysStocks = todayfile.readlines()
print(todaysStocks)
for val in todaysStocks:
    print(val)
