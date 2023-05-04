class portfolio:
    def __init__(self):
        self.cash = 0           #  amount of money on hand
        self.stocks = []        # stocks I am currently in
        self.live = False
        self.liquid = {}        # how many i own
        self.owned ={}
        self.price = {}         # what i paid to buy it 
        self.profits = 0

    def buy_stock(self,ticker):
        self.stocks.append(ticker)

    