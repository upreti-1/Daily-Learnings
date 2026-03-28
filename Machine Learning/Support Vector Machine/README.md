# Support Vector Machine

This folder contains practical notebooks for Support Vector Machine (SVM) algorithms, including classification and regression use cases.

## Contents

1. `basic SVM (SVC).ipynb`
   - Introduction to SVM classification with `SVC`.
   - Covers model fitting, prediction, and basic evaluation.

2. `SVM Kernal Implementation.ipynb`
   - Demonstrates kernel-based SVM concepts.
   - Helps compare linear and non-linear decision boundaries.

3. `support vector regression implecation.ipynb`
   - Implements Support Vector Regression (SVR).
   - Focuses on prediction for continuous target values.

## Learning Objectives

- Understand margin-based learning and support vectors.
- Learn when to use linear vs kernel SVM.
- Apply SVM for both classification (SVC) and regression (SVR).

## Requirements

Recommended Python packages:

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- jupyter

Install with:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

## How To Run

1. Open this folder in VS Code or Jupyter.
2. Start with `basic SVM (SVC).ipynb` for fundamentals.
3. Continue with kernel implementation and then SVR notebook.
4. Run cells sequentially from top to bottom.

## Notes

- SVM performance can be sensitive to feature scaling; standardization is often important.
- Tune hyperparameters like `C`, `gamma`, and kernel choice for better results.
