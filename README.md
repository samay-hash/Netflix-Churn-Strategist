# Netflix Customer Churn Prediction - Streamlit App

This is a Streamlit Web Application that predicts Netflix Customer Churn using a Decision Tree model.

## Setup Instructions (A to Z)

**Step 1:** Download your Google Colab Code logic. (Completed, code adapted in `model.py`)

**Step 2:** Open the project in VS Code.

**Step 3:** Ensure the required structure is set up:
```text
netflix-churn-streamlit/
│
├── app.py                     # The Streamlit application
├── model.py                   # Machine Learning logic
├── requirements.txt           # Library dependencies
├── netflix_customer_churn.csv # The dataset 
└── README.md                  # This file
```

**Step 4:** Run it Locally (FOR MAC)
1. Open your VS Code Terminal.
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python3 -m streamlit run app.py
   ```
5. View the app at `http://localhost:8501`.

**Step 5:** Upload to GitHub
1. Create an account at `https://github.com/` if you haven't already.
2. Create a new repository named `netflix-churn-streamlit`.
3. Run the following commands in the VS Code terminal:
   ```bash
   git init
   git add .
   git commit -m "Initial Streamlit app for Netflix churn prediction"
   git branch -M main
   git remote add origin https://github.com/USERNAME/netflix-churn-streamlit.git
   git push -u origin main
   ```
*(Replace USERNAME with your actual GitHub username)*

**Step 6:** Deploy on Streamlit Cloud
1. Go to `https://streamlit.io/cloud`.
2. Login with your GitHub account.
3. Click on "New app".
4. Select the repository `netflix-churn-streamlit`, Branch `main`, and Main file path `app.py`.
5. Click **Deploy!** 🚀
