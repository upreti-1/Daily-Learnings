# Insurance Premium Prediction System 🛡️

A full-stack Machine Learning application that predicts insurance premium categories using a FastAPI backend and a Streamlit frontend.

## 📁 Project Overview
This project demonstrates the end-to-end deployment of a Scikit-Learn model. It takes raw user data (weight, height, age, etc.), performs real-time feature engineering (BMI, City Tier, Lifestyle Risk), and returns a predicted insurance category.

## 🛠️ Tech Stack
* **Backend:** FastAPI (Python)
* **Frontend:** Streamlit
* **ML Library:** Scikit-Learn (Random Forest)
* **Data Validation:** Pydantic
* **Environment:** Python 3.12 Virtual Environment (venv)

## 🚀 How to Run

### 1. Setup the Environment
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn pandas scikit-learn streamlit requests

# 2.. Start the Backend (FastAPI)
uvicorn app:app --reload

# 3. Start the Frontend (Streamlit)
streamlit run frontend.py