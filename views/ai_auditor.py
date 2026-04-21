import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from views.theme import inject_theme, page_header
from logic.ai_agent import get_groq_api_key
import json
from streamlit_local_storage import LocalStorage

inject_theme()
localS = LocalStorage()

page_header(
    "Netflix · AI Auditor", 
    "Chat with your Database", 
    "Ask natural language questions about your dataset. The Agent will analyze the schema and data to answer."
)

@st.cache_data
def load_data():
    return pd.read_csv("data/netflix_customer_churn.csv")

df = load_data()

# Top-of-page Actions
col_head, col_clear = st.columns([4, 1])
with col_clear:
    if st.button("🗑️ Clear Chat", use_container_width=True, type="secondary"):
        st.session_state.messages = []
        # Force set the local storage to empty
        localS.setItem("chat_auditor_history", "[]", key="manual_clear")
        st.session_state.messages_just_cleared = True
        st.rerun()

# Retrieve stored history
if st.session_state.get("messages_just_cleared", False):
    stored_history = "[]"
    st.session_state.messages_just_cleared = False
else:
    stored_history = localS.getItem("chat_auditor_history")

# Chat UI
if "messages" not in st.session_state:
    if stored_history and isinstance(stored_history, str) and stored_history != "[]":
        try:
            st.session_state.messages = json.loads(stored_history)
        except Exception:
            st.session_state.messages = []
    else:
        st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("E.g., What is the average watch hours of churned users compared to active ones?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    localS.setItem("chat_auditor_history", json.dumps(st.session_state.messages), key="set_user")
    with st.chat_message("user"):
        st.markdown(prompt)

    api_key = get_groq_api_key()
    if not api_key:
        with st.chat_message("assistant"):
            st.error("GROQ_API_KEY is missing. Please set it via environment variables or Streamlit secrets.")
    else:
        with st.chat_message("assistant"):
            with st.spinner("Analyzing data..."):
                # We will construct a prompt with data info instead of executing raw python for security
                data_info = f"Dataset Columns: {list(df.columns)}\n"
                data_info += f"Data Sample (first 3 rows):\n{df.head(3).to_csv(index=False)}\n"
                
                # We can also compute some basic fast stats
                try:
                    churn_rate = df['churned'].mean() * 100
                    avg_fee = df['monthly_fee'].mean()
                    data_info += f"Quick Stats -> Overall Churn Rate: {churn_rate:.1f}%, Avg Fee: ${avg_fee:.2f}"
                except Exception:
                    pass

                # Build conversation history from session state (excluding the current prompt)
                history_str = ""
                if len(st.session_state.messages) > 1:
                    history_str = "\nConversation History:\n"
                    # We slice [:-1] because the current prompt is already appended to the end of the array
                    for m in st.session_state.messages[:-1]:
                        role_name = "User" if m["role"] == "user" else "Agent"
                        history_str += f"{role_name}: {m['content']}\n"

                system_prompt = (
                    "You are a Data Analyst Agent for Netflix. You are answering queries about the 'netflix_customer_churn.csv' database. "
                    "I will provide you with the schema, a small sample of the data, some basic stats, and the recent conversation history so you remember context.\n\n"
                    "Data Context:\n{context}\n{history}"
                )
                
                chat_prompt = ChatPromptTemplate.from_messages([
                    ("system", system_prompt),
                    ("human", "{question}")
                ])
                
                llm = ChatGroq(temperature=0.4, model_name="llama-3.3-70b-versatile", api_key=api_key)
                chain = chat_prompt | llm
                
                response = chain.invoke({
                    "context": data_info,
                    "history": history_str,
                    "question": prompt
                })
                
                st.markdown(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})
                localS.setItem("chat_auditor_history", json.dumps(st.session_state.messages), key="set_assistant")
