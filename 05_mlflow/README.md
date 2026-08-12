# MLflow

This section covers **MLflow for MLOps**, focusing on experiment tracking and model registry.

## 🚀 What is MLflow?

MLflow is an open-source platform used to manage the **machine learning lifecycle**.

It helps track experiments, store models, compare runs, and manage model versions.

## 🔬 Experiment Tracking

Track:

* Parameters
* Metrics
* Model artifacts
* Training runs
* Models

Example:

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 10)
    mlflow.log_metric("accuracy", 0.95)
```

Start the MLflow UI:

```bash
mlflow ui
```

Open `http://127.0.0.1:5000`.

## 📦 Model Registry

Model Registry is used to **store and manage model versions**.

```text
Training
   ↓
MLflow Tracking
   ↓
Model Evaluation
   ↓
Model Registry
   ↓
Model Version
   ↓
Deployment
```

Example:

```python
mlflow.sklearn.log_model(
    model,
    "model",
    registered_model_name="MyModel"
)
```

## 🛠️ MLOps Role

```text
Git/GitHub → Code Versioning
DVC        → Data Versioning
MLflow     → Experiment + Model Tracking
Docker     → Containerization
CI/CD      → Deployment
Monitoring → Production Monitoring
```

**Key idea:** MLflow makes ML experiments and models **trackable, reproducible, and version-controlled**.
