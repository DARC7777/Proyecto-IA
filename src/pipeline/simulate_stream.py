# src/pipeline/simulate_stream.py

import pandas as pd
import requests
import time
import os

# Ruta al archivo con datos simulados
DATA_PATH = "data/processed/full_transactions_10m.parquet"

# URL de la API desplegada en Hugging Face Spaces
API_URL = "https://juannavas38-fraud-api.hf.space/predict"

# Ruta para guardar resultados
OUTPUT_PATH = "results/predicciones_simulacion.csv"
os.makedirs("results", exist_ok=True)  # Crea carpeta si no existe

def main():
    print("🧾 Cargando dataset de prueba...")
    data = pd.read_parquet(DATA_PATH)
    data = data[data["is_fraud"].notna()].reset_index(drop=True)

    # Eliminar columnas no usadas
    X = data.drop(columns=["is_fraud", "id", "date", "card_id", "client_id", "mcc", "mcc_description"])
    y = data["is_fraud"]

    print(f"📊 Usando {X.shape[1]} columnas para predicción")

    results = []

    for i in range(100):  # Simula 10 transacciones
        x_i = X.iloc[i].tolist()
        y_i = y.iloc[i]

        payload = {
            "features": [float(x) for x in x_i]
        }

        print(f"▶️ Enviando transacción #{i+1} ({len(x_i)} features)...")

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                result = response.json()
                pred = result['is_fraud']
                print(f"✅ Real: {y_i} | Predicción: {pred}")

                results.append({
                    "transaccion_id": i + 1,
                    "real": int(y_i),
                    "prediccion": int(pred),
                    "riesgo": None  # Para futuras versiones
                })
            else:
                print(f"⚠️  Error {response.status_code} - {response.text}")

        except Exception as e:
            print(f"❌ Error de conexión: {e}")

        time.sleep(1)

    # Guardar resultados en CSV
    df_resultados = pd.DataFrame(results)
    df_resultados.to_csv(OUTPUT_PATH, index=False)
    print(f"\n📁 Resultados guardados en: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()

