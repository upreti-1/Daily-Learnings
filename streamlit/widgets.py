import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello, {name}")

age = st.slider("Select your age ", 18,100,25)
st.write(f'Your age is {age}.')

options = ['Python', 'java', 'c', 'JavaScript']
choice = st.selectbox("choose your programming language: ", options)
st.write(f'You choose: {choice}.')

choices = ['Nepal', 'India', 'England']
select = st.select_slider("Who won last game: ", choices, 'India')
st.write(f'You selected : {select}.')

data = {
    'name':['Prashant', 'jake', 'jane','jaguar'],
    'age': [20,30,40,50],
    'city': ['Bangalore','delhi','chennai','patna']
}

df = pd.DataFrame(data)
df.to_csv('sampled_data.csv')
st.write (f"The data is : ")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file: ", type= 'csv')
if uploaded_file is not None:
    dff = pd.read_csv(uploaded_file)
    st.write(dff)