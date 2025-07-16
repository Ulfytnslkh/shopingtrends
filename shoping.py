import pickle
import streamlit as st


# Membaca mode Shoping
shoping_model = pickle.load(open('shopping_data.sav', 'rb'))

# JUDUL

st.title('SHOOPING TRENDS')
