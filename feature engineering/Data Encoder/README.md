# Data Analysis with Python: NumPy & Pandas 📊

This section contains my learning progress and hands-on exercises for data manipulation and analysis using the industry-standard libraries NumPy and Pandas.

## 📁 Files in this Section

* `numpy.ipynb`: Introduction to NumPy arrays, vectorized operations, slicing, and statistical normalization.
* `pandas.ipynb`: Deep dive into Pandas Series and DataFrames, including data creation and basic manipulation.
* `datamanipulation.ipynb`: Practical exercises on handling missing values and data cleaning techniques.

## 🛠️ Key Concepts Covered

### NumPy
- **Array Creation:** Creating 1D and 2D arrays using `np.array`, `np.arange`, `np.ones`, and `np.zeros`.
- **Vectorized Operations:** Element-wise addition, subtraction, and universal functions like `np.sqrt` and `np.log`.
- **Indexing & Slicing:** Extracting specific sub-sections of matrices.
- **Normalization:** Manually calculating Mean and Standard Deviation to scale data.

### Pandas
- **Data Structures:** Difference between 1-dimensional **Series** and 2-dimensional **DataFrames**.
- **Data Access:** Using `.at[]`, `.iat[]`, and `.head()` to inspect and retrieve specific data points.
- **Manipulation:** Adding/dropping columns, updating values based on logic, and using `.describe()` for statistical summaries.

## 🚀 How to Use These Notebooks

1. Ensure your virtual environment is active:
   ```bash
   source venv/bin/activate
   ```

2. Install the necessary libraries:
   ```bash
   pip install numpy pandas ipykernel
   ```

3. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```