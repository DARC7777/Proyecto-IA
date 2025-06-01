# Sistema de Detección y Prevención de Fraudes Financieros

Este repositorio contiene un proyecto de analítica avanzada y machine learning para la detección de transacciones financieras potencialmente fraudulentas en tiempo real. Su desarrollo busca ofrecer una solución escalable para la institución ficticia **GlobalBank**, capaz de reconocer patrones sospechosos, minimizar falsos positivos y facilitar la investigación por parte de analistas de fraude.

---

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Integrantes](#integrantes)
- [Objetivos](#objetivos)
- [Dataset](#dataset)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Estado Actual del Proyecto](#estado-actual-del-proyecto)

---

## Descripción del Proyecto

A medida que las transacciones digitales se multiplican, las instituciones financieras enfrentan un creciente riesgo de fraude. Este proyecto aborda ese reto con los siguientes objetivos:

- Detectar en tiempo real transacciones fraudulentas en grandes volúmenes de datos.
- Minimizar falsos positivos que afecten transacciones legítimas.
- Adaptarse dinámicamente a nuevos esquemas de fraude mediante reentrenamiento periódico.
- Proveer interpretabilidad y herramientas para la investigación de alertas sospechosas.

---

## Integrantes

- Juan Sebastián Giraldo Sepúlveda  
- Juan Sebastián Navas Gómez  
- Daniel Alejandro Ruiz Carrillo  
- Carlos Alberto Trujillo  

---

## Objetivos

### Objetivo General

Desarrollar modelos de machine learning que identifiquen transacciones fraudulentas en tiempo real, integrando múltiples fuentes de datos y aplicando técnicas de análisis predictivo.

### Objetivos Específicos

1. Investigar y seleccionar algoritmos supervisados y no supervisados aplicables al problema de fraude.
2. Realizar un análisis exploratorio para comprender patrones, distribuciones y posibles sesgos.
3. Preprocesar y limpiar los datos, incluyendo codificación, normalización y manejo de desbalance.
4. Entrenar y comparar modelos como Random Forest, LightGBM, XGBoost, redes neuronales y autoencoders.
5. Implementar una simulación de predicción en tiempo real como prueba de concepto (PoC).
6. Evaluar el desempeño con métricas como AUC-ROC, recall, F1-score y tasa de falsos positivos.
7. Documentar todo el proceso técnico y entregar una propuesta escalable a producción (MLOps).

---

## Dataset

### Principal

**Transactions Fraud Datasets (Kaggle)**  
URL: [https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets)  
Contiene millones de transacciones etiquetadas como legítimas o fraudulentas, con información de tarjetas, clientes, comercios y montos.

### Adicionales (Opcional)

- **Amazon Fraud Dataset Benchmark**  
  [https://www.amazon.science/datasets/fraud-dataset-benchmark](https://www.amazon.science/datasets/fraud-dataset-benchmark)

---

## Estructura del Repositorio
├── data/ *Muy pesados se utiliza git ignore se tiene que crear en el repositorio local
│ ├── backup/ *Archivos originales descargados
│ └── processed/ # Dataset final: full_transactions_10m.parquet
├── notebooks/
│ ├── datos.ipynb # Exploración inicial
│ ├── Limpieza_de_datos.ipynb # Preprocesamiento y merge
│ └── validacion_full_transactions_10m.ipynb # Validaciones del dataset de full transactionns
├── src/ # Código fuente (scripts modulares)
├── README.md
└── requirements.txt # Dependencias del proyecto

## 🔄 Estado Actual del Proyecto

| Fase                      | Estado      | Notas                                                       |
|---------------------------|-------------|--------------------------------------------------------------|
| Recolección de Datos      | ✅ Completa | Dataset cargado desde Kaggle                                |
| EDA Inicial               | ✅ Completa | Análisis básico en `datos.ipynb`                            |
| Limpieza y Preprocesamiento | ✅ Completa | Dataset consolidado: `full_transactions_10m.parquet`        |
| Modelado                  | 🔜 En curso | Próximo paso: entrenamiento con LightGBM, RandomForest, etc.|
| Simulación en tiempo real | 🔜 Pendiente | Se hará PoC con flujo secuencial de transacciones           |
| Documentación final       | 🔄 En progreso | Se actualizará junto al avance del modelo                   |

---
