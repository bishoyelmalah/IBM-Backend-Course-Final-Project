import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_Obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = my_Obj, headers = headers)
    formatted_res = json.loads(response.text)

    
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

    emotions_dict = formatted_res["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    emotions_dict["dominant_emotion"] = dominant_emotion

    return emotions_dict