# ...existing code...
"""
Feature engineering helpers: lags, rolling means, category encodings.
"""
import pandas as pd
import numpy as np
from typing import List

def make_lag_features(df: pd.DataFrame, group_cols: List[str], target_col: str, lags: List[int]) -> pd.DataFrame:
    df = df.sort_values(group_cols + ['date'])
    for lag in lags:
        df[f'{target_col}_lag_{lag}'] = df.groupby(group_cols)[target_col].shift(lag)
    return df

def rolling_features(df: pd.DataFrame, group_cols: List[str], target_col: str, windows: List[int]) -> pd.DataFrame:
    df = df.sort_values(group_cols + ['date'])
    for w in windows:
        df[f'{target_col}_rollmean_{w}'] = df.groupby(group_cols)[target_col].shift(1).rolling(window=w, min_periods=1).mean().reset_index(0, drop=True)
    return df

def encode_categorical(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    for c in cols:
        df[c] = df[c].astype('category').cat.codes
    return df