"""
Emotion detection function using Watson NLP Library

URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }

"""
import requests

WATSON_NLP_EMOTION_PREDICT_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
WATSON_NLP_EMOTION_PREDICT_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detection(text_to_analyze = "This is a very nice default value"):

    emotion = None
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.get(WATSON_NLP_EMOTION_PREDICT_URL, headers= WATSON_NLP_EMOTION_PREDICT_HEADERS, params = input_json)
    
    emotion = response["text"]

    return emotion

