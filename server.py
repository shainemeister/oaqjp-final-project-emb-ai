"""
Emotion Detection Flask Web Appllication
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze emotion from query parameter and return formatted response."""
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)
    output = f"""For the given statement, the emotion detection response is
        'anger': {response['anger']},
        'disgust': {response['disgust']},
        'fear': {response['fear']},
        'joy': {response['joy']},
        'sadness': {response['sadness']}.
        The dominant emotion is {response['dominant_emotion']}.
    """

    return output

@app.route("/")
def render_index_page():
    """Render main application page."""
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)