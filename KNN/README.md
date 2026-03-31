# K Nearest Neighbors Classifier

This folder contains a notebook that builds and tunes a KNN classifier for a binary classification task.

## Files

- `KNN classifier.ipynb`: End-to-end KNN workflow from data generation to model evaluation.

## What the Notebook Covers

1. Importing core libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`)
2. Creating a synthetic dataset using `make_classification`
3. Splitting data into train and test sets
4. Training a baseline `KNeighborsClassifier`
5. Evaluating with:
   - Accuracy score
   - Confusion matrix
   - Classification report
6. Hyperparameter tuning with `GridSearchCV` for:
   - `n_neighbors`
   - `weights`
   - `metric`
7. Re-evaluating predictions using the tuned model

## Requirements

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## How to Run

1. Open this folder in VS Code.
2. Open `KNN classifier.ipynb`.
3. Run cells from top to bottom.
4. Check printed metrics before and after GridSearchCV to compare performance.

## Learning Outcome

You will understand how KNN works, why choosing the right `k` matters, and how grid search improves model selection through systematic tuning.
