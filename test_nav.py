import streamlit as st

predict_page = st.Page("pages/predict.py", title="Predict", default=True)
home_page = st.Page("pages/home.py", title="Home")
dataset_page = st.Page("pages/dataset.py", title="Dataset")

pg = st.navigation([predict_page, home_page, dataset_page])
pg.run()
