import streamlit as st
import warnings
import os
import logging

# Suppress HuggingFace, transformer, and PyTorch dependency warnings
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", message=".*unauthenticated.*")
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)

st.set_page_config(
    page_title="Netflix Churn Strategist", 
    page_icon="🎬", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

predict_page = st.Page("views/predict.py", title="Predict Churn", icon=":material/analytics:")
home_page = st.Page("views/home.py", title="Model Dashboard", icon=":material/dashboard:")
dataset_page = st.Page("views/dataset.py", title="Dataset Explorer", icon=":material/database:")

ai_strategist_page = st.Page("views/ai_strategist.py", title="AI Strategist", icon=":material/smart_toy:", default=True)
ai_auditor_page = st.Page("views/ai_auditor.py", title="AI Data Auditor", icon=":material/manage_search:")
batch_agent_page = st.Page("views/batch_agent.py", title="Batch Campaign Agent", icon=":material/rocket_launch:")

pg = st.navigation({
    "Agentic AI Studio": [ai_strategist_page, ai_auditor_page, batch_agent_page],
    "Core Predictor": [predict_page, home_page, dataset_page]
})
pg.run()
