import streamlit as st
import pandas as pd
from model import train_model

st.set_page_config(page_title="Netflix Churn Prediction", page_icon="🎬", layout="centered")

st.title("🎬 Netflix Customer Churn Prediction")
st.markdown("This Streamlit app trains a **Decision Tree Classifier** on the Netflix Customer Churn dataset and displays the performance metrics.")

with st.spinner("Training Model... Please wait!"):
    model, metrics = train_model()

st.success("Model trained successfully!")

st.header("📊 Model Performance", divider="red")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", f"{metrics['accuracy']:.4f}")
col2.metric("Precision", f"{metrics['precision']:.4f}")
col3.metric("Recall", f"{metrics['recall']:.4f}")
col4.metric("F1 Score", f"{metrics['f1']:.4f}")

st.header("🔍 Dataset Preview", divider="red")

df = pd.read_csv("netflix_customer_churn.csv")
st.dataframe(df.head(10))

st.markdown("---")
st.caption("Developed dynamically based on Google Colab to Streamlit migration guidelines.")
