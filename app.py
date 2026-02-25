import streamlit as st

st.set_page_config(
    page_title="Netflix · Churn Strategist",
    page_icon="📡",
    layout="wide",
)

# ── Sidebar brand header ───────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

/* App background */
.stApp {
    background: #080B14;
    background-image:
        radial-gradient(ellipse 60% 45% at 100% 0%,  rgba(108,99,255,0.09) 0%, transparent 58%),
        radial-gradient(ellipse 40% 35% at 0%  100%, rgba(0,212,170,0.05)  0%, transparent 55%);
    background-attachment: fixed;
}
#MainMenu, footer { visibility: hidden; }

/* Sidebar shell */
section[data-testid="stSidebar"] {
    background: #0C0E18 !important;
    border-right: 1px solid rgba(255,255,255,0.07) !important;
    width: 240px !important;
}
section[data-testid="stSidebar"] .block-container { padding: 0 !important; }

/* Nav links */
[data-testid="stSidebarNav"] { padding-top: 0 !important; gap: 2px; }
[data-testid="stSidebarNav"] a {
    border-radius: 9px !important;
    padding: 9px 14px !important;
    color: #64748B !important;
    font-size: 0.875rem !important;
    font-weight: 600 !important;
    transition: all 0.18s ease !important;
    margin: 1px 6px !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    text-decoration: none !important;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(108,99,255,0.1) !important;
    color: #A09BFF !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(108,99,255,0.18) !important;
    color: #A09BFF !important;
    border: 1px solid rgba(108,99,255,0.3) !important;
}

/* Collapse arrow */
[data-testid="collapsedControl"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# Sidebar brand block
with st.sidebar:
    st.markdown("""
    <div style="padding:1.3rem 1rem 0.6rem;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:0.3rem;">
            <div style="background:#E50914;border-radius:5px;width:22px;height:22px;
                        display:flex;align-items:center;justify-content:center;
                        color:white;font-size:0.65rem;font-weight:900;flex-shrink:0;">N</div>
            <span style="color:#E2E8F0;font-size:0.95rem;font-weight:800;letter-spacing:-0.2px;">Churn Strategist</span>
        </div>
        <p style="color:#2D3748;font-size:0.68rem;margin:0 0 1rem;padding-left:30px;">Decision Tree · AI</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color:#2D3748;font-size:0.65rem;font-weight:700;letter-spacing:2px;
              text-transform:uppercase;margin:0.5rem 0.8rem 0.4rem;padding-bottom:5px;
              border-bottom:1px solid rgba(255,255,255,0.05);">Navigation</p>
    """, unsafe_allow_html=True)

# ── Pages ─────────────────────────────────────────────────────────────────────
home_page    = st.Page("pages/home.py",    title="Dashboard",     icon="🏠")
predict_page = st.Page("pages/predict.py", title="Predict Churn", icon="🔮")
dataset_page = st.Page("pages/dataset.py", title="Dataset",       icon="📂")

pg = st.navigation([predict_page, home_page, dataset_page], position="sidebar")
pg.run()
