import streamlit as st
import pandas as pd
import plotly.express as px
from model import train_model, predict_new_customer

st.set_page_config(page_title="Netflix Churn Strategist", page_icon="🎬", layout="wide")

st.markdown("""
<style>
    /* Main Static Mesh Background */
    .stApp {
        background-color: #0A0C10;
        background-image: 
            radial-gradient(ellipse at 0% 50%, rgba(229, 9, 20, 0.15) 0%, transparent 50%),
            radial-gradient(ellipse at 100% 50%, rgba(48, 54, 61, 0.3) 0%, transparent 50%),
            linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
        background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
        background-attachment: fixed;
    }
    
    /* Form Smooth Load Animation */
    @keyframes smoothLoad {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Form & Input Customization */
    [data-testid="stForm"] {
        background: linear-gradient(180deg, rgba(22, 27, 34, 0.75), rgba(16, 20, 26, 0.85));
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(48, 54, 61, 0.4);
        border-radius: 12px;
        padding: 25px;
        animation: smoothLoad 0.6s ease-out forwards;
        transition: all 0.3s ease;
    }
    
    [data-testid="stForm"]:hover {
        border-color: rgba(229, 9, 20, 0.3);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3) !important;
    }

    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
        background-color: rgba(13, 17, 23, 0.8) !important;
        border: 1px solid rgba(48, 54, 61, 0.5) !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }
    
    /* Hover Effects & Gaming Cursor */
    [data-testid="stForm"]:hover,
    div[data-baseweb="input"] > div:hover, 
    div[data-baseweb="select"] > div:hover {
        cursor: cell !important;
        border-color: #E50914 !important;
        box-shadow: 0 4px 20px rgba(229, 9, 20, 0.1) !important;
    }
    
    div[data-baseweb="input"]:focus-within > div, div[data-baseweb="select"]:focus-within > div {
        border-color: #E50914 !important;
        box-shadow: 0 0 0 1px #E50914 !important;
    }

    /* Primary Button Customization (Predict Button) */
    div.stButton > button {
        background-color: #E50914;
        color: white;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 14px 0 rgba(229, 9, 20, 0.39);
        transition: all 0.3s ease-in-out;
        font-weight: 600;
        padding: 0.6rem 2rem;
        letter-spacing: 0.5px;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.5);
        background-color: #F40612;
        color: white;
    }
    
    /* Metric Cards (Tab 2) */
    .stMetric {
        background: linear-gradient(145deg, rgba(22, 27, 34, 0.6), rgba(16, 20, 26, 0.8));
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(48, 54, 61, 0.3);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        transition: all 0.4s ease;
    }
    .stMetric:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 24px rgba(229, 9, 20, 0.12);
        border: 1px solid rgba(229, 9, 20, 0.6);
        background: linear-gradient(145deg, rgba(22, 27, 34, 0.8), rgba(28, 14, 18, 0.9));
    }
    
    /* Top Tabs Styling */
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        transition: all 0.3s ease;
        border-radius: 6px 6px 0 0;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #E50914;
        background-color: rgba(229, 9, 20, 0.05);
    }
    
    /* Animations & Dynamic Elements */
    @keyframes dropDown {
        0% { transform: translateY(-30px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    @keyframes slideUpFade {
        0% { transform: translateY(30px) scale(0.98); opacity: 0; }
        100% { transform: translateY(0) scale(1); opacity: 1; }
    }
    
    .animated-header {
        animation: dropDown 0.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
        text-align: center;
        padding: 1.5rem 0 3rem 0;
    }
    
    .animated-result {
        animation: slideUpFade 0.6s cubic-bezier(0.25, 1, 0.5, 1) forwards;
        text-align: center;
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 15px;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    
    .low-risk {
        background: linear-gradient(90deg, rgba(46, 160, 67, 0.05), rgba(46, 160, 67, 0.15), rgba(46, 160, 67, 0.05));
        border: 1px solid rgba(46, 160, 67, 0.3);
        box-shadow: 0 8px 30px rgba(46, 160, 67, 0.1);
        color: #46c759;
    }
    
    .high-risk {
        background: linear-gradient(90deg, rgba(229, 9, 20, 0.05), rgba(229, 9, 20, 0.15), rgba(229, 9, 20, 0.05));
        border: 1px solid rgba(229, 9, 20, 0.3);
        box-shadow: 0 8px 30px rgba(229, 9, 20, 0.15);
        color: #ff6b6b;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_and_train_model():
    return train_model()

model, metrics, X_columns = load_and_train_model()

st.markdown("""
<div class="animated-header">
    <h1 style="color: white; font-size: 3.5rem; font-weight: 800; margin-bottom: 10px; letter-spacing: -1px;">🎬 Netflix Customer Churn Strategist</h1>
    <p style="color: #8B949E; font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.6;">
        Welcome to the Netflix Customer Churn Prediction System. This professional tool analyzes customer 
        viewing behavior, subscription details, and demographics to evaluate the likelihood of churning using a 
        Classical Machine Learning algorithm.
    </p>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🔮 Single Customer Prediction", "📊 Model Dashboard & Metrics"])

with tab1:
    st.markdown("### Enter Customer Details to Predict Churn Risk")
    
    with st.form("prediction_form"):
        st.markdown("#### 👤 Demographic Information")
        col1, col2, col3 = st.columns(3)
        age = col1.number_input("Age", min_value=18, max_value=100, value=30)
        gender = col2.selectbox("Gender", ['Male', 'Female', 'Other'])
        region = col3.selectbox("Region", ['Africa', 'Europe', 'Asia', 'Oceania', 'South America', 'North America'])
        
        st.markdown("#### 📱 Subscription & Device Information")
        col4, col5, col6 = st.columns(3)
        subscription_type = col4.selectbox("Subscription Type", ['Basic', 'Standard', 'Premium'])
        device = col5.selectbox("Device", ['TV', 'Mobile', 'Laptop', 'Desktop', 'Tablet'])
        payment_method = col6.selectbox("Payment Method", ['Gift Card', 'Crypto', 'Debit Card', 'PayPal', 'Credit Card'])
        
        st.markdown("#### 🎬 Usage & Viewing Activity")
        col7, col8, col9 = st.columns(3)
        watch_hours = col7.number_input("Total Watch Hours (Monthly)", min_value=0.0, max_value=1000.0, value=15.0)
        last_login_days = col8.number_input("Days Since Last Login", min_value=0, max_value=365, value=5)
        avg_watch_time_per_day = col9.number_input("Average Watch Time Per Day (Hours)", min_value=0.0, max_value=24.0, value=1.5)
        
        st.markdown("#### ⚙️ Account Preferences")
        col10, col11, col12 = st.columns(3)
        monthly_fee = col10.number_input("Monthly Subscription Fee ($)", min_value=0.0, value=12.99)
        number_of_profiles = col11.number_input("Number of Active Profiles", min_value=1, max_value=10, value=2)
        favorite_genre = col12.selectbox("Favorite Genre", ['Action', 'Sci-Fi', 'Drama', 'Horror', 'Romance', 'Comedy', 'Documentary'])
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Predict Churn Risk", type="primary")

    if submitted:
        customer_data = {
            'age': age,
            'gender': gender,
            'subscription_type': subscription_type,
            'watch_hours': watch_hours,
            'last_login_days': last_login_days,
            'region': region,
            'device': device,
            'monthly_fee': monthly_fee,
            'payment_method': payment_method,
            'number_of_profiles': number_of_profiles,
            'avg_watch_time_per_day': avg_watch_time_per_day,
            'favorite_genre': favorite_genre
        }
        
        with st.spinner("Analyzing customer behavior..."):
            prediction = predict_new_customer(model, X_columns, customer_data)
        
        if prediction == 1:
            st.markdown("""
            <div class="animated-result high-risk">
                <h3 style="margin: 0 0 8px 0; font-size: 1.8rem; color: #ff6b6b;">⚠️ HIGH RISK OF CHURN</h3>
                <p style="margin: 0; font-size: 1.1rem; color: #e6edf3;">This customer is predicted to <strong>cancel their subscription</strong></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="animated-result low-risk">
                <h3 style="margin: 0 0 8px 0; font-size: 1.8rem; color: #46c759;">✅ LOW RISK</h3>
                <p style="margin: 0; font-size: 1.1rem; color: #e6edf3;">This customer is predicted to <strong>STAY</strong></p>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 📊 Decision Tree Performance on Test Data")
    
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    mcol1.metric("Accuracy", f"{metrics['accuracy']:.4f}")
    mcol2.metric("Precision", f"{metrics['precision']:.4f}")
    mcol3.metric("Recall", f"{metrics['recall']:.4f}")
    mcol4.metric("F1 Score", f"{metrics['f1']:.4f}")
    
    st.markdown("---")
    
    st.markdown("### 🔍 Confusion Matrix")
    cm = metrics['confusion_matrix']
    
    st.markdown("<h4 style='text-align: center; color: white;'>Actual vs Predicted Churn Classes</h4>", unsafe_allow_html=True)
    fig = px.imshow(cm, text_auto=True, aspect="auto", color_continuous_scale='Reds',
                    labels=dict(x="Predicted Label", y="Actual Label", color="Count"),
                    x=['Stayed (0)', 'Churned (1)'], 
                    y=['Stayed (0)', 'Churned (1)'])
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    st.plotly_chart(fig, width="stretch")
    
    st.markdown("---")
    
    st.markdown("### 📂 Dataset Preview")
    df = pd.read_csv("netflix_customer_churn.csv")
    st.dataframe(df.head(15), width="stretch")
