# src/modeling/train_baseline_model_rf.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
import joblib
import os

print("📥 Cargando datos desde data/processed/full_transactions_10m.parquet...")
df = pd.read_parquet("data/processed/full_transactions_10m.parquet")

print("🧹 Preprocesando datos...")
# Eliminar columnas no numéricas o irrelevantes para modelado (por ejemplo: IDs, fechas si no son útiles)
drop_cols = ["id", "date", "card_id", "client_id", "mcc", "mcc_description"]
feature_cols = [col for col in df.columns if col not in drop_cols + ["is_fraud"]]
X = df[feature_cols]
y = df["is_fraud"]

print("📊 Dividiendo datos en entrenamiento y prueba...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

print("🧠 Entrenando modelo Random Forest...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

print("📈 Evaluando el modelo en el conjunto de prueba...")
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

print("\n✅ Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("✅ Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("✅ AUC-ROC:", round(roc_auc_score(y_test, y_proba), 4))

# Guardar el modelo
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/random_forest_baseline.pkl")
print("💾 Modelo guardado en models/random_forest_baseline.pkl")