# ...existing code...
"""
FastAPI inference endpoint (minimal).
"""
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import List

app = FastAPI(title="M5 Demand Forecast API")

MODEL_PATH = "model.pkl"

class PredictRequest(BaseModel):
    records: List[dict]

@app.on_event("startup")
def load_model():
    try:
        app.state.model = joblib.load(MODEL_PATH)
    except Exception:
        app.state.model = None

@app.post("/predict")
def predict(req: PredictRequest):
    model = app.state.model
    if model is None:
        return {"error": "model not loaded"}
    df = pd.DataFrame(req.records)
    preds = model.predict(df)
    return {"predictions": preds.tolist()}