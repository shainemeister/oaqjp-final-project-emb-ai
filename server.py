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

    # Blank Input Handling
    if not text_to_analyse or text_to_analyse.strip() == "":
        return "Invalid input! Try again."

    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid input! Try again."

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
