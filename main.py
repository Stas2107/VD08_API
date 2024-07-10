from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get_quote')
def get_quote():
  url = "https://api.quotable.io/random"
  response = requests.get(url)
  data = response.json()
  quote = data['content']
  return {'quote': quote}

if __name__ == '__main__':
  app.run(debug=True)