"""
   Emotion Detector Web App using Watson Libraries
"""
# Imports
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """ Retrieve text input from HTML page and run emotion detection function.
        Return emotion scores.
    """

    # Retrieve text
    text_to_analyze = request.args.get('textToAnalyze')

    # Run emotion detection
    emotions = emotion_detector(text_to_analyze)

    if emotions is None:
        return "Invalid text! Please try again!"
    elif emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    resp_str = f"For the given statement, the system response is " \
            f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, " \
            f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. " \
            f"The dominant emotion is {emotions['dominant_emotion']}."

    return resp_str

@app.route("/")
def render_index_page():
    """ Render main Web app page 
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run Web App
    app.run(host="0.0.0.0", port=5000)
