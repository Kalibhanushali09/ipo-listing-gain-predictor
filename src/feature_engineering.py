import pandas as pd
import numpy as np
import yfinance as yf

def extract_date_features(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df = df.drop(columns=['Date'])
    return df

def add_nifty_return(df):
    nifty = yf.download('^NSEI', start='2010-01-01', end='2025-12-31')
    nifty_close = nifty['Close']

    def get_nifty_return(date):
        try:
            end_price = nifty_close.asof(date)
            start_price = nifty_close.asof(date - pd.Timedelta(days=14))
            return ((end_price - start_price) / start_price * 100).iloc[0]
        except:
            return None

    df['Nifty_14d_Return'] = pd.to_datetime(df['Date']).apply(get_nifty_return)
    return df

def drop_leakage_columns(df):
    cols_to_drop = ['List Price', 'Total', 'CMP(BSE)', 'CMP(NSE)', 
                    'Current Gains', 'IPO_Name']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
    return df

def engineer_features(df):
    df = drop_leakage_columns(df)
    df = add_nifty_return(df)
    df = extract_date_features(df)
    return df