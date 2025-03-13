# -- coding: utf-8 --
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from aux_functions import generate_custom_run_name

# Set MLflow tracking URI (must match MLflow server in Docker Compose)
mlflow.set_tracking_uri("http://mlflow:5000") #to use inside of container

# Define MLflow experiment
mlflow.set_experiment("Linear_Regression_Experiment")

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3X + noise

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start an MLflow run
with mlflow.start_run():
    custom_run_name = generate_custom_run_name()
    mlflow.set_tag('mlflow.runName', custom_run_name)
    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Compute metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Log parameters & metrics
    mlflow.log_param("fit_intercept", model.fit_intercept)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2_score", r2)

    # Save model to MLflow
    mlflow.sklearn.log_model(model, "linear_regression_model")

    print(f"Model logged in MLflow with MSE: {mse:.4f}, R2 Score: {r2:.4f}")