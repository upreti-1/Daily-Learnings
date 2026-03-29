# Gradient Boosting

This folder contains notebooks and datasets for learning and practicing Gradient Boosting for regression tasks.

## Overview

Gradient Boosting is an ensemble learning technique that builds multiple weak learners (usually decision trees) sequentially. Each new model focuses on correcting the errors of previous models, helping improve overall predictive performance.

## Folder Contents

- `gradient boositng implementation.ipynb`:
  Notebook focused on implementing Gradient Boosting workflow step by step.
- `gradient boosting regressor.ipynb`:
  Notebook dedicated to `GradientBoostingRegressor` and model evaluation.
- `Travel.csv`:
  Dataset used for regression practice examples.
- `cardekho_imputated.csv`:
  Cleaned/imputed car-related dataset used for model training and experiments.

## Topics Covered

- Data loading and preprocessing
- Feature and target selection
- Train-test split
- Training Gradient Boosting Regressor models
- Hyperparameter experimentation
- Performance evaluation using regression metrics

## Requirements

Install the common dependencies before running notebooks:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## How To Use

1. Open this folder in VS Code.
2. Start Jupyter and open either notebook.
3. Run all cells in sequence from top to bottom.
4. Compare model behavior across different parameter settings.

## Suggested Experiments

- Change `n_estimators`, `learning_rate`, and `max_depth` to observe bias-variance tradeoff.
- Compare model performance on `Travel.csv` vs `cardekho_imputated.csv`.
- Visualize feature importance to understand which features drive predictions.

## Learning Goal

Build intuition for how boosting improves regression performance over a single tree model, and learn how tuning impacts generalization.