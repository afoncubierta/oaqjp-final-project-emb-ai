"""
Flask application
"""

from EmotionDetection import emotion_detector
from flask import Flask, request
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion():
    text_to_analyze = request.args.get("statement")
    emotions = emotion_detector(text_to_analyze)

    dominant_emotion = emotions.pop("dominant_emotion")

    response_content = f"For the given statement, the system response is {emotions}. The dominant emotion is <b>{dominant_emotion}</b>."

    return()
