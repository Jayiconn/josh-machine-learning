import streamlit as st
import pandas as pd
st.title('🤖Machine Learning App')

st.info("This is app builds a machine learning model")
df = pd.read_csv("http://www.petrkeil.com/wp-content/uploads/2014/02/snakes.csv")
df
