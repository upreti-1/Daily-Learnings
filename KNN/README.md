# K-Nearest Neighbours (KNN) Classifier

## Overview
This folder contains a comprehensive implementation and guide for the K-Nearest Neighbours (KNN) classification algorithm. KNN is a simple yet powerful supervised learning algorithm used for classification and regression tasks.

## Contents
- **KNN classifier.ipynb** - A detailed Jupyter notebook covering KNN implementation and hyperparameter tuning

## Key Concepts Covered

### 1. **Dataset Preparation**
   - Creating synthetic classification datasets using `sklearn.datasets.make_classification`
   - Understanding data structure and features

### 2. **Train-Test Split**
   - Splitting data into training (70%) and testing (30%) sets
   - Using `sklearn.model_selection.train_test_split` for reproducible splits

### 3. **KNN Model Implementation**
   - Building a KNN classifier with configurable hyperparameters
   - Training the model on training data
   - Making predictions on test data

### 4. **Model Evaluation**
   - **Accuracy Score**: Overall correctness of predictions
   - **Confusion Matrix**: True positives, true negatives, false positives, false negatives
   - **Classification Report**: Precision, recall, and F1-score metrics

### 5. **Hyperparameter Tuning**
   - Using `GridSearchCV` for exhaustive parameter search
   - Tuning key hyperparameters:
     - **n_neighbors**: Number of nearest neighbours (3, 5, 7, 9, 11, 15)
     - **weights**: Weight function - 'uniform' or 'distance'
     - **metric**: Distance metric - 'euclidean', 'manhattan', or 'minkowski'
   - Finding optimal parameters for best accuracy

## Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Data visualization
- **seaborn**: Statistical graphics
- **scikit-learn**: Machine learning algorithms and utilities

## How to Run
1. Open the notebook: `KNN classifier.ipynb`
2. Execute cells sequentially to understand each step
3. Modify hyperparameters to experiment with different configurations
4. Observe how parameter tuning affects model performance

## Key Takeaways
- KNN is a distance-based algorithm that classifies data based on proximity to nearest neighbours
- The choice of `k` (number of neighbours) significantly impacts model performance
- Distance metrics and weight functions can be tuned for optimal results
- GridSearchCV helps automate the hyperparameter tuning process
- Always evaluate models on a separate test set to assess generalization

## Next Steps
- Experiment with different values of k
- Try various distance metrics
- Apply KNN to real-world datasets
- Compare KNN performance with other classification algorithms
