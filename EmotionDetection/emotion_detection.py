import requests
import json

def emotion_detector(text_to_analyse):
    """Emotion detection using Watson NLP Library for EmotionPredict service"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {
        "raw_document": { "text": text_to_analyse }
    }

    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
 
    anger_score = emotions.get('anger')
    disgust_score = emotions.get('disgust')
    fear_score = emotions.get('fear')
    joy_score = emotions.get('joy')
    sadness_score = emotions.get('sadness')
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }