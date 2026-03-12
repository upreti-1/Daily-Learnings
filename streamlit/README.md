# Streamlit Demos

This folder contains small Streamlit demo apps and helper modules used for interactive data exploration and simple classification demos.

## What you'll find here

- `app.py` — Main Streamlit app. Launches the interactive UI and ties together widgets and classification logic.
- `classification.py` — Contains classification helper functions and model-related code used by the app (preprocessing, training/prediction helpers).
- `widgets.py` — Reusable Streamlit widgets or UI components for the app.
- `sampled_data.csv` — A small sample dataset used by the demo (for local testing and examples).
- `streamlit.ipynb` — Notebook with notes or exploratory work related to the Streamlit app.

## Purpose / Overview

The example demonstrates how to build a lightweight interactive app with Streamlit for exploring a dataset and performing a simple classification task. It's intended as a learning/demo project rather than production-quality code.

## Quick start

1. Create and activate a Python virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install required packages. If you have a global requirements file, use it; otherwise install the common dependencies used by Streamlit demos:

```bash
pip install --upgrade pip
pip install streamlit pandas scikit-learn matplotlib seaborn
```

3. From this folder, run the Streamlit app:

```bash
cd /home/prashant/Desktop/Daily-Learnings/streamlit
streamlit run app.py
```

4. The app will open in your browser (or provide a local URL in the terminal). Use the UI to load the sample dataset and try classification options.

## Notes & assumptions

- The app expects `sampled_data.csv` to be present in the same folder. If the code loads data from a different path, update the path in `app.py` accordingly.
- If `classification.py` refers to a saved model file (e.g., a `joblib` or `pickle` file) that isn't present, the app may train a small model on-the-fly or show an error — inspect `classification.py` to confirm behavior.
- Adjust package list if the code uses additional libraries (e.g., `joblib`, `xgboost`, or `plotly`). Install them with pip as needed.

## File descriptions (more detail)

- `app.py`: Entry point for the Streamlit UI. Handles layout, user inputs, and calls functions from `widgets.py` and `classification.py`.
- `classification.py`: Data processing and model logic. Look here to see how features are engineered and how predictions are produced.
- `widgets.py`: Small helpers to keep UI code tidy (custom forms, sidebar controls, or plotting wrappers).

## Development tips

- Use `streamlit`'s `--logger.level=debug` flag if you need more console logs:

```bash
streamlit run app.py --logger.level=debug
```

- When iterating on the UI, Streamlit auto-reloads on file save. For heavier code changes, consider restarting the app.

## Troubleshooting

- If the app doesn't start, check for Python version compatibility (recommended: 3.8+).
- If imports fail, inspect `classification.py` and `widgets.py` for extra dependencies and install them.
- If the sample data file is missing or large, replace or point to a smaller CSV for quick testing.

## License

This repository contains learning/demo code. No license is set — if you plan to share or use it widely, add a LICENSE file.

---

If you'd like, I can:
- generate a `requirements.txt` containing detected dependencies,
- add a short example screenshot and usage notes to the README,
- or open `app.py` and verify the exact packages used and update the README accordingly.
