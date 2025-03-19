import pandas as pd
import yfinance as yf

def load_data(stock_symbol, start="2010-01-01", end="2024-01-01"):
    df = yf.download(stock_symbol, start=start, end=end)
    df = df[['Close']]  # We only need closing price
    return df
