import streamlit as st
import pandas as pd
import requests
import time

# Configuración de la página
st.set_page_config(page_title="Simulación en Tiempo Real", layout="wide")

# Ruta local del dataset
DATA_PATH = "data/processed/full_transactions_10m.parquet"
API_URL = "https://juannavas38-fraud-api.hf.space/predict"

# Título
st.title("🔍 Simulación de Detección de Fraude en Tiempo Real")

@st.cache_data
def cargar_datos():
    df = pd.read_parquet(DATA_PATH)
    df = df[df["is_fraud"].notna()].reset_index(drop=True)
    X = df.drop(columns=["is_fraud", "id", "date", "card_id", "client_id", "mcc", "mcc_description"])
    y = df["is_fraud"]
    return X, y

# Cargar datos
X, y = cargar_datos()
st.success(f"✅ Dataset cargado con {len(X)} transacciones y {X.shape[1]} columnas.")

# Crear un botón para iniciar simulación
if st.button("🚀 Iniciar Simulación"):
    resultados = []
    placeholder = st.empty()

    for i in range(100):
        x_i = X.iloc[i].tolist()
        y_i = y.iloc[i]

        payload = {"features": [float(x) for x in x_i]}
        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                result = response.json()
                pred = result["is_fraud"]
                resultados.append({
                    "Transacción": i + 1,
                    "Real": int(y_i),
                    "Predicción": int(pred),
                })
            else:
                resultados.append({
                    "Transacción": i + 1,
                    "Real": int(y_i),
                    "Predicción": "Error",
                })
        except Exception as e:
            resultados.append({
                "Transacción": i + 1,
                "Real": int(y_i),
                "Predicción": f"Error: {e}",
            })

        # Mostrar resultados parciales
        df_resultados = pd.DataFrame(resultados)
        placeholder.dataframe(df_resultados)
        time.sleep(1)
