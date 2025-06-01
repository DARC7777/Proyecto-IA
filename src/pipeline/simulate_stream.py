# src/pipeline/simulate_stream.py

import pandas as pd
import time
import joblib
from huggingface_hub import hf_hub_download
from sklearn.ensemble import RandomForestClassifier

# 📦 Cargar modelo desde Hugging Face (si no está localmente)
try:
    print("📦 Cargando modelo desde Hugging Face o local...")
    model_path = hf_hub_download(
        repo_id="Juannavas38/fraud-model-rf",
        filename="random_forest_baseline.pkl",
        cache_dir="models"
    )
except:
    model_path = "models/random_forest_baseline.pkl"

model = joblib.load(model_path)

# 🧾 Cargar datos simulados
print("🧾 Cargando datos simulados...")
data = pd.read_parquet("data/processed/full_transactions_10m.parquet")

# ✅ Usar la columna 'is_fraud' como target
data = data[data["is_fraud"].notna()].reset_index(drop=True)
y = data["is_fraud"]
X = data.drop(columns=["is_fraud", "id", "date", "card_id", "client_id", "mcc", "mcc_description"])

# 🔁 Simular flujo de datos
print("📡 Iniciando simulación de flujo de transacciones...\n")
for i in range(10):  # Simula solo 10 transacciones para demostración
    x_i = X.iloc[[i]]
    y_i = y.iloc[i]

    pred = model.predict(x_i)[0]
    proba = model.predict_proba(x_i)[0][1]

    print(f"🧾 Transacción #{i + 1} | Real: {y_i} | Predicción: {pred} | Riesgo: {proba:.2%}")

    # ⏱️ Simula llegada de datos en tiempo real
    time.sleep(1)
