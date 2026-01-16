from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    response_str = ''
    for key,value in response.items():
        response_str += f"{key}:{value}" 

    final_result = f"For the given statement, the system response is {response_str}"