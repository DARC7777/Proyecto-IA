# app/app.py

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import urllib.request
import tempfile

app = FastAPI()

MODEL_URL = "https://huggingface.co/Juannavas38/fraud-model-rf/resolve/main/random_forest_baseline.pkl"

def load_model_from_url(url):
    with tempfile.NamedTemporaryFile(suffix=".pkl", delete=False) as tmp_file:
        urllib.request.urlretrieve(url, tmp_file.name)
        model = joblib.load(tmp_file.name)
    return model

model = load_model_from_url(MODEL_URL)

class Transaction(BaseModel):
    amount: float
    credit_limit: float
    current_age: int
    yearly_income: float

@app.post("/predict")
def predict(transaction: Transaction):
    input_df = pd.DataFrame([{
        "amount": transaction.amount,
        "credit_limit": transaction.credit_limit,
        "current_age": transaction.current_age,
        "yearly_income": transaction.yearly_income
    }])
    prediction = model.predict(input_df)[0]
    return {"prediction": int(prediction)}

