import pandas as pd
import joblib
import numpy as np

# === 1. Load training data to extract expected features ===
train_df = pd.read_csv("data/simulated_student_ISA_dataset.csv")

target_vars = ["predicted_salary", "salary_growth", "discount_rate"]
exclude_cols = ["student_id"] + target_vars
features = [col for col in train_df.columns if col not in exclude_cols]

# === 2. Load trained models (already include preprocessing pipeline) ===
models = {
    target: joblib.load(f"models/lasso_model_{target}.pkl")
    for target in target_vars
}

# === 3. Function to apply model on a new dataset ===
def apply_model_to_file(file_path):
    df = pd.read_csv(file_path)

    # Sanitize and ensure all expected features exist
    df.columns = df.columns.str.strip()
    for col in features:
        if col not in df.columns:
            print(f"⚠️ Adding missing column '{col}' in {file_path} with default value")
            df[col] = 0 if train_df[col].dtype in [np.int64, np.float64] else "unknown"

    # Only select model-relevant features
    input_data = df[features].copy()

    # Predict with each model
    for target in target_vars:
        df[target] = models[target].predict(input_data)

    # Save updated CSV
    df.to_csv(file_path, index=False)
    print(f"✅ Predictions added and saved to {file_path}")

# === 4. Apply to all 3 files ===
apply_model_to_file("data/students.csv")
apply_model_to_file("data/students_trading.csv")
apply_model_to_file("data/portfolio_sample.csv")



