import requests
import json

def emotion_detector (text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers = headers)

    response_json = json.loads(response.text)
    pick_emotion = response_json['emotionPredictions'][0]['emotion']
    anger_score = pick_emotion['anger']
    disgust_score = pick_emotion['disgust']
    fear_score = pick_emotion['fear']
    joy_score = pick_emotion['joy']
    sadness_score = pick_emotion['sadness']
    dominant_emotion = ''
    counter = 0

    for emotion,emotion_value in enumerate(pick_emotion):
        if float(emotion_value) > counter:
            counter = float(emotion_value)
            dominant_emotion = emotion


    return response.text

