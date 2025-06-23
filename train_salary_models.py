import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# Load data
df = pd.read_csv("data/simulated_student_ISA_dataset.csv")

# Target variables
target_vars = ['predicted_salary', 'salary_growth', 'discount_rate']
features = [col for col in df.columns if col not in target_vars + ['student_id']]

# Identify categorical columns
categorical_cols = df[features].select_dtypes(include="object").columns.tolist()
numeric_cols = df[features].select_dtypes(include=np.number).columns.tolist()

# Define preprocessor
preprocessor = ColumnTransformer(transformers=[
    ("cat", OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_cols)
], remainder="passthrough")

# Create directory for models
os.makedirs("models", exist_ok=True)

for target in target_vars:
    print(f"\n🔍 Training models for target: {target}")
    print("-" * 40)
    
    X = df[features]
    y = df[target]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # OLS pipeline
    ols_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ])
    ols_pipeline.fit(X_train, y_train)

    # Lasso pipeline
    lasso_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", Lasso(alpha=0.1))
    ])
    lasso_pipeline.fit(X_train, y_train)

    # Evaluate
    ols_test_mse = mean_squared_error(y_test, ols_pipeline.predict(X_test))
    lasso_test_mse = mean_squared_error(y_test, lasso_pipeline.predict(X_test))

    ols_cv = cross_val_score(ols_pipeline, X, y, cv=5, scoring="neg_mean_squared_error")
    lasso_cv = cross_val_score(lasso_pipeline, X, y, cv=5, scoring="neg_mean_squared_error")

    print(f"OLS Test MSE: {abs(ols_test_mse):.4f}")
    print(f"OLS CV MSE: {abs(ols_cv.mean()):.4f}")
    print(f"Lasso Test MSE: {abs(lasso_test_mse):.4f}")
    print(f"Lasso CV MSE: {abs(lasso_cv.mean()):.4f}")

    # ✅ Save model
    joblib.dump(lasso_pipeline, f"models/lasso_model_{target}.pkl")
    print(f"✅ Saved: models/lasso_model_{target}.pkl")

