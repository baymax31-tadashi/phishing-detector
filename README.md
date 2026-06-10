# 🛡️ Phishing URL Detector

A machine learning system that detects phishing URLs using cybersecurity-informed features, with multi-model comparison and an interactive Streamlit interface.

Trained on **58,645 real-world URLs** from the GregaVrbancic Phishing Dataset.

## 📊 Model Performance

| Model | Accuracy | AUC-ROC |
|---|---|---|
| Logistic Regression | 86.80% | 0.9408 |
| **Random Forest** | **95.59%** | **0.9911** |
| Gradient Boosting | 93.14% | 0.9806 |

Best Model: **Random Forest** — Precision: 96%, Recall: 96%, F1: 96%

## 🔍 Top Features by Importance

`directory_length`, `time_domain_activation`, `length_url`, `qty_slash_directory`, `ttl_hostname`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python train_model.py
streamlit run streamlit_app.py
```

## 📁 Project Structure
cd ~/phishing-detector
cat > README.md << 'EOF'
# 🛡️ Phishing URL Detector

A machine learning system that detects phishing URLs using cybersecurity-informed features, with multi-model comparison and an interactive Streamlit interface.

Trained on **58,645 real-world URLs** from the GregaVrbancic Phishing Dataset.

## 📊 Model Performance

| Model | Accuracy | AUC-ROC |
|---|---|---|
| Logistic Regression | 86.80% | 0.9408 |
| **Random Forest** | **95.59%** | **0.9911** |
| Gradient Boosting | 93.14% | 0.9806 |

Best Model: **Random Forest** — Precision: 96%, Recall: 96%, F1: 96%

## 🔍 Top Features by Importance

`directory_length`, `time_domain_activation`, `length_url`, `qty_slash_directory`, `ttl_hostname`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python train_model.py
streamlit run streamlit_app.py
```

## 📁 Project Structure
## 🛠️ Tech Stack
Python · Scikit-learn · Streamlit · Flask · Pandas · Matplotlib
