import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, classification_report,
    roc_auc_score, ConfusionMatrixDisplay
)

df = pd.read_csv("phishing_dataset.csv")
print(f"Dataset: {df.shape[0]} rows")
print(df['phishing'].value_counts())

X = df.drop(columns=['phishing'])
y = df['phishing']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
    "Gradient Boosting":   GradientBoostingClassifier(n_estimators=100, random_state=42),
}

results = {}
print("\n" + "="*60)
print(f"{'Model':<25} {'Accuracy':>10} {'AUC-ROC':>10}")
print("="*60)

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)
    results[name] = {"model": model, "accuracy": acc, "auc": auc}
    print(f"{name:<25} {acc:>10.4f} {auc:>10.4f}")

print("="*60)

best_name = max(results, key=lambda x: results[x]["auc"])
best_model = results[best_name]["model"]
y_pred_best = best_model.predict(X_test)

print(f"\nBest Model: {best_name}\n")
print(classification_report(y_test, y_pred_best, target_names=["Legit", "Phishing"]))

joblib.dump(best_model, "app/model/phishing_model.pkl")
print("Model saved")

rf_model = results["Random Forest"]["model"]
importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1][:15]
feat_names = X.columns

plt.figure(figsize=(12, 6))
plt.title("Top 15 Feature Importances — Random Forest")
plt.bar(range(15), importances[indices])
plt.xticks(range(15), [feat_names[i] for i in indices], rotation=45, ha='right')
plt.tight_layout()
plt.savefig("feature_importance.png", dpi=150)
plt.close()

fig, ax = plt.subplots(figsize=(5, 4))
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred_best,
    display_labels=["Legit", "Phishing"],
    ax=ax, colorbar=False
)
plt.title(f"Confusion Matrix — {best_name}")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150)
plt.close()

names = list(results.keys())
accs = [results[n]["accuracy"] for n in names]
aucs = [results[n]["auc"] for n in names]
x = np.arange(len(names))
width = 0.35
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width/2, accs, width, label='Accuracy')
ax.bar(x + width/2, aucs, width, label='AUC-ROC')
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.set_ylim(0.8, 1.0)
ax.set_title("Model Comparison")
ax.legend()
plt.tight_layout()
plt.savefig("model_comparison.png", dpi=150)
plt.close()
print("All plots saved!")
