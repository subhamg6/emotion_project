from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        return "Invalid input! Please try again."

    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid input! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

app.run(host="0.0.0.0", port=5000)