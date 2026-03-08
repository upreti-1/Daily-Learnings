## EDA folder — Overview

This folder contains exploratory data analysis (EDA) notebooks and related datasets used for quick analysis and feature engineering experiments.

## Contents

- `2.0-EDA+And+FE+Flight+Price.ipynb` — End-to-end EDA and feature engineering for a flight price dataset.
- `flight price prediction.ipynb` — Notebook focused on model building / prediction for flight price forecasting.
- `Google playstore dataset.ipynb` — EDA and analysis for the Google Play Store apps dataset.
- `redwinedata.ipynb` — Analysis and visualization of the red wine quality dataset.
- `winequality-red.csv` — Raw red wine quality dataset (CSV).
- `data/google_cleaned.csv` — Cleaned Google Play Store dataset used by the Google Play Store notebook.

## How to open

1. Install required Python packages (example):

```bash
python -m pip install -r requirements.txt
# or
python -m pip install pandas numpy matplotlib seaborn scikit-learn jupyterlab
```

2. Launch Jupyter Lab / Notebook from the `EDA` directory to open the notebooks:

```bash
jupyter lab
# or
jupyter notebook
```

## Recommended packages

- pandas, numpy — data handling
- matplotlib, seaborn, plotly — visualization
- scikit-learn — feature engineering and modeling
- jupyterlab or notebook — interactive exploration

If you already have a central `requirements.txt` for the project, prefer installing that; otherwise the list above covers the commonly used libraries in these notebooks.

## Notes

- The notebooks are exploratory; they may read datasets from the relative `data/` folder or the CSV files included in this directory. If a notebook fails to find a file, check the path in the first cells and update it to the correct relative path.
- For reproducibility, consider creating a virtual environment before installing packages:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## License / Attribution

These notebooks are for learning and experimentation. If any dataset requires attribution, check the original dataset source and cite accordingly.

---

If you'd like, I can also:
- add a minimal `requirements.txt` inside this folder,
- add small README badges, or
- run a quick check to ensure each notebook runs its first cell without errors.
