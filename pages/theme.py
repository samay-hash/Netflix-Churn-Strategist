import streamlit as st

def inject_theme():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

/* ── App background ── */
.stApp {
    background: #080B14;
    background-image:
        radial-gradient(ellipse 65% 50% at 100% 0%,  rgba(108,99,255,0.09) 0%, transparent 60%),
        radial-gradient(ellipse 45% 35% at 0%  100%, rgba(0,212,170,0.05)  0%, transparent 55%);
    background-attachment: fixed;
}

/* ── Hide default chrome ── */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent !important; }
.block-container { padding: 3.2rem 2.8rem 4rem !important; max-width: 1240px !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #080B14; }
::-webkit-scrollbar-thumb { background: #6C63FF; border-radius: 4px; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: #0C0E18 !important;
    border-right: 1px solid rgba(255,255,255,0.07) !important;
}
section[data-testid="stSidebar"] .block-container { padding: 0 !important; }

/* ── Inputs ── */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div:first-child {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 9px !important;
    color: #E2E8F0 !important;
    transition: all 0.2s ease !important;
}
div[data-baseweb="input"] > div:hover,
div[data-baseweb="select"] > div:first-child:hover {
    border-color: rgba(108,99,255,0.45) !important;
}
div[data-baseweb="input"]:focus-within > div,
div[data-baseweb="select"]:focus-within > div:first-child {
    border-color: #6C63FF !important;
    box-shadow: 0 0 0 3px rgba(108,99,255,0.14) !important;
}
input { color: #E2E8F0 !important; }

/* ── Labels ── */
label[data-testid="stWidgetLabel"] p {
    color: #64748B !important; font-size: 0.75rem !important;
    font-weight: 600 !important; letter-spacing: 0.4px !important;
    text-transform: uppercase !important;
}

/* ── Number input buttons ── */
[data-testid="stNumberInput"] button {
    background: rgba(255,255,255,0.04) !important;
    border-color: rgba(255,255,255,0.09) !important;
    color: #6C63FF !important; border-radius: 6px !important;
}
[data-testid="stNumberInput"] button:hover {
    background: rgba(108,99,255,0.15) !important;
}

/* ── Submit button ── */
div.stFormSubmitButton > button,
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #6C63FF 0%, #5A52D5 100%) !important;
    color: #fff !important;
    border: 1px solid rgba(108,99,255,0.4) !important;
    border-radius: 10px !important;
    font-weight: 700 !important; font-size: 0.95rem !important;
    padding: 0.68rem 2rem !important;
    box-shadow: 0 4px 18px rgba(108,99,255,0.32) !important;
    transition: all 0.22s ease !important;
    width: 100%;
}
div.stFormSubmitButton > button:hover,
div.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 26px rgba(108,99,255,0.48) !important;
}

/* ── Metric cards ── */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 1.2rem 1.4rem !important;
    transition: all 0.22s ease;
}
[data-testid="stMetric"]:hover {
    border-color: rgba(108,99,255,0.3);
    background: rgba(108,99,255,0.05);
    transform: translateY(-3px);
    box-shadow: 0 8px 22px rgba(0,0,0,0.25);
}
[data-testid="stMetricLabel"] p {
    color: #64748B !important; font-size: 0.72rem !important;
    font-weight: 700 !important; text-transform: uppercase; letter-spacing: 0.8px;
}
[data-testid="stMetricValue"] div {
    color: #E2E8F0 !important; font-size: 1.9rem !important; font-weight: 800 !important;
}

/* ── Dividers ── */
hr { border: none !important; border-top: 1px solid rgba(255,255,255,0.07) !important; margin: 1.5rem 0 !important; }

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 12px !important; overflow: hidden !important;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: #6C63FF !important; }

/* ── Form card ── */
[data-testid="stForm"] {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 1.8rem 2rem !important;
    transition: border-color 0.2s;
}
[data-testid="stForm"]:hover { border-color: rgba(108,99,255,0.2); }

/* ── Animations ── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}
.fade-up { animation: fadeUp 0.4s ease forwards; }

/* ── Select dropdown ── */
ul[role="listbox"] {
    background: #12141F !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 9px !important;
}
ul[role="listbox"] li { color: #C9D1D9 !important; }
ul[role="listbox"] li:hover,
ul[role="listbox"] li[aria-selected="true"] {
    background: rgba(108,99,255,0.12) !important;
    color: #A09BFF !important;
}
</style>
""", unsafe_allow_html=True)


def page_header(eyebrow: str, title: str, subtitle: str):
    st.markdown(f"""
    <div style="margin-bottom:2rem;">
        <p style="color:#6C63FF;font-size:0.68rem;font-weight:700;
                  letter-spacing:3px;text-transform:uppercase;margin:0 0 5px;">{eyebrow}</p>
        <h1 style="color:#E2E8F0;font-size:1.85rem;font-weight:800;
                   letter-spacing:-0.6px;margin:0 0 6px;line-height:1.2;">{title}</h1>
        <p style="color:#64748B;font-size:0.875rem;margin:0;max-width:580px;line-height:1.6;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def section_label(text: str, margin_top: str = "1.5rem"):
    st.markdown(f"""
    <p style="color:#64748B;font-size:0.68rem;font-weight:700;letter-spacing:2px;
              text-transform:uppercase;margin:{margin_top} 0 0.7rem;
              border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:6px;">{text}</p>
    """, unsafe_allow_html=True)
