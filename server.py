"""
Flask application
"""

from EmotionDetection import emotion_detector
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion():
    request_data = json.loads(request.data)
    text_to_analyze = request_data["statement"]
    emotions = emotion_detector(text_to_analyze)

    dominant_emotion = emotions.pop("dominant_emotion")

    response_content = f"For the given statement, the system response is {emotions}. The dominant emotion is <b>{dominant_emotion}</b>."
    
    return(response_content)
