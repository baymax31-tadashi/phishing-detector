# app/utils.py

import re
import pytesseract
from PIL import Image
import cv2
import numpy as np

def extract_features_from_url(url):
    return [
        len(url),
        url.count('.'),
        url.count('/'),
        int(url.startswith("https")),
        int("@" in url),
        int("-" in url),
        int("login" in url.lower()),
        int("secure" in url.lower()),
        int("account" in url.lower()),
        int("update" in url.lower())
    ]

def extract_text_from_image(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Optional preprocessing
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    # OCR
    text = pytesseract.image_to_string(gray)
    return text

def extract_urls_from_text(text):
    url_pattern = r'(https?://[^\s]+)'
    urls = re.findall(url_pattern, text)
    return urls
