"""
Emotion detection function using Watson NLP Library

URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }

"""
import requests
import json

WATSON_NLP_EMOTION_PREDICT_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
WATSON_NLP_EMOTION_PREDICT_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze = "This is a very nice default value"):

    emotion = None
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(WATSON_NLP_EMOTION_PREDICT_URL, headers= WATSON_NLP_EMOTION_PREDICT_HEADERS, json = input_json)

    response_dict = json.loads(response.text)
    predictions = response_dict.get("emotionPredictions")[0]
    emotions = predictions.get("emotion")

    dominant_emotion = [emotion_name for emotion_name, emotion_score in emotions.items() if emotion_score == max(emotions.values())][0]
    emotions["dominant_emotion"] = dominant_emotion

    return emotions

