from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect():
    text = request.args.get('textToAnalyze')

    if not text:
        return "Invalid input! Please try again."

    try:
        result = emotion_detector(text)

        if "error" in result:
            return "Invalid input! Please try again."

        return f"Dominant emotion: {result['dominant_emotion']}"

    except Exception as e:
        return f"Error occurred: {str(e)}"

app.run()