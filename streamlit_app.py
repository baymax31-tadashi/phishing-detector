# streamlit_app.py

import streamlit as st
from app.ml_model import process_url_or_screenshot
from PIL import Image

st.set_page_config(page_title="Phishing Detector", layout="centered")
st.title("🔍 Phishing URL or Screenshot Analyzer")

url_input = st.text_input("Paste a URL (optional):")
screenshot_file = st.file_uploader("Upload Screenshot (optional)", type=["png", "jpg", "jpeg"])

if st.button("Analyze"):
    if not url_input and not screenshot_file:
        st.warning("Please provide a URL or upload a screenshot.")
    else:
        with st.spinner("Analyzing..."):
            try:
                prediction, confidence = process_url_or_screenshot(url_input, screenshot_file)
                st.success(f"🧠 Prediction: **{prediction.upper()}** ({round(confidence * 100, 2)}% confidence)")

                if screenshot_file:
                    st.image(Image.open(screenshot_file), caption="Uploaded Screenshot", use_column_width=True)

            except Exception as e:
                st.error(f"Error: {e}")
