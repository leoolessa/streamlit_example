import streamlit as st
import src.manage_data as cleaning

df = cleaning.load_dataframe()

# df = load_daatframe
st.write('Adventure time data')
st.Dataframe(df)