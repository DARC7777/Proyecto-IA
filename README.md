# Sistema de Detección y Prevención de Fraudes Financieros

Este repositorio contiene el proyecto para desarrollar modelos de aprendizaje automático que identifiquen transacciones financieras potencialmente fraudulentas en tiempo real. El objetivo es construir una base robusta para GlobalBank, de modo que pueda reconocer patrones de fraude, disminuir falsos positivos y generar alertas instantáneas ante actividades sospechosas.

---

## Tabla de Contenidos
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Integrantes](#integrantes)
- [Objetivos](#objetivos)
  - [General](#objetivo-general)
  - [Específicos](#objetivos-específicos)
- [Dataset](#dataset)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Avances Recientes](#avances-recientes)
- [Uso del Proyecto](#uso-del-proyecto)

---

## Descripción del Proyecto

A medida que crecen las transacciones digitales, las instituciones financieras enfrentan un riesgo cada vez mayor de fraude. Este proyecto busca:

- Detectar a tiempo transacciones fraudulentas en el flujo diario de datos.
- Minimizar los falsos positivos para no bloquear operaciones legítimas.
- Adaptarse dinámicamente a nuevos patrones de fraude mediante reentrenamientos periódicos.
- Facilitar la investigación de casos sospechosos a analistas de fraude.

El proyecto está desarrollado en Python bajo una arquitectura modular escalable y se encuentra alineado con buenas prácticas de MLOps.

---

## Integrantes
- Juan Sebastián Giraldo Sepúlveda  
- Juan Sebastián Navas Gómez  
- Daniel Alejandro Ruiz Carrillo  
- Carlos Alberto Trujillo  

---

## Objetivos

### Objetivo General
Desarrollar modelos de machine learning capaces de identificar transacciones financieras fraudulentas en tiempo real, empleando datos históricos y técnicas avanzadas de aprendizaje automático para GlobalBank.

### Objetivos Específicos
- Investigar y seleccionar algoritmos supervisados y no supervisados adecuados para el problema.
- Realizar EDA para entender distribuciones, detectar desbalance y descubrir patrones relevantes.
- Preprocesar y limpiar los datos (normalización, codificación, valores faltantes, etc.).
- Entrenar, validar y comparar modelos como Random Forest, XGBoost, LightGBM, Redes Neuronales, Autoencoders, Isolation Forest, etc.
- Implementar una simulación secuencial para evaluación en tiempo real.
- Usar métricas como precisión, recall, F1-score, AUC-ROC y tasa de falsos positivos.
- Documentar cada fase y presentar una propuesta viable para producción.

---

## Dataset

**Fuente principal:**
- [Transactions Fraud Datasets – Kaggle](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets)

**Descripción:**
- Transacciones históricas etiquetadas como legítimas o fraudulentas.
- Variables: monto, hora, tipo, MCC, tarjetas, clientes, geolocalización, etc.

**Dataset procesado para entrenamiento:**
- `data/processed/full_transactions_10m.parquet`

---

## Estructura del Repositorio
Proyecto-IA/
├── data/
│ ├── backup/ # Datos originales sin procesar
│ ├── processed/ # Dataset final en formato .parquet
├── models/ # Modelos se almacenan ahora en Hugging Face
├── notebooks/ # Análisis exploratorio y limpieza de datos
├── src/
│ └── modeling/
│ ├── train_baseline_model.py # Entrenamiento Random Forest
│ └── upload_model_to_hf.py # Subida del modelo a Hugging Face
├── .gitignore
├── README.md


## Avances Recientes

- ✅ Se realizó limpieza de datos, codificación de variables, y reducción del dataset a 10 millones de registros.
- ✅ Se integraron los datasets de transacciones, tarjetas y usuarios.
- ✅ Se añadió la descripción del MCC a las transacciones.
- ✅ Se entrenó un modelo base de Random Forest utilizando todas las variables disponibles.
- ✅ Se migró el modelo a Hugging Face para evitar el error de Git por tamaño de archivo (>100MB).
- ✅ Se eliminó el seguimiento de `models/` con Git LFS y `filter-repo` para limpiar el historial.

---

