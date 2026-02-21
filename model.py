import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_model():
    # Load the valid csv file
    df = pd.read_csv("netflix_customer_churn.csv")

    # Drop unnecessary columns
    if 'customer_id' in df.columns:
        df = df.drop('customer_id', axis=1)

    X = df.drop("churned", axis=1)
    y = df["churned"]

    # One hot encode categorical features using get_dummies
    X = pd.get_dummies(X, drop_first=True)

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train Tuned Decision Tree
    model = DecisionTreeClassifier(
        max_depth=10, 
        min_samples_leaf=2, 
        min_samples_split=10, 
        random_state=42
    )
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate metrics
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred)
    }

    return model, metrics
