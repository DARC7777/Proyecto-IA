import gradio as gr
import pandas as pd
import joblib
import tempfile
import urllib.request

# Cargar el modelo desde Hugging Face
MODEL_URL = "https://huggingface.co/Juannavas38/fraud-model-rf/resolve/main/random_forest_baseline.pkl"

def load_model_from_url(url):
    """Descarga el modelo desde Hugging Face y lo carga en memoria."""
    with tempfile.NamedTemporaryFile(suffix=".pkl") as tmp_file:
        urllib.request.urlretrieve(url, tmp_file.name)
        model = joblib.load(tmp_file.name)
    return model

model = load_model_from_url(MODEL_URL)

# Función de predicción
def predecir_fraude(amount, credit_limit, current_age, yearly_income):
    input_data = pd.DataFrame([{
        "amount": amount,
        "credit_limit": credit_limit,
        "current_age": current_age,
        "yearly_income": yearly_income
    }])
    pred = model.predict(input_data)[0]
    return "🔴 Fraude detectado" if pred == 1 else "🟢 Transacción legítima"

# Interfaz de Gradio
demo = gr.Interface(
    fn=predecir_fraude,
    inputs=[
        gr.Number(label="Monto de la transacción"),
        gr.Number(label="Límite de crédito"),
        gr.Number(label="Edad actual"),
        gr.Number(label="Ingreso anual"),
    ],
    outputs="text",
    title="🛡️ Detección de Fraude Financiero - GlobalBank",
    description="Simula una transacción y predice si es fraudulenta usando un modelo de Random Forest entrenado."
)

if __name__ == "__main__":
    demo.launch()
