# Sistema de Detección y Prevención de Fraudes Financieros

Este repositorio contiene el desarrollo de una **prueba de concepto** para detectar transacciones financieras fraudulentas en tiempo real. El objetivo es ofrecer una solución funcional y escalable para **GlobalBank**, utilizando técnicas de aprendizaje automático, despliegue con Docker y modelos alojados en Hugging Face Hub.

---

## 📂 Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Integrantes](#integrantes)
- [Objetivos](#objetivos)
- [Dataset](#dataset)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Despliegue en Hugging Face Spaces](#despliegue-en-hugging-face-spaces)

---

## 🧠 Descripción del Proyecto

El sistema detecta transacciones sospechosas en tiempo real, minimiza falsos positivos y permite una fácil investigación por parte de analistas. Para ello:

- Se entrena un modelo de clasificación supervisado.
- Se simula un flujo de transacciones que se analizan secuencialmente.
- Se despliega una API para predecir fraudes usando el modelo.

---

## 🧱 Arquitectura del Sistema

- **Entrenamiento Offline:** El modelo Random Forest se entrena localmente y se sube a Hugging Face Hub.
- **Simulación:** Se genera un flujo de datos simulados que imita operaciones reales.
- **Predicción Online:** Una API construida con FastAPI consulta el modelo en Hugging Face Hub.
- **Despliegue:** Se utiliza Docker para crear un contenedor listo para Hugging Face Spaces.

---

## 👥 Integrantes

- Juan Sebastián Giraldo Sepúlveda  
- Juan Sebastián Navas Gómez  
- Daniel Alejandro Ruiz Carrillo  
- Carlos Alberto Trujillo  

---

## 🎯 Objetivos

### Objetivo General
Construir una plataforma básica de detección de fraudes que sea escalable, modular y accesible desde cualquier navegador.

### Objetivos Específicos

- Entrenar un modelo de clasificación (Random Forest).
- Simular un flujo continuo de transacciones.
- Evaluar el modelo con métricas como AUC-ROC, precisión y recall.
- Subir el modelo a Hugging Face Hub.
- Desplegar una demo en línea usando Docker en Hugging Face Spaces.

---

## 📊 Dataset

- **Fuente principal:** [Transactions Fraud Datasets – Kaggle](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets)
- Se procesaron 10 millones de transacciones para entrenamiento y prueba (`full_transactions_10m.parquet`).
- El modelo entrenado se encuentra disponible en Hugging Face: [`fraud-model-rf`](https://huggingface.co/Juannavas38/fraud-model-rf)

---

## 🗂️ Estructura del Repositorio

```plaintext
Proyecto-IA/
├── app/
│   └── app.py                 # API FastAPI para detección de fraude
├── data/                      # (NO se sube al repositorio)
├── models/                    # (vacía, modelo se carga desde Hugging Face)
├── notebooks/                 # Jupyter notebooks de análisis y simulación
├── src/
│   ├── modeling/
│   │   └── train_baseline_model.py
│   ├── pipeline/
│   │   └── simulate_stream.py
│   └── utils/
│       └── predict_utils.py   # Funciones auxiliares para predicción
├── Dockerfile                 # Imagen para Hugging Face Spaces
├── requirements.txt           # Dependencias
├── .gitignore
└── README.md