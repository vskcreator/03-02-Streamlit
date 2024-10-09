import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

# Загрузка списка тикеров S&P 500 с сайта Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
table = pd.read_html(url)
sp500_tickers = table[0]
st.write('## List of stocks from SP500')
st.write(sp500_tickers)
stock_chooser_button = st.selectbox('Choose the ticker of the stock you would like to see on the graphs',sp500_tickers := table[0]['Symbol'].to_list())

# 1. Write title
st.title('Single stock price information')
# 2. Closing price and volume
st.write('Provided graphs for ***Closing price*** and ***Volune***')
# define ticker symbol
tickerSymbol = stock_chooser_button
#get data on defined ticker
tickerData = yf.Ticker(tickerSymbol)
# upload the historical prices for the defined ticker
tickerDf = tickerData.history(period='1d', start='2010-1-31', end='2024-10-8')
# Open  High    Low     Close   Volume  Dividends   Stock Splits
st.write(f'''
## Closing price ~ {tickerSymbol}''')
st.line_chart(tickerDf.Close)
st.write(f'''
## Volume Price ~ {tickerSymbol}
''')
st.line_chart(tickerDf.Volume)