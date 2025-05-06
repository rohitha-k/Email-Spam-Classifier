
from flask import Flask, request, render_template
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')

app = Flask(__name__)
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text).lower()
    text = text.split()
    text = [ps.stem(word) for word in text if word not in stop_words]
    return ' '.join(text)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    msg = request.form['email']
    data = preprocess(msg)
    vect = vectorizer.transform([data])
    prediction = model.predict(vect)[0]
    result = "Spam ❌" if prediction == 1 else "Ham ✅"
    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == "__main__":
    app.run(debug=True)
