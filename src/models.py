# ...existing code...
"""
Model training helpers: LightGBM trainer and simple predict wrapper.
"""
import joblib
import lightgbm as lgb
from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split

def train_lgb(df: pd.DataFrame, target: str, features: list, params: dict = None, model_path: str = 'model.pkl') -> Tuple[object, dict]:
    params = params or {
        'objective': 'regression',
        'metric': 'rmse',
        'verbosity': -1,
        'seed': 42
    }
    X = df[features]
    y = df[target]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    train_data = lgb.Dataset(X_train, label=y_train)
    val_data = lgb.Dataset(X_val, label=y_val)
    model = lgb.train(params, train_data, valid_sets=[val_data], early_stopping_rounds=50, num_boost_round=1000)
    joblib.dump(model, model_path)
    return model, {'model_path': model_path}

def predict_lgb(model, df: pd.DataFrame, features: list) -> pd.Series:
    return model.predict(df[features])