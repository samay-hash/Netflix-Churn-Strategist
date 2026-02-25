import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pages.theme import inject_theme, page_header, section_label

inject_theme()

page_header(
    "Netflix · Churn Strategist",
    "Dataset Explorer",
    "Browse the raw Netflix customer churn dataset used to train and evaluate the model."
)

df = pd.read_csv("netflix_customer_churn.csv")

# ── Summary stats ──────────────────────────────────────────────────────────────
section_label("Dataset Overview", margin_top="0")

s1, s2, s3, s4 = st.columns(4)
s1.metric("Total Records",   f"{len(df):,}")
s2.metric("Feature Columns", f"{len(df.columns) - 1}")
s3.metric("Churned",        f"{int(df['churned'].sum()):,}")
s4.metric("Retention Rate", f"{1 - df['churned'].mean():.1%}")

st.markdown("<hr>", unsafe_allow_html=True)

# ── Filter controls ────────────────────────────────────────────────────────────
section_label("Filter & Search")

fc1, fc2, fc3 = st.columns([1, 1, 1.5])

if 'subscription_type' in df.columns:
    plan_filter = fc1.multiselect(
        "Plan Type",
        options=df['subscription_type'].unique().tolist(),
        default=df['subscription_type'].unique().tolist(),
        label_visibility="visible"
    )
    df = df[df['subscription_type'].isin(plan_filter)]

churn_filter = fc2.selectbox("Churn Status", ["All", "Churned", "Stayed"])
if churn_filter == "Churned":
    df = df[df['churned'] == 1]
elif churn_filter == "Stayed":
    df = df[df['churned'] == 0]

rows_to_show = fc3.slider("Rows to display", min_value=5, max_value=100, value=20, step=5)

st.markdown("<hr>", unsafe_allow_html=True)

# ── Data table ─────────────────────────────────────────────────────────────────
section_label(f"Records ({len(df):,} matching)")
st.dataframe(df.head(rows_to_show), width="stretch", hide_index=False)

st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

# ── Column info ────────────────────────────────────────────────────────────────
with st.expander("📋  Column Descriptions", expanded=False):
    col_info = {
        "age": "Customer age in years",
        "gender": "Gender identity of the customer",
        "subscription_type": "Netflix plan tier (Basic / Standard / Premium)",
        "watch_hours": "Total hours watched in the current month",
        "last_login_days": "Days elapsed since the customer last logged in",
        "region": "Geographic region of the customer",
        "device": "Primary device used to stream Netflix",
        "monthly_fee": "Monthly subscription cost in USD",
        "payment_method": "Payment method on file",
        "number_of_profiles": "Number of active user profiles on the account",
        "avg_watch_time_per_day": "Average hours spent watching per day",
        "favorite_genre": "Customer's most-watched content genre",
        "churned": "1 = cancelled subscription, 0 = still subscribed",
    }
    for col, desc in col_info.items():
        if col in df.columns:
            st.markdown(f"""
            <div style="display:flex;gap:1rem;padding:0.5rem 0;border-bottom:1px solid rgba(255,255,255,0.05);">
                <code style="color:#A09BFF;min-width:200px;font-size:0.82rem;">{col}</code>
                <span style="color:#64748B;font-size:0.82rem;">{desc}</span>
            </div>
            """, unsafe_allow_html=True)
