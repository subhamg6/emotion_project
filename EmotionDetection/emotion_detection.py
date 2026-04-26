def emotion_detector(text_to_analyse):

    if text_to_analyse.strip() == "":
        return {"error": "Invalid input"}

    return {
        "anger": 0.01,
        "disgust": 0.02,
        "fear": 0.03,
        "joy": 0.90,
        "sadness": 0.04,
        "dominant_emotion": "joy"
    }