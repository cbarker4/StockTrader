class portfolio:
    def __init__(self):
        self.cash = 0
        self.stocks = []
        self.live = False
        self.liquid = {}
        self.owned ={}
        self.price = {}
        self.profits = 0

    def buy_stock(self,ticker):
        self.stocks.append(ticker)

    