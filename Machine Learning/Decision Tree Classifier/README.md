# Decision Tree Classifier

## Overview
This folder contains a comprehensive implementation and guide for Decision Tree Classifier, a powerful supervised learning algorithm used for classification tasks. Decision Trees are intuitive, interpretable models that make predictions by recursively splitting data based on feature values.

## Contents
- **decision tree classifier.ipynb** - A detailed Jupyter notebook covering Decision Tree implementation, visualization, and hyperparameter tuning

## Key Concepts Covered

### 1. **Dataset Preparation**
   - Loading the Iris dataset using `sklearn.datasets.load_iris`
   - Understanding dataset structure and features
   - Working with independent (X) and dependent (y) variables

### 2. **Train-Test Split**
   - Splitting data into training (70%) and testing (30%) sets
   - Using `sklearn.model_selection.train_test_split` with reproducible random state

### 3. **Decision Tree Model Implementation**
   - Building a Decision Tree Classifier with scikit-learn
   - Training the model on training data
   - Making predictions on test data

### 4. **Tree Visualization**
   - Visualizing the decision tree structure using `tree.plot_tree()`
   - Understanding how the tree makes decisions at each node
   - Interpreting splits based on feature values and information gain

### 5. **Model Evaluation**
   - **Confusion Matrix**: Understanding true positives, true negatives, false positives, and false negatives
   - **Classification Report**: Detailed metrics including precision, recall, and F1-score for each class

### 6. **Hyperparameter Tuning (Prepruning)**
   - Using `GridSearchCV` for exhaustive parameter search with 5-fold cross-validation
   - Key hyperparameters tuned:
     - **criterion**: Split quality measure - 'gini', 'entropy', or 'log_loss'
     - **splitter**: Strategy for splitting - 'best' or 'random'
     - **max_depth**: Maximum depth of the tree (1, 2, 3, 4, 5)
     - **max_features**: Number of features to consider - 'auto', 'sqrt', or 'log2'
   - Identifying best parameters and best estimator

## Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Data visualization
- **scikit-learn**: Machine learning algorithms and utilities

## How to Run
1. Open the notebook: `decision tree classifier.ipynb`
2. Execute cells sequentially to understand each step
3. Observe the tree visualization to understand how decisions are made
4. Compare baseline model performance with hyperparameter-tuned model
5. Experiment with different parameter values

## Key Takeaways
- Decision Trees split features based on information gain (Gini impurity or entropy)
- Trees are highly interpretable compared to other machine learning algorithms
- Tree depth is crucial - deeper trees can overfit, shallower trees may underfit
- Prepruning (limiting tree growth) helps prevent overfitting
- GridSearchCV automates the process of finding optimal hyperparameters
- The Iris dataset is perfect for learning classification with clear feature relationships

## Advantages of Decision Trees
- ✓ Easy to understand and interpret
- ✓ Requires little data preprocessing
- ✓ Works with both numerical and categorical data
- ✓ Fast predictions
- ✓ Provides feature importance

## Disadvantages of Decision Trees
- ✗ Prone to overfitting (requires careful pruning)
- ✗ Can be unstable (small data changes can affect tree structure)
- ✗ Biased towards features with more levels
- ✗ May create biased trees with imbalanced datasets

## Next Steps
- Experiment with different splitting criteria (gini vs entropy vs log_loss)
- Try post-pruning techniques for model simplification
- Apply Decision Trees to other datasets
- Explore ensemble methods like Random Forest and Gradient Boosting
- Compare Decision Tree performance with other classifiers
