# Sistema de Detección y Prevención de Fraudes Financieros

Este repositorio contiene el proyecto para desarrollar modelos de aprendizaje automático que identifiquen transacciones financieras potencialmente fraudulentas en tiempo real. El objetivo es construir una base robusta para GlobalBank, de modo que pueda reconocer patrones de fraude, disminuir falsos positivos y generar alertas instantáneas ante actividades sospechosas.

---

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)  
2. [Integrantes](#integrantes)  
3. [Objetivos](#objetivos)  
   - [General](#objetivo-general)  
   - [Específicos](#objetivos-específicos)  
4. [Dataset](#dataset)  
5. [Estructura del Repositorio](#estructura-del-repositorio)  
---

## Descripción del Proyecto

A medida que crecen las transacciones digitales, las instituciones financieras enfrentan un riesgo cada vez mayor de fraude. Este proyecto busca:

- Detectar a tiempo transacciones fraudulentas en el flujo diario de datos.  
- Minimizar los falsos positivos para no bloquear operaciones legítimas.  
- Adaptarse dinámicamente a nuevos patrones de fraude mediante reentrenamientos periódicos.  
- Facilitar la investigación de casos sospechosos a analistas de fraude.  

Para ello, usaremos el dataset de Kaggle “Transactions Fraud Datasets” (https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets) como fuente principal de datos, junto con posibles fuentes externas, y construiremos una arquitectura modular en Python que permita escalar a producción (MLOps).

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

1. Investigar y seleccionar algoritmos supervisados y no supervisados adecuados para el problema de detección de fraude.  
2. Realizar Análisis Exploratorio de Datos (EDA) para entender distribuciones, detectar desbalance y descubrir patrones relevantes.  
3. Preprocesar y limpiar los datos (normalización, codificación, manejo de valores faltantes, tratamiento de desbalance de clases).  
4. Entrenar, validar y comparar diferentes modelos (Random Forest, XGBoost, LightGBM, Redes Neuronales, Autoencoders, Isolation Forest, etc.).  
5. Implementar un prototipo de simulación en tiempo real que procese transacciones de manera secuencial y genere alertas.  
6. Evaluar el desempeño usando métricas clave: precisión, recall, F1-score, AUC-ROC y tasa de falsos positivos.  
7. Documentar cada fase del proyecto y entregar un informe técnico completo con resultados, conclusiones y recomendaciones para producción.  

---

## Dataset

- Transactions Fraud Datasets (Kaggle)  
  URL: https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets  
  - Contiene transacciones históricas etiquetadas como legítimas o fraudulentas.  
  - Incluye variables como importe, tipo de transacción, geolocalización (si aplica), información de cuenta, timestamp, entre otras.  

- Posibles Datasets Adicionales (opcional)  
  - Fraud Dataset Benchmark (Amazon Science) — Enlace: https://www.amazon.science/datasets/fraud-dataset-benchmark  

---

## Estructura del Repositorio

