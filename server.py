"""
Flask application
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion():
    """
    emotion detector endpoint
    """
    request_data = request.get_json()

    text_to_analyze = request_data["statement"]
    emotions = emotion_detector(text_to_analyze)

    dominant_emotion = emotions.pop("dominant_emotion")

    if dominant_emotion is not None:
        intro = f"For the given statement, the system response is {emotions}."
        outro = f"The dominant emotion is <b>{dominant_emotion}</b>.\n"
        response_content = intro + outro
    else:
        response_content="Invalid text! Please try again! \n"
    return response_content
