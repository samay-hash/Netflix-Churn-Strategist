import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pages.theme import inject_theme, page_header, section_label
from model import train_model
import plotly.graph_objects as go

inject_theme()

@st.cache_resource
def get_model():
    return train_model()

model, metrics, X_columns = get_model()

page_header(
    "Netflix · Churn Strategist",
    "Model Dashboard",
    "Live performance metrics for the Decision Tree classifier trained on Netflix customer data."
)

# ── KPI Cards ─────────────────────────────────────────────────────────────────
section_label("Model Performance", margin_top="0")
k1, k2, k3, k4 = st.columns(4)
k1.metric("Accuracy",  f"{metrics['accuracy']:.2%}")
k2.metric("Precision", f"{metrics['precision']:.2%}")
k3.metric("Recall",    f"{metrics['recall']:.2%}")
k4.metric("F1 Score",  f"{metrics['f1']:.2%}")

st.markdown("<hr>", unsafe_allow_html=True)

# ── Info cards row ─────────────────────────────────────────────────────────────
section_label("About This Model")
i1, i2, i3 = st.columns(3)

def info_card(col, icon, title, body):
    col.markdown(f"""
    <div style="background:rgba(255,255,255,0.025);border:1px solid rgba(255,255,255,0.08);
                border-radius:14px;padding:1.4rem;height:100%;">
        <div style="font-size:1.6rem;margin-bottom:0.6rem;">{icon}</div>
        <p style="color:#A09BFF;font-size:0.82rem;font-weight:700;margin:0 0 5px;">{title}</p>
        <p style="color:#64748B;font-size:0.8rem;line-height:1.6;margin:0;">{body}</p>
    </div>
    """, unsafe_allow_html=True)

info_card(i1, "🌳", "Algorithm", "Decision Tree Classifier with Gini impurity, trained on labelled customer subscription data.")
info_card(i2, "📦", "Dataset", "Netflix customer churn dataset covering demographics, subscription plans, and viewing behaviour.")
info_card(i3, "🎯", "Task", "Binary classification — predicts whether a customer will churn (cancel) or stay subscribed.")

st.markdown("<hr>", unsafe_allow_html=True)

# ── Confusion Matrix ───────────────────────────────────────────────────────────
section_label("Confusion Matrix")
_, cm_col, _ = st.columns([1, 2, 1])
with cm_col:
    cm = metrics['confusion_matrix']
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=['Stayed', 'Churned'],
        y=['Stayed', 'Churned'],
        text=[[str(v) for v in row] for row in cm],
        texttemplate="<b>%{text}</b>",
        textfont={"size": 28, "color": "white"},
        colorscale=[
            [0.0, '#0C0E18'],
            [0.5, '#231A5E'],
            [1.0, '#6C63FF'],
        ],
        showscale=False,
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter', color='#64748B', size=13),
        margin=dict(l=20, r=20, t=20, b=20),
        height=320,
        xaxis=dict(title='Predicted Label', showgrid=False),
        yaxis=dict(title='Actual Label',    showgrid=False),
    )
    st.plotly_chart(fig, width="stretch")
