import streamlit as st
import pandas as pd
st.title('🤖Machine Learning App')

st.info("This is app builds a machine learning model")
df = pd.read_csv("species_to_country_mapping.csv")
df
