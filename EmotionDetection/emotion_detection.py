
import requests   # library for HTTP requests
import json       # JSON parsing

def emotion_detector(text_to_analyse):
    """ Detect Emotion using the Emotion Predict Function of the Watson NLP Library
    """ 

    # Watson NLP function inputs
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send POST request
    response = requests.post(url, json=myobj, headers=header)

    # Parse the JSON response
    formatted_response = json.loads(response.text)

    # Extract Emotion Scores
    scores = {}
    if response.status_code == 200:
        scores['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
        scores['disgust'] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        scores['fear'] = formatted_response['emotionPredictions'][0]['emotion']['fear']
        scores['joy'] = formatted_response['emotionPredictions'][0]['emotion']['joy']
        scores['sadness'] = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        # Determine dominant emotion
        dominant = max(scores, key=scores.get)
        scores['dominant_emotion'] = dominant

    elif response.status_code == 400:
        scores['anger'] = None
        scores['disgust'] = None
        scores['fear'] = None
        scores['joy'] = None
        scores['sadness'] = None
        scores['dominant_emotion'] = None

    else:
        scores = None

    return(scores)

