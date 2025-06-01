# src/pipeline/simulate_stream.py

import pandas as pd
import joblib
import time

print("📦 Cargando modelo desde Hugging Face o local...")
model = joblib.load("models/random_forest_baseline.pkl")

print("🧾 Cargando datos simulados...")
data = pd.read_parquet("data/processed/full_transactions_10m.parquet")

# Filtrar transacciones con etiqueta
data = data[data["target"].notna()].reset_index(drop=True)

# Separar variables predictoras
X = data.drop(columns=["target"])
y = data["target"]

print("▶️ Iniciando simulación de flujo en tiempo real...\n")

for i in range(0, len(X), 100):  # Lotes de 100 transacciones
    batch = X.iloc[i:i+100]
    preds = model.predict_proba(batch)[:, 1]

    for j, prob in enumerate(preds):
        if prob > 0.9:
            print(f"⚠️  ALERTA: Transacción {i+j} sospechosa con probabilidad {prob:.2f}")

    time.sleep(0.5)  # Espera 0.5 segundos entre lotes (simulación)
