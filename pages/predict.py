import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pages.theme import inject_theme, page_header, section_label
from model import train_model, predict_new_customer

inject_theme()

@st.cache_resource
def get_model():
    return train_model()

model, metrics, X_columns = get_model()

page_header(
    "Netflix · Churn Strategist",
    "Predict Customer Churn",
    "Enter the customer's details and click Predict to see whether they're at risk of cancelling."
)

with st.form("churn_form"):

    # ── Demographics ───────────────────────────────────────────────────────────
    section_label("👤  Demographics", margin_top="0")
    c1, c2, c3 = st.columns(3)
    age    = c1.number_input("Age",    min_value=18, max_value=100, value=30)
    gender = c2.selectbox("Gender",  ['Male', 'Female', 'Other'])
    region = c3.selectbox("Region",  ['Africa', 'Europe', 'Asia', 'Oceania', 'South America', 'North America'])

    # ── Subscription ──────────────────────────────────────────────────────────
    section_label("💳  Subscription & Device")
    c4, c5, c6 = st.columns(3)
    subscription_type = c4.selectbox("Plan",    ['Basic', 'Standard', 'Premium'])
    device            = c5.selectbox("Device",  ['TV', 'Mobile', 'Laptop', 'Desktop', 'Tablet'])
    payment_method    = c6.selectbox("Payment", ['Gift Card', 'Crypto', 'Debit Card', 'PayPal', 'Credit Card'])

    # ── Viewing Activity ───────────────────────────────────────────────────────
    section_label("📺  Viewing Activity")
    c7, c8, c9 = st.columns(3)
    watch_hours            = c7.number_input("Monthly Watch Hrs",  min_value=0.0,  max_value=1000.0, value=15.0)
    last_login_days        = c8.number_input("Days Since Login",   min_value=0,    max_value=365,    value=5)
    avg_watch_time_per_day = c9.number_input("Avg Hrs / Day",      min_value=0.0,  max_value=24.0,   value=1.5)

    # ── Account ────────────────────────────────────────────────────────────────
    section_label("⚙️  Account Preferences")
    c10, c11, c12 = st.columns(3)
    monthly_fee        = c10.number_input("Monthly Fee ($)", min_value=0.0, value=12.99, step=0.01, format="%.2f")
    number_of_profiles = c11.number_input("Active Profiles", min_value=1,  max_value=10, value=2)
    favorite_genre     = c12.selectbox("Favourite Genre",
                                       ['Action', 'Sci-Fi', 'Drama', 'Horror', 'Romance', 'Comedy', 'Documentary'])

    st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)

    _, btn_col, _ = st.columns([2, 2.5, 2])
    with btn_col:
        submitted = st.form_submit_button("⚡  Predict Churn Risk", type="primary", width="stretch")

# ── Prediction Result ──────────────────────────────────────────────────────────
if submitted:
    customer_data = {
        'age': age, 'gender': gender,
        'subscription_type': subscription_type,
        'watch_hours': watch_hours,
        'last_login_days': last_login_days,
        'region': region, 'device': device,
        'monthly_fee': monthly_fee,
        'payment_method': payment_method,
        'number_of_profiles': number_of_profiles,
        'avg_watch_time_per_day': avg_watch_time_per_day,
        'favorite_genre': favorite_genre,
    }
    with st.spinner("Analysing customer data…"):
        prediction = predict_new_customer(model, X_columns, customer_data)

    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

    if prediction == 1:
        left_r, right_r = st.columns([1, 1])
        with left_r:
            st.markdown("""
            <div class="fade-up" style="
                background: linear-gradient(135deg, rgba(255,107,107,0.07), rgba(255,60,60,0.03));
                border: 1px solid rgba(255,107,107,0.25);
                border-left: 4px solid #FF6B6B;
                border-radius: 16px; padding: 1.8rem;
            ">
                <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem;">
                    <div style="width:52px;height:52px;border-radius:14px;background:rgba(255,107,107,0.1);
                                display:flex;align-items:center;justify-content:center;font-size:1.6rem;flex-shrink:0;">⚠️</div>
                    <div>
                        <p style="color:#FF6B6B;font-size:1.15rem;font-weight:800;margin:0;letter-spacing:-0.3px;">High Churn Risk</p>
                        <p style="color:#64748B;font-size:0.78rem;margin:0;">Predicted to cancel subscription</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with right_r:
            st.markdown("""
            <div class="fade-up" style="
                background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.08);
                border-radius:16px;padding:1.8rem;height:100%;
            ">
                <p style="color:#A09BFF;font-size:0.72rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin:0 0 0.8rem;">
                    💡 Retention Strategy
                </p>
                <ul style="color:#64748B;font-size:0.83rem;line-height:1.8;margin:0;padding-left:1.2rem;">
                    <li>Send a personalised re-engagement email</li>
                    <li>Offer a temporary discount or free month</li>
                    <li>Recommend content based on their genre</li>
                    <li>Consider downgrading plan to reduce cost friction</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    else:
        left_r, right_r = st.columns([1, 1])
        with left_r:
            st.markdown("""
            <div class="fade-up" style="
                background: linear-gradient(135deg, rgba(0,212,170,0.07), rgba(0,180,140,0.03));
                border: 1px solid rgba(0,212,170,0.22);
                border-left: 4px solid #00D4AA;
                border-radius: 16px; padding: 1.8rem;
            ">
                <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem;">
                    <div style="width:52px;height:52px;border-radius:14px;background:rgba(0,212,170,0.1);
                                display:flex;align-items:center;justify-content:center;font-size:1.6rem;flex-shrink:0;">✅</div>
                    <div>
                        <p style="color:#00D4AA;font-size:1.15rem;font-weight:800;margin:0;letter-spacing:-0.3px;">Low Churn Risk</p>
                        <p style="color:#64748B;font-size:0.78rem;margin:0;">Predicted to remain subscribed</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with right_r:
            st.markdown("""
            <div class="fade-up" style="
                background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.08);
                border-radius:16px;padding:1.8rem;height:100%;
            ">
                <p style="color:#00D4AA;font-size:0.72rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin:0 0 0.8rem;">
                    💡 Growth Opportunity
                </p>
                <ul style="color:#64748B;font-size:0.83rem;line-height:1.8;margin:0;padding-left:1.2rem;">
                    <li>Strong engagement — ideal for upsell campaigns</li>
                    <li>Offer Premium plan upgrade with added perks</li>
                    <li>Enrol in loyalty or referral rewards program</li>
                    <li>Surface new releases matching their favourite genre</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
