''' Executing this function initiates the emotion detection
    application using flask
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_analyzer():
    '''This function runs analysis on the input at /emotionDetector
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    final_result = f"For the given statement, the system response is 'anger':{response['anger']}, \
    'disgust':{response['disgust']}, 'fear':{response['fear']}, \
    'joy':{response['joy']}, and 'sadness':{response['sadness']}. \
    The dominant emotion is {response['dominant_emotion']}"

    if not response['dominant_emotion']:
        return "Invalid text! Please try again!"

    return final_result


@app.route('/')
def render_home():
    '''This method runs the homepage template
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5000)
