# app/ml_model.py

import joblib
import numpy as np
from app.utils import (
    extract_features_from_url,
    extract_text_from_image,
    extract_urls_from_text
)

model = joblib.load("app/model/phishing_model.pkl")

def predict_url(features):
    prediction = model.predict([features])[0]
    confidence = model.predict_proba([features])[0].max()
    return "PHISHING" if prediction == 1 else "LEGIT", confidence

def process_url_or_screenshot(url=None, screenshot_path=None):
    if url:
        features = extract_features_from_url(url)
        return predict_url(features)
    elif screenshot_path:
        text = extract_text_from_image(screenshot_path)
        urls = extract_urls_from_text(text)
        if urls:
            features = extract_features_from_url(urls[0])
            return predict_url(features)
        else:
            return "No URL Found", 0.0
