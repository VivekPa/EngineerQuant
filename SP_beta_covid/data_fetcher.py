import pandas as pd 
import numpy as np 
import yfinance as yf


# #tickers = ['AIR', 'COST', 'KO', 'XOM', 'GE', 'ADS', 'AAPL', 'AMZN', 'FB', 'MSFT', 'DAL', 'AAL', 'UAL', 'TSCO']
# tickers = ['OXY', 'BA', 'SLB', 'SPG', 'AIG', 'COP', 'GE', 'XOM', 'WFC', 'GM', 'AIR.PA', 'KO', 'TSCO', 'DAL', 'AAL', 'UAL']
# # sp100 = pd.read_csv('sp100_list.csv')
# # print(sp100['tickers'])

# period = '9mo'
# interval = '1d'
# for i in tickers:
#     data = yf.download(i, period=period, interval=interval)
#     print(f'{i} data downloaded...')
#     data.to_csv(f'raw_data/{i}_{period}_{interval}.csv')
#     print(f'{i} data saved...')


# data = yf.download('AIR.PA', period=period, interval=interval)
# data.to_csv(f'raw_data/AIR.PA_{period}_{interval}.csv')
# print(data.tail())

def get_data(tickers, interval, start, end):
    full_prices = pd.DataFrame()
    for i in tickers:
        df = yf.download(i, interval=interval, start=start, end=end)['Adj Close']
        print(f'{i} data downloaded...')
        #df.to_csv(f'raw_data/{i}_{start}_{end}_{interval}.csv')
        #print(f'{i} data saved...')
        #df.index = np.arange(len(df))
        
        full_prices = pd.concat([full_prices, df], axis=1, sort=False)

    full_prices.columns = tickers
    #print(full_prices.shape)
    #full_prices.head()   
    return full_prices