# src/utils/predict_utils.py

import joblib
import numpy as np
from huggingface_hub import hf_hub_download

def load_model():
    path = hf_hub_download(repo_id="Juannavas38/fraud-model-rf", filename="random_forest_baseline.pkl")
    return joblib.load(path)

def predict_transaction(model, features):
    X = np.array(features).reshape(1, -1)
    return model.predict(X)[0]
