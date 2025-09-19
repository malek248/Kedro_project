# Financial Predictions with Kedro

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)  
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Context & Objectives

This project demonstrates how to structure a professional data science workflow using **Kedro**, from initial exploration in a notebook to final model evaluation. We use an imbalanced banking marketing dataset (UCI Bank Marketing) and an XGBoost classifier. You will learn to:

- Organize data and configuration in a **Data Catalog**.
- Build, test, and run reusable **pipelines** for each stage:  
  1. **Data Processing** (cleaning, train/test split)  
  2. **EDA** (statistical and visual exploration)  
  3. **Feature Engineering** (preprocessing, encoding, scaling)  
  4. **Model Training** (XGBoost, feature selection, final training)  
  5. **Evaluation** (precision, recall, AUC)  
- Ensure **reproducibility** and **traceability** throughout the project.

## Prerequisites

- Python 3.10+  
- Virtual environment  
- Git  
- On macOS: Homebrew for libomp (required by XGBoost)

## Installation

1. **Create & activate** the Conda environment:  

   ```bash
   conda create --name kedro-financial-predictions python=3.10 -y
   conda activate kedro-financial-predictions

2. **Install project dependencies**:

    ```bash
    git clone <your-gitlab-repo>
    cd kedro
    pip install -r requirements.txt
    pip install "kedro-datasets[pandas]"  # for CSVDataset & ParquetDataset

3. **(macOS) Install OpenMP for XGBoost**:

    ```bash
    brew install libomp
    export LDFLAGS="-L/opt/homebrew/opt/libomp/lib"
    export CPPFLAGS="-I/opt/homebrew/opt/libomp/include"

## Project Structure

    .
    ├── conf/
    │   ├── base/
    │   │   ├── catalog.yml
    │   │   └── parameters.yml
    │   └── local/
    ├── data/
    ├── notebooks/
    ├── src/
    │   └── financial_predictions/
    │       ├── pipelines/
    │       └── ...
    ├── tests/
    ├── README.md
    └── requirements.txt

## Data Catalog

| Dataset                       | Type             | Purpose                               |
| ----------------------------- | ---------------- | ------------------------------------- |
| `bank`                        | `CSVDataset`     | Raw dataset                           |
| `preprocessed_bank`           | `ParquetDataset` | Cleaned version                       |
| `grouped_mean`                | `CSVDataset`     | EDA summary statistics                |
| `data_train`, `data_test`     | `ParquetDataset` | Split datasets                        |
| `attrs_map`                   | `ParquetDataset` | Feature metadata                      |
| `X_*`, `y_*`                  | `ParquetDataset` | Transformed features & targets        |
| `xgb_model`                   | `PickleDataset`  | Trained model                         |
| `y_pred_test`, `y_proba_test` | `JSONDataset`    | Prediction results                    |
| `model_metrics`               | `JSONDataset`    | Final evaluation (precision, recall…) |

## Kedro Pipelines

### 1. Data processing

- **Nodes:** `clean_data`, `split_raw_data`
- **Function:** Drop nulls, convert types, train/test split
- **Params:** `split_data.test_size`, `split_data.random_state`

### 2. EDA

- **Nodes:** `get_dtypes`, `plot_count`, `groupby_mean`, `plot_pairplot`, `plot_heatmap`
- **Function:** Explore types, balance, distribution, correlations
- **Params:** `num_cols`, `num_cols_with_y`

### 3. Feature Engineering

- **Nodes:** `split_attributes`, `transform_features`, `transform_target`
- **Function:** Extract features, encode + scale inputs, encode target
- **Output:** `X_train`, `X_test`, `y_train`, `y_test`

### 4. Model Training

- **Nodes:**  `find_best_weight`, `train_initial_model`, `select_features_transformer`, `transform_train`, `train_final_model`, `transform_test`, `predict_model`
- **Function:** Weight tuning → train XGBoost → feature selection → prediction
- **Output:** `xgb_model`, `y_pred_test`, `y_proba_test`

### 5. Evaluation

- **Nodes:** `evaluate_model`
- **Function:** Compute `recall`, `precision`, and `roc_auc` from predictions

## Run Pipelines

Run the full pipeline:

    kedro run

Run a specific one:

    kedro run --pipeline=model_training

Or resume from a specific node:

    kedro run --from-nodes=train_final_model_node

## Testing

Run tests:

    pytest

Linter:

    ruff check

## Publish and Share on AWS

Once your pipelines are working locally, you’ll want to make your work visible and reproducible by others. Below are two common flows: sharing your **Kedro Viz** site, and packaging your project for distribution.

### 1. Set AWS Credentials

In your terminal, export your AWS keys so Kedro‑Viz can push to S3:

    export AWS_ACCESS_KEY_ID="your_access_key_id"
    export AWS_SECRET_ACCESS_KEY="your_secret_access_key"
    
### 2. Publish via the Kedro‑Viz UI

**1. Start the Viz app:**

    kedro viz run

**2. Click the Publish & share icon in the lower‑left corner.**
**3. In the modal:**

- Select hosting platform (e.g. AWS S3)
- Enter your Bucket name and Endpoint URL
- Toggle All dataset previews on or off.

**4. Click Publish and copy the shareable URL when it appears.**

## Contribution Guidelines

- Follow PEP8 (enforced by `ruff`)
- Do not commit raw data or secrets
- Put all secrets in `conf/local/` (not versioned)

## Acknowledgments

This project adapts a Jupyter notebook originally from IBM’s xgboost-financial-predictions repo into a modular, reproducible Kedro pipeline.
