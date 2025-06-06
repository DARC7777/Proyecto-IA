from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import urllib.request
import os

# URL del modelo en Hugging Face
MODEL_URL = "https://huggingface.co/Juannavas38/fraud-model-rf/resolve/main/random_forest_baseline.pkl"

def load_model_from_url(url):
    os.makedirs("models", exist_ok=True)
    local_path = "models/temp_model.pkl"
    
    if not os.path.exists(local_path):
        urllib.request.urlretrieve(url, local_path)
    
    model = joblib.load(local_path)
    return model

model = load_model_from_url(MODEL_URL)

# Crear la API
app = FastAPI(title="GlobalBank Fraud Detection API")

# Definir el esquema de entrada
class Transaction(BaseModel):
    amount: float
    credit_limit: float
    current_age: float
    yearly_income: float

# Endpoint de predicción
@app.post("/predict")
def predict(tx: Transaction):
    input_data = pd.DataFrame([tx.dict()])
    prediction = model.predict(input_data)[0]
    return {"prediction": int(prediction)}
