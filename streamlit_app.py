import streamlit as st
import pandas as pd
st.title('🤖Machine Learning App')

st.info("This is app builds a machine learning model")
df = pd.read_csv("wget https://raw.githubusercontent.com/pcarbo/qBio9_stuff/main/dogs.csv")
df
