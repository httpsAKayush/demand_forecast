# ...existing code...
"""
Minimal data loader for M5-like CSV files.
Functions:
- load_sales
- load_calendar
- load_prices
- merge_all
"""
import os
import pandas as pd
from typing import Optional

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_sales(path: Optional[str] = None) -> pd.DataFrame:
    path = path or os.path.join(DATA_DIR, 'raw', 'sales.csv')
    return pd.read_csv(path, parse_dates=['date'])

def load_calendar(path: Optional[str] = None) -> pd.DataFrame:
    path = path or os.path.join(DATA_DIR, 'raw', 'calendar.csv')
    return pd.read_csv(path, parse_dates=['date'])

def load_prices(path: Optional[str] = None) -> pd.DataFrame:
    path = path or os.path.join(DATA_DIR, 'raw', 'sell_prices.csv')
    return pd.read_csv(path)

def merge_all(sales: pd.DataFrame, calendar: pd.DataFrame, prices: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(calendar, on='date', how='left')
    df = df.merge(prices, on=['store_id', 'item_id', 'wm_yr_wk'], how='left')
    return df