import streamlit as st
import requests

API_URL = 'http://localhost:8000/predict'

st.title("Insurance Premium Category Predictor")

st.markdown("Enter your details below: ")

# input feilds
age = st.number_input('Age', min_value = 1, max_value = 200, value = 30)
weight = st.number_input('weighty (kg)', min_value = 1.0, max_value = 200.0, value = 30.0)
height = st.number_input('height (m)', min_value = 0.5, max_value = 4.0, value = 1.3)
income_lpa = st.number_input('Income (LPA)', min_value = 1.0, value = 3.0)
smoker = st.selectbox('Are you a smoker?', options = [True, False])
city = st.text_input('City', value = 'Mumbai')
occupation = st.selectbox(
    "Occupation",
    ['unemployed', 'retired', 'freelancer', 'student', 'government_job',
       'private_job', 'business_owner']
)

if st.button("Predict Premium Category"):
    input_data = {
        'age' : age,
        'weight' : weight,
        'height' : height,
        'income_lpa' : income_lpa,
        'smoker' : smoker,
        'city' : city,
        'occupation' : occupation
    }

    try:
        response = requests.post(API_URL, json = input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance category is:  **{result}**")
        else:
            st.error(f'API Error: {response.status_code} - {response.text}')
        
    except requests.exceptions.ConnectionError:
        st.error("could not connect to the fastAPI server. Make sure it is up and running on the given port")