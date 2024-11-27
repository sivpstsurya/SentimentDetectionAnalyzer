from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    analysis = TextBlob(text)
    sentiment = analysis.sentiment
    return jsonify({
        'sentiment': 'Positive' if sentiment.polarity > 0 else 'Negative' if sentiment.polarity < 0 else 'Neutral',
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    })

if __name__ == '__main__':
    app.run(debug=True)