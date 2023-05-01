class portfolio:
    def __init__(self):
        self.cash = 0
        self.stocks = []
        self.live = False

    def buy_stock(self,ticker):
        self.stocks.append(ticker)

    