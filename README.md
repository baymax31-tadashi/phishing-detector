# 🛡️ Phishing URL & Screenshot Detector

A machine learning system that detects phishing URLs using 15 cybersecurity-informed features, with multi-model comparison and an interactive Streamlit interface.

## 📊 Model Performance

| Model | Accuracy | AUC-ROC |
|---|---|---|
| Logistic Regression | — | — |
| Random Forest | — | — |
| Gradient Boosting | — | — |

> Run `train_model.py` and fill in your actual numbers above.

## 🔍 Features Engineered (15)

| Feature | Cybersecurity Rationale |
|---|---|
| `url_length` | Phishing URLs tend to be longer to obscure domain |
| `num_dots` | Subdomain abuse increases dot count |
| `num_hyphens` | Hyphens used to mimic legit domains (e.g. `paypal-login.com`) |
| `num_at` | `@` redirects browser to text after it |
| `has_ip_in_domain` | Direct IP instead of domain = strong phishing signal |
| `has_suspicious_keywords` | login, verify, secure, confirm, etc. |
| `num_subdomains` | Multiple subdomains used to bury real domain |
| `has_https` | Phishing sites increasingly use HTTPS — not a safety guarantee |
| `domain_length` | Longer domains often disguise real identity |
| `num_query_params` | Many params = redirect/tracking abuse |
| `num_digits_in_url` | Digits used to imitate IPs or obfuscate |
| `has_port` | Non-standard port = suspicious server |
| `path_length` | Deep paths used to hide malicious endpoints |
| `num_special_chars` | `%`, `=`, `#` used for encoding attacks |
| `num_double_slash` | Double slashes used for URL redirection |

## 🚀 How to Run

```bash
pip install -r requirements.txt

# Train and compare models
python train_model.py

# Launch Streamlit app
streamlit run streamlit_app.py
```

## 📁 Project Structure
