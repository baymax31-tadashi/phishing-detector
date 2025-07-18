from flask import Blueprint, render_template, request
from .ml_model import extract_features, predict_url
import os
import time
from werkzeug.utils import secure_filename

bp = Blueprint("main", __name__)

# In-memory log
url_log = []

@bp.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None
    if request.method == "POST":
        url = request.form.get("url")
        screenshot = request.files.get("screenshot")

        features = extract_features(url)
        prediction, raw_confidence = predict_url(features)  # raw_confidence: float (0-1)
        confidence_percent = round(raw_confidence * 100, 2)

        # Save screenshot if uploaded
        screenshot_filename = None
        if screenshot and screenshot.filename:
            filename = secure_filename(screenshot.filename)
            screenshot_filename = f"static/uploads/{int(time.time())}_{filename}"
            os.makedirs(os.path.dirname(screenshot_filename), exist_ok=True)
            screenshot.save(screenshot_filename)

        # Add to history
        url_log.insert(0, {
            "url": url,
            "prediction": prediction,
            "confidence": confidence_percent,
            "screenshot": screenshot_filename
        })

        # Limit log to latest 10 entries
        if len(url_log) > 10:
            url_log.pop()

        result = prediction
        confidence = confidence_percent

    return render_template("index.html", result=result, confidence=confidence, log=url_log)
