<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" alt="Netflix Logo" width="150"/>
  <br>
  <h1>🎬 Netflix Customer Churn Strategist</h1>
  <p><strong>A SaaS-grade Classical Machine Learning Platform for Predictive Churn Analytics</strong></p>
  
  [![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
  [![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
  [![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
  [![Deployment](https://img.shields.io/badge/Deployed-Streamlit_Cloud-success.svg?style=for-the-badge)](#)
</div>

<hr>

## 📌 Executive Overview
**Milestone 1 Core Deliverable**

The **Netflix Customer Churn Strategist** is an intelligent web application engineered to predict customer retention probabilities. By leveraging historical demographic footprints and viewing behavior logs, the underlying classical Machine Learning architecture (**Decision Tree Classifier**) seamlessly identifies high-risk churn profiles in real-time.

This repository serves as the definitive source code for the Streamlit-based web platform as required by the **Milestone 1 Submission Criteria**.

---

## ⚡ Key Features & Capabilities

- 🔮 **Real-Time Predictive Inference:** A dynamic Streamlit UI accepting 12 distinct customer input vectors to compute real-time churn likelihood.
- 📊 **Robust Model Validation Dashboard:** Interactive tracking of continuous model deployment metrics (`Accuracy: ~97.9%`, `Precision: ~98.5%`).
- 📈 **Interactive Plotly Visualizations:** Engaging rendered confusion matrices to map predictive disparities visually with deep hover effects.
- 🎨 **Premium SaaS-Grade UI/UX:** Completely restyled utilizing advanced glassmorphism, smooth scrolling (`scroll-behavior: smooth`), dynamic micro-animations (slide-up fades, pulse glows), and fully highly interactive hover states across forms, buttons, inputs, dataframes, and metric cards.
- 🔒 **Stateless Architecture:** Highly scalable, session-independent stateless predictions perfectly integrated with Streamlit Cloud environments.

---

## 🛠️ Technology Stack (Architecture)

| Component | Technology Used | Description |
|-----------|-----------------|-------------|
| **Frontend UI** | Streamlit, CSS3, HTML5 | Web interface and responsive custom styling. |
| **Data Engine** | Pandas, Numpy | For structured encoding, dropping columns, and manipulation. |
| **Core ML Engine** | Scikit-Learn | Training the foundational `DecisionTreeClassifier`. |
| **Visualizer**  | Plotly Express | For rendering interactive data plots and matrices. |

---

## 🚀 Setup & Installation (Local Deployment)

To deploy the intelligence network locally onto your environment, follow the structured CLI workflow below:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/samay-hash/netflix-churn-streamlit.git
cd netflix-churn-streamlit
```

### 2️⃣ Initialize Virtual Environment (VENV)
Isolating dependencies ensures zero conflict with global Python packages. *(Recommended for macOS / Linux)*
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
Provisioning the exact architecture components defined in `requirements.txt`:
```bash
pip install -r requirements.txt
```
*(Optionally include `pip install watchdog` for enhanced local caching performance).*

### 4️⃣ Deploy Local Server
Boot up the Streamlit interface mapped to port 8501:
```bash
python3 -m streamlit run app.py
```
📍 **Dashboard Access:** `http://localhost:8501`

---

## ☁️ Streamlit Cloud Integration (Live Hosting)

This codebase is specifically tuned for optimal integration via **Streamlit Community Cloud**. To deploy:
1. Connect via [Streamlit Cloud Dashboard](https://share.streamlit.io/).
2. Mount the target repository `samay-hash/netflix-churn-streamlit`.
3. Set the **Main file path** index to `app.py`.
4. Boot deployment. Cloud compute will automatically resolve dependencies and fetch the `.csv` database to fire up the system.

---

## 📁 Repository Blueprint
```text
📦 netflix-churn-streamlit
 ┣ 📜 app.py                     # [FRONTEND] Streamlit Application & Routing logic
 ┣ 📜 model.py                   # [BACKEND] Intelligent Decision Tree mapping & validation
 ┣ 📜 netflix_customer_churn.csv # [DATA] Core structured dataset (5000 records)
 ┣ 📜 requirements.txt           # [DEVOPS] Python package manifests
 ┣ 📜 .gitignore                 # [GIT] Ignored caches & environments
 ┗ 📜 README.md                  # System Documentation 
```

<br>
<div align="center">
    <p><i>Developed dynamically aligned with End-Sem/Mid-Sem ML Lifecycle Protocols</i></p>
</div>
