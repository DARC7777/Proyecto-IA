from huggingface_hub import upload_file

repo_id = "Juannavas38/fraud-model-rf"
local_path = "models/random_forest_baseline.pkl"
hf_path = "random_forest_baseline.pkl"

print(f"📤 Subiendo modelo {local_path} a {repo_id}...")

upload_file(
    path_or_fileobj=local_path,
    path_in_repo=hf_path,
    repo_id=repo_id,
    repo_type="model"
)

print("✅ Subida completada correctamente.")
