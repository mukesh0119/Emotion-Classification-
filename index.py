import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from nltk.tokenize import word_tokenize
import joblib
import pandas as pd
from datetime import datetime

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


model = joblib.load('final_model.joblib')
vectorizer = joblib.load('final_vectorizer.joblib')


nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


emotions = [
    'admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity',
    'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear',
    'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief',
    'remorse', 'sadness', 'surprise', 'neutral'
]

emotion_df = pd.DataFrame({'emotion': emotions})

audit_data = []

def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub('[^A-Za-z0-9 ]+', '', text)
    text = text.lower()
    text = re.sub('\d+', '', text)
    text = word_tokenize(text)
    text = [word for word in text if word not in stop_words]
    text = [stemmer.stem(word) for word in text]
    text = ' '.join(text)
    return text

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()
        text = data.get('text')
    else:
        text = request.form.get('text')

    if text is None:
        return jsonify({'error': 'Invalid input'})


    text = preprocess_text(text)

    text_vectorized = vectorizer.transform([text])

    predicted_class = model.predict(text_vectorized)[0]

    emotion = get_emotion(predicted_class)

    now = datetime.now()
    audit_data.append({'input': request.form.get('text'), 'class': predicted_class, 'emotion': emotion, 'date': now.date(), 'time': now.time()})

    results = {
        'input_text': request.form.get('text'),
        'predicted_class': predicted_class,
        'emotion': emotion
    }

    return render_template('results.html', input_text=request.form.get('text'), predicted_class=predicted_class, emotion=emotion)

@app.route('/audit')
def audit():
    return render_template('audit.html', audit_data=audit_data)

def get_emotion(predicted_class):
    if predicted_class < 0 or predicted_class >= len(emotions):
        return 'Unknown'
    return emotion_df.loc[predicted_class, 'emotion']

if __name__ == '__main__':
    app.run(debug=True)
