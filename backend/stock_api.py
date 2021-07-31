import yfinance as yf
from args import make_args

class stock_api:
    def __init__(self):
        self.args = make_args()

    def split_into_batches(self, tickers):
        # split stocks into batches and request api by
        # ticker batches to shave execution time
        i = 0
        stockArray = tickers.split(" ")
        n = len(stockArray)
        batches = []

        while(i < n-(n % self.args.batchSize)):
            b = []
            for x in range(0,self.args.batchSize):
                b.append(stockArray[i+x])
            batches.append(b)
            i+=self.args.batchSize

        # append remainder number of tickers
        batches.append(stockArray[n-(n % self.args.batchSize):])

        return batches

    def get_close_curr_ticker_list(self, tickers):
        batches = self.split_into_batches(tickers)
        for i, batch in enumerate(batches):
            tcks = ' '.join([b for b in batch])
            if i == 0:
                # build DataFrame structure with first itteration
                infoContainer = yf.download(tcks, period='2d', interval='1d')
            else:
                infoContainer = infoContainer.join(yf.download(tcks, period='2d', interval='1d'))

        return infoContainer['Close']