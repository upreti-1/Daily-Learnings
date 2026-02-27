# Data Preprocessing & Feature Engineering Essentials 📊
### This repository contains a collection of Jupyter Notebooks documenting my learning path through essential data preprocessing, statistical analysis, and feature engineering techniques. These steps are fundamental for preparing raw data into a format suitable for Machine Learning models.


# 📁 Files in this Repository
***5 number summary.ipynb***: Implementation of descriptive statistics and outlier detection using the Interquartile Range (IQR) method and Seaborn visualizations.

***handling missing values.ipynb***: Exploration of missing data mechanisms (MCAR, MAR, MNAR) and various imputation strategies.

***imbalance dataset.ipynb***: Techniques for balancing datasets, including manual UpSampling, DownSampling, and advanced synthetic methods.

***SMOTE.ipynb***: Deep dive into Synthetic Minority Over-sampling Technique (SMOTE) to address class imbalance through interpolation.

***ordinal and Label encoding.ipynb***: Converting categorical text into numerical data using Label and Ordinal encoding techniques.

***target_guided_ordinal_encoding.ipynb***: Advanced feature engineering where categories are ranked based on their relationship with the target variable.



# 🛠️ Key Concepts Covered
## Statistical Analysis
***5-Number Summary***: Calculating Minimum, First Quartile (Q1), Median, Third Quartile (Q3), and Maximum.

***Outlier Detection***: Using the IQR (Interquartile Range) to define "fences" (Lower and Higher) to identify extreme values in a dataset.

***Visual Exploration***: Creating Box Plots using seaborn to visualize data distribution and outliers.

## Data Cleaning
***Missing Data Mechanisms***: Understanding MCAR (Completely at Random), MAR (at Random), and MNAR (Not at Random).

***Imputation***: Handling null values using Mean, Median (for data with outliers), and Mode (for categorical data) imputation.


## eature Engineering & Encoding
***Label Encoding***: Assigning unique integers to categories (typically for target variables).

***Ordinal Encoding***: Mapping categories to ordered integers when an intrinsic rank exists (e.g., Small, Medium, Large).

***Target Guided Encoding***: Encoding categorical features based on the mean/median of the target variable to capture monotonic relationships.


## Handling Imbalanced Data
***Resampling***: Manual implementation of UpSampling (increasing minority class) and DownSampling (decreasing majority class).

***SMOTE***: Using imblearn to generate synthetic examples for the minority class rather than simply duplicating rows.


## 🚀 Getting Started
Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git


Install necessary libraries:

Bash

pip install numpy pandas seaborn matplotlib scikit-learn imblearn
Run the Notebooks:
Open the files in Jupyter Lab, Jupyter Notebook, or VS Code to explore the code and visualizations.

# Author: **Prashant Upreti**