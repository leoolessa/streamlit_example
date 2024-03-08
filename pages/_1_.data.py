import streamlit as st
import pandas as pd
import src.manage_data as cleaning

df = cleaning.load_dataframe()

# df = load_daatframe
st.write('Adventure time data')
st.dataframe(df)