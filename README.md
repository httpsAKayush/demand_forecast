# Supply Chain Demand Forecasting — Causal AI

End-to-end hierarchical demand forecasting on the Walmart M5 dataset (42,840 time series) with causal inference to isolate promotional lift from seasonal effects.

## Stack
Python · SQL · LightGBM · Prophet · DoWhy · MLflow · FastAPI · Pandas · NumPy

## Architecture
- **Data Layer**: Hierarchical schema (store → dept → item), calendar/price/promo features, SQL analytical views
- **Forecasting**: SARIMA baseline → LightGBM with lag features → Prophet+XGBoost hybrid. Metric: WRMSSE
- **Causal Inference**: DoWhy causal DAG to isolate promotional lift from seasonal demand
- **Business Output**: Overstock/understock risk flags, revenue impact of forecast error, FastAPI inference endpoint

## Dataset
[Walmart M5 Forecasting Competition](https://www.kaggle.com/competitions/m5-forecasting-accuracy) — Kaggle

## Status
🚧 In Progress