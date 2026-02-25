import streamlit as st
import pandas as pd
import plotly.express as px
from model import train_model, predict_new_customer

st.set_page_config(page_title="Netflix Churn Strategist", page_icon="🎬", layout="wide", initial_sidebar_state="collapsed")

# Inject Custom High-End CSS
st.markdown("""
<style>
    /* Global Settings & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        scroll-behavior: smooth !important;
    }
    
    /* Ultimate Premium Background */
    .stApp {
        background: #000000;
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(229, 9, 20, 0.05), transparent 25%),
            radial-gradient(circle at 85% 30%, rgba(229, 9, 20, 0.05), transparent 25%);
        color: #ededed;
    }

    /* Top Bar Header */
    header[data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0.5) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }
    
    /* Elegant Form Container */
    [data-testid="stForm"] {
        background: rgba(10, 10, 10, 0.6) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 16px !important;
        padding: 40px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 24px 48px -12px rgba(0, 0, 0, 0.5) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }
    
    [data-testid="stForm"]:hover {
        border-color: rgba(229, 9, 20, 0.3) !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 24px 48px -12px rgba(229, 9, 20, 0.15) !important;
    }

    /* Sleek Inputs */
    div[data-baseweb="input"] > div, 
    div[data-baseweb="select"] > div, 
    div[data-baseweb="number-input"] > div {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
        color: #ffffff !important;
        transition: all 0.2s ease !important;
    }

    div[data-baseweb="input"] > div:hover, 
    div[data-baseweb="select"] > div:hover, 
    div[data-baseweb="number-input"] > div:hover {
        border-color: rgba(255, 255, 255, 0.2) !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
    }

    div[data-baseweb="input"]:focus-within > div, 
    div[data-baseweb="select"]:focus-within > div, 
    div[data-baseweb="number-input"]:focus-within > div {
        border-color: #E50914 !important;
        background-color: rgba(0, 0, 0, 0.5) !important;
        box-shadow: 0 0 0 1px #E50914 !important;
    }

    /* Labels */
    .stMarkdown label, label {
        font-weight: 500 !important;
        color: #a1a1aa !important;
        font-size: 0.9rem !important;
        margin-bottom: 4px !important;
    }

    /* Button Styling */
    div.stButton > button {
        background: #E50914 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        letter-spacing: 0.01em !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
        max-width: 300px !important;
        margin: 0 auto !important;
        display: block !important;
    }

    div.stButton > button:hover {
        background: #f6121d !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 16px rgba(229, 9, 20, 0.3) !important;
    }
    
    div.stButton > button:active {
        transform: translateY(0) !important;
        box-shadow: 0 4px 8px rgba(229, 9, 20, 0.3) !important;
    }

    /* Dashboard Metrics Containers */
    [data-testid="metric-container"] {
        background: rgba(15, 15, 15, 0.6) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 12px !important;
        padding: 24px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="metric-container"]:hover {
        border-color: rgba(255, 255, 255, 0.15) !important;
        transform: translateY(-4px) !important;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.4) !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        letter-spacing: -0.05em !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #a1a1aa !important;
        font-weight: 500 !important;
        font-size: 1.1rem !important;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
        padding-bottom: 8px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px !important;
        background-color: transparent !important;
        border: none !important;
        color: #a1a1aa !important;
        font-weight: 500 !important;
        font-size: 1.05rem !important;
        transition: color 0.2s ease !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #ffffff !important;
    }

    .stTabs [aria-selected="true"] {
        color: #ffffff !important;
        font-weight: 600 !important;
        border-bottom: 2px solid #E50914 !important;
    }
    
    /* Result Banners */
    .result-banner {
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 40px;
        animation: fadeIn 0.5s ease forwards;
        border: 1px solid;
    }
    
    .result-danger {
        background: rgba(229, 9, 20, 0.1);
        border-color: rgba(229, 9, 20, 0.3);
        box-shadow: 0 10px 30px rgba(229, 9, 20, 0.15);
    }
    
    .result-safe {
        background: rgba(16, 185, 129, 0.1);
        border-color: rgba(16, 185, 129, 0.3);
        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.15);
    }
    
    .result-danger h2 { color: #ff4d4f !important; margin: 0 0 10px 0 !important; font-size: 2.2rem !important; }
    .result-safe h2 { color: #10b981 !important; margin: 0 0 10px 0 !important; font-size: 2.2rem !important; }
    .result-desc { color: #d4d4d8 !important; font-size: 1.1rem !important; margin: 0 !important; }

    /* Keyframes */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* DataFrame & Scrollbars */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.2); }
    
    [data-testid="stDataFrame"] { border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.05); }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_and_train_model():
    return train_model()

model, metrics, X_columns = load_and_train_model()

# --- HERO SECTION ---
st.markdown("""
<div style="text-align: center; margin: 60px 0 50px 0; animation: fadeIn 0.8s ease;">
    <h1 style="font-size: 4rem; font-weight: 800; color: #ffffff; margin-bottom: 16px; line-height: 1.1;">
        Netflix Churn Strategist
    </h1>
    <p style="color: #a1a1aa; font-size: 1.25rem; max-width: 600px; margin: 0 auto; font-weight: 400; line-height: 1.6;">
        Advanced predictive analytics engine to identify at-risk subscribers before they cancel.
    </p>
</div>
""", unsafe_allow_html=True)

# --- TABS LAYOUT ---
tab1, tab2 = st.tabs(["Prediction Engine", "Analytics Dashboard"])

with tab1:
    col_spacer1, col_form, col_spacer2 = st.columns([1, 10, 1])
    
    with col_form:
        with st.form("prediction_form", clear_on_submit=False):
            st.markdown("<h3 style='margin-bottom: 24px; color: #ededed;'>Subscriber Profile</h3>", unsafe_allow_html=True)
            
            # Row 1: Demographics
            st.markdown("<p style='color: #888; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;'>Demographics</p>", unsafe_allow_html=True)
            r1c1, r1c2, r1c3 = st.columns(3)
            age = r1c1.number_input("Age", min_value=18, max_value=100, value=30)
            gender = r1c2.selectbox("Gender", ['Male', 'Female', 'Other'])
            region = r1c3.selectbox("Region", ['Africa', 'Europe', 'Asia', 'Oceania', 'South America', 'North America'])
            
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
            
            # Row 2: Account Details
            st.markdown("<p style='color: #888; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;'>Account Details</p>", unsafe_allow_html=True)
            r2c1, r2c2, r2c3 = st.columns(3)
            subscription_type = r2c1.selectbox("Plan Tier", ['Basic', 'Standard', 'Premium'])
            monthly_fee = r2c2.number_input("Monthly Fee ($)", min_value=0.0, value=12.99)
            payment_method = r2c3.selectbox("Payment Method", ['Credit Card', 'Debit Card', 'PayPal', 'Gift Card', 'Crypto'])
            
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

            # Row 3: Engagement Metrics
            st.markdown("<p style='color: #888; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;'>Engagement Metrics</p>", unsafe_allow_html=True)
            r3c1, r3c2, r3c3 = st.columns(3)
            watch_hours = r3c1.number_input("Monthly Watch Hours", min_value=0.0, max_value=1000.0, value=25.0)
            avg_watch_time_per_day = r3c2.number_input("Daily Average (Hours)", min_value=0.0, max_value=24.0, value=1.5)
            last_login_days = r3c3.number_input("Days Since Login", min_value=0, max_value=365, value=2)

            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

            # Row 4: Preferences
            st.markdown("<p style='color: #888; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;'>Preferences & Devices</p>", unsafe_allow_html=True)
            r4c1, r4c2, r4c3 = st.columns(3)
            device = r4c1.selectbox("Primary Device", ['TV', 'Mobile', 'Laptop', 'Desktop', 'Tablet'])
            favorite_genre = r4c2.selectbox("Top Genre", ['Action', 'Sci-Fi', 'Drama', 'Horror', 'Romance', 'Comedy', 'Documentary'])
            number_of_profiles = r4c3.number_input("Active Profiles", min_value=1, max_value=10, value=2)
            
            st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
            
            submitted = st.form_submit_button("Run Churn Analysis")

        if submitted:
            customer_data = {
                'age': age, 'gender': gender, 'subscription_type': subscription_type,
                'watch_hours': watch_hours, 'last_login_days': last_login_days, 'region': region,
                'device': device, 'monthly_fee': monthly_fee, 'payment_method': payment_method,
                'number_of_profiles': number_of_profiles, 'avg_watch_time_per_day': avg_watch_time_per_day,
                'favorite_genre': favorite_genre
            }
            
            with st.spinner("Processing demographic and engagement matrices..."):
                prediction = predict_new_customer(model, X_columns, customer_data)
            
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
            
            if prediction == 1:
                st.markdown("""
                <div class="result-banner result-danger">
                    <h2>High Churn Risk Detected</h2>
                    <p class="result-desc">The model indicates this subscriber exhibits behaviors highly correlated with cancellation. Recommend immediate retention intervention.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="result-banner result-safe">
                    <h2>Subscriber is Stable</h2>
                    <p class="result-desc">The model indicates strong retention traits. This subscriber is highly likely to continue their membership.</p>
                </div>
                """, unsafe_allow_html=True)

with tab2:
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom: 24px;'>Model Performance</h3>", unsafe_allow_html=True)
    
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    mcol1.metric("Accuracy", f"{metrics['accuracy'] * 100:.2f}%")
    mcol2.metric("Precision", f"{metrics['precision'] * 100:.2f}%")
    mcol3.metric("Recall", f"{metrics['recall'] * 100:.2f}%")
    mcol4.metric("F1 Score", f"{metrics['f1'] * 100:.2f}%")
    
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    fig_col1, fig_col2 = st.columns([1.5, 2])
    
    with fig_col1:
        st.markdown("#### Confusion Matrix")
        st.markdown("<p style='color: #888; font-size: 0.9rem;'>Actual vs Predicted Classification</p>", unsafe_allow_html=True)
        cm = metrics['confusion_matrix']
        fig = px.imshow(cm, text_auto=True, aspect="auto", color_continuous_scale='Reds',
                        labels=dict(x="Predicted", y="Actual", color="Count"),
                        x=['Retained (0)', 'Churned (1)'], 
                        y=['Retained (0)', 'Churned (1)'])
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#d4d4d8'),
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with fig_col2:
        st.markdown("#### Raw Data Feed")
        st.markdown("<p style='color: #888; font-size: 0.9rem;'>Preview of the latest batch records</p>", unsafe_allow_html=True)
        df = pd.read_csv("netflix_customer_churn.csv")
        st.dataframe(df.head(20), use_container_width=True, height=350)

