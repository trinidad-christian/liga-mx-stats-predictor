# src/train_model.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

def load_training_data(path):
    return pd.read_csv(path)

def prepare_features_and_labels(df):
    # These are your input features (X) and target (y)
    X = df[["shots", "rating"]]        # You can add more features here
    y = df["scored"]                   # 1 = scored, 0 = did not score
    return X, y

def train_and_save_model(X, y, model_path="models/goal_predictor.pkl"):
    model = LogisticRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("Model Accuracy:", acc)
    print("Report:\n", classification_report(y_test, y_pred))

    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
