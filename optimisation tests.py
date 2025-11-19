import yfinance as yf
import pandas as pd

aapl = yf.Ticker('aapl')

aapl_historical = aapl.history(start='2025-01-01',end='2025-06-01', interval='1d', actions = False)  ## gets apple stock data for six month period

print (type(aapl_historical))
print (type(aapl.info))


