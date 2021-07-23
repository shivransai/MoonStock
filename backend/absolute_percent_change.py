import csv
import yfinance as yf
import pandas
from datetime import date

class absolute_percent_change:
    def __init__(self):
        self.stocks = {}
        with open('./backend/stocks.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].isalpha():
                    self.stocks[row[0]] = 0

    def setAllPercentChange(self):
        for ticker, percentChange in self.stocks.items():
            self.stocks[ticker] = self.getTickerPercentChange(ticker)
        self.rankAllStocks()

    def getTickerPercentChange(self, ticker):
        open,close = self.getTickerOpenClose(ticker)
        return round(((close-open)/open)*100, 2)

    def getTickerOpenClose(self, ticker):
        try:
            infoContainer = yf.download(ticker, period='1d', interval='1d')
            currDate = date.today().strftime("%Y-%m-%d")
            return infoContainer.at[currDate, 'Open'], infoContainer.at[currDate, 'Close']

        except:
            return 1,1


    def rankAllStocks(self):
        sorted(self.stocks, key=self.stocks.get, reverse=True)

    def get_highest_movers(self):
        self.setAllPercentChange()
        high_movers = {}
        limit = 0
        for key, val in self.stocks.items():
            if limit == 16:
                break
            high_movers[key] = val
            limit+=1
        return high_movers