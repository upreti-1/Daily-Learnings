import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title('hello streamlit')

# Display a simple text
st.write("Hey! This is a simple text")

# create a dataframe and printing it
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

# Displaying the dataframe
st.write("Here is the data Frame")
st.write (df)

# Creating a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a','b','c']
)
st.line_chart(chart_data)
