
from fastapi import FastAPI
from pydantic import BaseModel
from src.utils.predict_utils import load_model, predict_transaction

app = FastAPI(title="Fraud Detection API")

# Cargar modelo desde Hugging Face al iniciar
model = load_model()

class Transaction(BaseModel):
    features: list[float]  # Lista con 217 features en orden

@app.post("/predict")
def predict(transaction: Transaction):
    prediction = predict_transaction(model, transaction.features)
    return {"is_fraud": bool(prediction)}