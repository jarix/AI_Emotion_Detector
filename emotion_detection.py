
import requests   # library for HTTP requests

def emotion_detector(text_to_analyse):
    """ Detect Emotion using the Emotion Predict Function of the Watson NLP Library
    """ 

    # Watson NLP function inputs
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send POST request
    response = requests.post(url, json=myobj, headers=header)

    # Return response text
    return response.text 
    