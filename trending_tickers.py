import pandas as pd
import yahooquery as yq
from yahooquery import Ticker
'''
This code creates a trending_ticker.csv file of the trending tickers on yahoo finance and their Pre-market percent change
'''
# Get the list of trending tickers
data = yq.get_trending()
# Create empty lists
tick_list = []
pct_change_list = []
# Iterate for every item in the trending ticker list
for item is data['quotes']:
  # Store symbol in format 'AAPL'
  symbol = str(item['symbol'])
  # Create ticker object for each symbol in trending stock data
  ticker = Ticker(symbol)
  # Store value of each ticker
  values = ticker.price[symbol]
  # Append symbol and pre market percent change to lists
  tick_list.append(symbol)
  pct_change_list.append(values['preMarketChangePercent'])

# Create a dictionary in a pandas df for tickers and pct_change and save it to a csv
dict = {'ticker' : tick_list, 'pct_change' : pct_change_list}
df = pd.DataFrame(dict)
df.to_csv('trending_tickers.csv')
