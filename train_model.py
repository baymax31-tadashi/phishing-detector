from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from app.utils import extract_features_from_url
from sklearn.ensemble import RandomForestClassifier
import joblib


df = pd.read_csv("phishing_dataset.csv")


df["type"] = df["type"].map({"legit": 0, "phishing": 1})


X = df["url"].apply(extract_features_from_url).tolist()
y = df["type"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


joblib.dump(model, "app/model/phishing_model.pkl")
