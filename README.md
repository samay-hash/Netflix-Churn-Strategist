<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" alt="Netflix Logo" width="150"/>
  <br>
  <h1>🎬 Netflix Customer Churn Strategist</h1>
  <p><strong>An AI-Driven Customer Analytics System for Predictive Churn Analysis & Agentic Retention Strategy</strong></p>

  [![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
  [![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
  [![LangGraph](https://img.shields.io/badge/LangGraph-Agent_Framework-blueviolet.svg?style=for-the-badge)](https://github.com/langchain-ai/langgraph)
  [![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
  [![Deployment](https://img.shields.io/badge/Deployed-Streamlit_Cloud-success.svg?style=for-the-badge)](#-live-deployment)
</div>

<hr>

## 📌 Executive Overview

The **Netflix Customer Churn Strategist** is a two-milestone AI-driven customer analytics system:

- **Milestone 1 (Mid-Sem):** A classical Machine Learning pipeline built using Scikit-Learn that predicts customer churn risk from 12 behavioural and demographic input features — *without any LLMs*.
- **Milestone 2 (End-Sem):** An agentic AI extension powered by LangGraph that autonomously reasons about churn risk, retrieves retention best practices via RAG (Retrieval-Augmented Generation), and generates structured, actionable intervention strategies.

> This repository is the definitive source code for the end-to-end **ML + Agentic Retention Platform** as required by the **Course Project Submission Criteria**.

---

## 🧠 Business Context & Problem Understanding

### Why Does Churn Matter?
Customer churn — the rate at which subscribers cancel their service — is one of the most critical KPIs for subscription businesses like Netflix. Industry research shows that **acquiring a new customer costs 5–25× more** than retaining an existing one. Even a **1% reduction in churn** can translate into millions of dollars in retained revenue at scale.

### The Problem
Netflix experiences customer attrition driven by a complex mix of factors:
- **Behavioural signals:** Low watch time, infrequent logins, declining engagement scores
- **Demographic signals:** Age groups, subscription tiers, support interaction history
- **Financial signals:** Payment delays, downgrades, plan switches

Traditional rule-based systems fail to capture non-linear relationships between these variables. This project addresses that gap with a data-driven, ML-first approach, further augmented by an AI agent that reasons over the output and proposes targeted retention actions.

### Business Goal
> **"Predict which customers are at risk of churning and autonomously generate personalised retention strategies to reduce churn rate."**

---

## ⚡ Key Features & Capabilities

- 🔮 **Real-Time Predictive Inference:** Dynamic Streamlit UI accepting 12 customer input vectors to compute real-time churn probability.
- 📊 **Robust Model Validation Dashboard:** Interactive tracking of model accuracy (`~97.9%`), Precision (`~98.5%`), Recall, and F1-Score.
- 📈 **Interactive Plotly Visualizations:** Rendered confusion matrices and feature importance charts with deep hover effects.
- 🤖 **Agentic Retention Strategist (M2):** LangGraph-based AI agent that autonomously retrieves best practices and generates structured retention reports.
- 🗂️ **RAG-Powered Knowledge Retrieval (M2):** Chroma/FAISS vector store integration to fetch relevant retention playbooks at inference time.
- 🎨 **Premium SaaS-Grade UI/UX:** Glassmorphism, micro-animations, smooth scrolling, and interactive hover states.
- 🔒 **Stateless Architecture:** Scalable, session-independent design built for Streamlit Cloud.

---

## 🏗️ System Architecture

### Milestone 1 — ML Pipeline Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                        STREAMLIT FRONTEND                           │
│           (Input Form → 12 Feature Vectors Collected)               │
└───────────────────────────┬──────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────────────┐
│                      DATA PREPROCESSING LAYER                       │
│     (Label Encoding · Missing Value Handling · Feature Scaling)     │
└───────────────────────────┬──────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────────────┐
│                     ML ENGINE (model.py)                            │
│         Decision Tree Classifier (Scikit-Learn)                     │
│         Trained on: netflix_customer_churn.csv (5000 records)       │
└───────────────────────────┬──────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────────────┐
│                     PREDICTION OUTPUT LAYER                         │
│     Churn Risk Score · Confidence Probability · Visual Dashboard    │
└──────────────────────────────────────────────────────────────────────┘
```

### Milestone 2 — Agentic AI Architecture (LangGraph)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     LANGGRAPH AGENT WORKFLOW                        │
│                                                                     │
│   [START]                                                           │
│      │                                                              │
│      ▼                                                              │
│  ┌─────────────────────┐                                            │
│  │  Churn Risk Intake  │  ← ML Model Output (Risk Score + Features)│
│  └────────┬────────────┘                                            │
│           │                                                         │
│           ▼                                                         │
│  ┌─────────────────────┐   ┌──────────────────────────────────┐    │
│  │  RAG Retrieval Node │──▶│  Chroma/FAISS Vector Store       │    │
│  │  (Fetch Best        │   │  (Retention Playbooks, Case      │    │
│  │   Practices)        │   │   Studies, Intervention Docs)    │    │
│  └────────┬────────────┘   └──────────────────────────────────┘    │
│           │                                                         │
│           ▼                                                         │
│  ┌─────────────────────┐                                            │
│  │  Reasoning Node     │  ← LLM (Open-source / Free-tier API)     │
│  │  (Risk Analysis +   │                                            │
│  │   Strategy Planning)│                                            │
│  └────────┬────────────┘                                            │
│           │                                                         │
│           ▼                                                         │
│  ┌─────────────────────┐                                            │
│  │  Report Generation  │  → Structured Retention Report (PDF/UI)  │
│  └────────┬────────────┘                                            │
│           │                                                         │
│         [END]                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

| Component | Technology | Description |
|-----------|------------|-------------|
| **Frontend UI** | Streamlit, CSS3, HTML5 | Web interface and premium custom styling |
| **Data Engine** | Pandas, NumPy | Feature encoding, manipulation, and preprocessing |
| **Core ML Engine (M1)** | Scikit-Learn | `DecisionTreeClassifier` training & inference |
| **Agent Framework (M2)** | LangGraph | State machine-based agentic workflow |
| **Vector Store / RAG (M2)** | Chroma / FAISS | Retention knowledge retrieval |
| **LLMs (M2)** | Open-source / Free-tier APIs | Reasoning and report generation |
| **Visualizer** | Plotly Express | Interactive confusion matrices and charts |
| **Hosting** | Streamlit Cloud | Cloud deployment for mandatory live demo |

---

## 📊 Model Performance Evaluation (Milestone 1)

The `DecisionTreeClassifier` was trained and evaluated on the `netflix_customer_churn.csv` dataset (5000 records) using an 80/20 train-test split.

| Metric | Score |
|--------|-------|
| **Accuracy** | ~97.9% |
| **Precision** | ~98.5% |
| **Recall** | ~97.4% |
| **F1-Score** | ~97.9% |

### Key Observations
- The model performs strongly across both churned and non-churned classes with minimal false negatives.
- **Top predictive features** identified: `Engagement_Score`, `Watch_Hours_Per_Week`, `Support_Tickets_Per_Month`, `Subscription_Type`.
- Confusion matrix is rendered interactively within the application dashboard.

> Full evaluation breakdown is available within the app's **"Model Performance"** tab.

---

## 🚀 Setup & Installation (Local Deployment)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/samay-hash/netflix-churn-streamlit.git
cd netflix-churn-streamlit
```

### 2️⃣ Initialize Virtual Environment (VENV)
```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
python3 -m streamlit run app.py
```
📍 **Dashboard Access:** `http://localhost:8501`

---

## ☁️ Live Deployment

This application is **publicly hosted** on Streamlit Community Cloud as per the mandatory submission requirement.

🔗 **Live App:** *(Add your Streamlit Cloud deployment link here)*

To deploy your own instance:
1. Connect via [Streamlit Cloud Dashboard](https://share.streamlit.io/).
2. Mount the repository `samay-hash/netflix-churn-streamlit`.
3. Set **Main file path** to `app.py`.
4. Click Deploy — dependencies are auto-resolved from `requirements.txt`.

---

## 📁 Repository Structure

```text
📦 netflix-churn-strategist
 ┣ 📜 app.py                     # [FRONTEND] Streamlit Application & Routing logic
 ┣ 📜 model.py                   # [BACKEND] Decision Tree ML engine & validation
 ┣ 📜 netflix_customer_churn.csv # [DATA] Core structured dataset (5000 records)
 ┣ 📜 requirements.txt           # [DEVOPS] Python package manifests
 ┣ 📂 pages/                     # [PAGES] Multi-page Streamlit routing modules
 ┃  ┗ 📜 theme.py                # [UI] Theme constants and CSS injection
 ┣ 📜 .gitignore                 # [GIT] Ignored caches & environments
 ┗ 📜 README.md                  # System Documentation
```

---

## 🗂️ Agent Workflow Documentation (Milestone 2)

### LangGraph States & Nodes

| Node | Type | Description |
|------|------|-------------|
| `CustomerIntakeNode` | Entry | Receives ML churn score + 12 feature vectors as agent state |
| `RiskClassificationNode` | Process | Categorises customer into Low / Medium / High churn risk tier |
| `RAGRetrievalNode` | Tool | Queries Chroma/FAISS vector store for relevant retention strategies |
| `ReasoningNode` | LLM | Analyses risk tier + retrieved docs to draft personalised strategy |
| `ReportGenerationNode` | Output | Formats structured retention report with actionable recommendations |

### State Schema
```python
class AgentState(TypedDict):
    customer_features: dict        # 12 input features from ML model
    churn_score: float             # Predicted churn probability
    risk_tier: str                 # "Low" | "Medium" | "High"
    retrieved_docs: list[str]      # RAG-fetched retention documents
    reasoning: str                 # LLM-generated analysis
    retention_report: str          # Final structured output
```

---

## 📋 Evaluation Criteria

| Phase | Weight | Assessment Areas |
|-------|--------|-----------------|
| **Milestone 1 (Mid-Sem)** | 25% | ML technique application, Feature Engineering quality, UI Usability, Evaluation Metrics (Accuracy, F1, Precision, Recall) |
| **Milestone 2 (End-Sem)** | 30% | Reasoning quality, RAG & State management implementation, Output clarity, Deployment success |

> ⚠️ **Important:** Localhost-only demonstrations are **not accepted** for final submission. The application must be publicly hosted.

---

## 🎥 Demo Video

📹 **Demo Video (Max 5 mins):** *(Add your demo video link here — YouTube / Drive)*

The demo covers:
- Live walkthrough of the churn prediction UI
- Model performance metrics dashboard
- Agentic retention strategy generation (Milestone 2)
- RAG retrieval in action

---

## 👥 Team

| Name | Role |
|------|------|
| Samay Samrat | ML Engineer & Full-Stack Dev |
| *(Team Member 2)* | *(Role)* |
| *(Team Member 3)* | *(Role)* |
| *(Team Member 4)* | *(Role)* |

---

<br>
<div align="center">
    <p><i>Developed as part of the AI-Driven Customer Analytics Course Project · Milestone 1 (Classical ML) + Milestone 2 (Agentic AI)</i></p>
</div>
