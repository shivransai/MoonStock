import math
import itertools
from backend import stock_api
from args import make_args

class percent_change:
    def __init__(self):
        f = open('./backend/stocks.txt', 'r')
        self.stocks = {}
        self.tickers = f.read()
        self.args = make_args()

    def set_all_percent_change(self):
        # get close of prev day and curr price for all tickers
        api = stock_api.stock_api()
        closeOpenList = api.get_close_curr_ticker_list(self.tickers)

        for column in closeOpenList:
            close = closeOpenList.iloc[0][column]
            open = closeOpenList.iloc[1][column]

            # account for tickers that are passed as NULL from api
            if math.isnan(close) or math.isnan(open):
                continue

            # calculate percent change and round to 2 decimals
            self.stocks[column] = round(((open-close)/close)*100, 2)

    def set_stocks_to_decending_order(self):
        # sort by value (percent change)
        self.stocks = dict(sorted(self.stocks.items(), key=lambda item: item[1], reverse=True))
        return

    def get_stock_by_listSize(self):
        return dict(itertools.islice(self.stocks.items(), self.args.listSize))

    def get_highest_positive_movers(self):
        self.set_all_percent_change()
        self.set_stocks_to_decending_order()
        return self.get_stock_by_listSize()






