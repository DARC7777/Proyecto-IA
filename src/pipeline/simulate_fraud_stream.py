import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st
import requests
import time
import os

# --- Cargar y preparar el dataset ---
ruta = 'data/processed/full_transactions_10m.parquet'
assert os.path.exists(ruta), f"⚠️ No se encontró el archivo: {ruta}"

df = pd.read_parquet(ruta)

# Dividir entre entrenamiento y prueba
df_train, df_test = train_test_split(df, test_size=0.2, stratify=df['is_fraud'], random_state=42)
df_fraud_test = df_test[df_test['is_fraud'] == 1].reset_index(drop=True)

# --- Configuración de la app ---
st.set_page_config(page_title="Simulador de Fraudes", layout="wide")
st.title("🛡️ Simulación de Transacciones Fraudulentas")
st.caption("Visualizando características del cliente y resultado de predicción del modelo")

# --- Iterar por cada transacción fraudulenta ---
for i, row in df_fraud_test.iterrows():
    st.markdown(f"### 💳 Transacción Fraudulenta #{i+1} | {row['mcc_description']}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Monto", f"${row['amount']:.2f}")
        st.text(f"🕒 Hora: {row['trans_hour']}:00")
        st.text(f"📅 Día: {row['trans_day']} - Mes: {row['trans_month']}")

    with col2:
        st.text(f"🧓 Edad cliente: {int(row['current_age'])} años")
        st.text(f"🧠 Ingreso anual: ${int(row['yearly_income'])}")
        st.text(f"💳 Límite crédito: ${int(row['credit_limit'])}")

    with col3:
        genero = "👨 Hombre" if row["gender"] == 1 else "👩 Mujer"
        chip = "✅ Tiene chip" if row["has_chip"] == 1 else "❌ Sin chip"
        st.text(f"🧬 Género: {genero}")
        st.text(f"💾 Tarjeta: {chip}")
        st.text(f"🏦 MCC: {row['mcc']}")

    # Preparar features para la API Hugging Face
    features = row.drop([
        'is_fraud', 'id', 'date', 'card_id', 'client_id', 'mcc', 'mcc_description'
    ]).tolist()
    payload = {"features": [float(x) for x in features]}

    try:
        response = requests.post("https://juannavas38-fraud-api.hf.space/predict", json=payload)
        pred = response.json().get('prediction', 0)

        if pred == 1:
            st.error("🚨 FRAUDE DETECTADO por el modelo")
        else:
            st.success("⚠️ NO detectado por el modelo")

    except Exception as e:
        st.warning(f"❌ No se pudo conectar a la API: {e}")

    st.markdown("---")
    time.sleep(1)
