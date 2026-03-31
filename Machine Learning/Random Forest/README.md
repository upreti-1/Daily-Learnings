# Random Forest Implementation

This folder contains an end-to-end classification workflow using Random Forest on a travel package purchase dataset.

## Problem Statement

Trips and Travel company wants to improve marketing efficiency for package promotions. Instead of random outreach, the notebook uses customer data to predict whether a customer will purchase a travel package.

## Dataset

- File: `Travel.csv`
- Source: https://www.kaggle.com/datasets/susant4learning/holiday-package-purchase-prediction
- Size used in notebook: 4888 rows, 20 columns
- Target column: `ProdTaken`

## Files in This Folder

- `Random Forest Implementation.ipynb`: Complete workflow from data cleaning to model tuning.
- `Travel.csv`: Input dataset for training and evaluation.

## Workflow Covered

1. Data loading and quick inspection
2. Data cleaning
3. Missing value imputation
4. Feature engineering (`TotalVisiting`)
5. Train/test split
6. Preprocessing with `ColumnTransformer`
7. Baseline model comparison:
   - Logistic Regression
   - Decision Tree
   - Random Forest
8. Hyperparameter tuning with `RandomizedSearchCV`
9. Final model evaluation (Accuracy, Precision, Recall, F1, ROC-AUC)

## Requirements

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn jupyter
```

## How to Run

1. Open this folder in VS Code.
2. Open `Random Forest Implementation.ipynb`.
3. Run cells in order from top to bottom.
4. Keep `Travel.csv` in the same directory as the notebook.

## Notes

- The notebook compares multiple classifiers before focusing on a tuned Random Forest model.
- The final section indicates performance improvement after hyperparameter tuning.