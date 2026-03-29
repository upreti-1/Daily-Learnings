# XGBoost

This folder contains notebook implementations of XGBoost for both classification and regression tasks.

## Overview

XGBoost (Extreme Gradient Boosting) is a high-performance ensemble learning algorithm based on gradient-boosted decision trees. It is widely used for structured/tabular datasets because of strong accuracy, regularization options, and efficient training.

## Folder Contents

- `Xgboost classification implementation.ipynb`:
  End-to-end workflow for classification using XGBoost, including model training and ROC-AUC evaluation.
- `Xgboost regressor implementation .ipynb`:
  Regression workflow using XGBoost Regressor with prediction and error analysis.
- `Travel.csv`:
  Dataset used for model training and experimentation.
- `auc.png`:
  Saved ROC curve plot from the classification workflow.

## Topics Covered

- Data loading and preprocessing
- Feature-target split
- Train-test split
- XGBoost model training (classifier and regressor)
- Evaluation metrics:
  - Classification: ROC curve, AUC, confusion matrix (if included in notebook)
  - Regression: R2 score, MAE, MSE, RMSE (based on notebook implementation)

## Requirements

Install dependencies before running the notebooks:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost jupyter
```

## How To Use

1. Open this folder in VS Code.
2. Open either notebook in Jupyter.
3. Run cells in sequence from top to bottom.
4. Compare performance across parameter settings.

## Suggested Experiments

- Tune `n_estimators`, `max_depth`, `learning_rate`, and `subsample`.
- Compare underfitting vs overfitting behavior.
- Try cross-validation to make model selection more reliable.
- Compare XGBoost performance with other models in your `Machine Learning` folder.

## Learning Goal

Understand how boosting improves model performance for both classification and regression, and how hyperparameter tuning affects generalization.