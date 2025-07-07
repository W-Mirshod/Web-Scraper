from flask import Flask, request, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    if not url or not url.startswith(('http://', 'https://')):
        return jsonify({'error': 'Invalid URL'}), 400
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        return jsonify({'text': text[:2000]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
