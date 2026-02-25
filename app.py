import streamlit as st

st.set_page_config(
    page_title="Netflix Churn Strategist", 
    page_icon="🎬", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

predict_page = st.Page("pages/predict.py", title="Predict Churn", icon="🔮", default=True)
home_page = st.Page("pages/home.py", title="Model Dashboard", icon="📊")
dataset_page = st.Page("pages/dataset.py", title="Dataset Explorer", icon="📁")

pg = st.navigation([predict_page, home_page, dataset_page])
pg.run()
