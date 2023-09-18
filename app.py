# app.py
import subprocess
import uuid
from flask import Flask, request, jsonify, send_file
import requests
from werkzeug.utils import secure_filename
import os


def create_app():
    app = Flask(__name__, static_folder='uploads', static_url_path='/uploads')
    app.config['UPLOAD_FOLDER'] = '/app/uploads/'
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    # Other setup code...
    return app


app = create_app()


@app.route('/', methods=['GET'])
def homepage():
    return "Homepage"


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello"

import requests
import json
import csv

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    keyword = request.json['keyword']
    
    session_id = '133-2190809-5709766'
    customer_id = 'A1CNYR04B8CZOZ'
    request_id = 'NTH41W0H5GYC8N00NVCS'
    page_type = 'Gateway'
    lop = 'en_US'
    site_variant = 'desktop'
    client_info = 'amazon-search-ui'
    mid = 'ATVPDKIKX0DER'
    alias = 'aps'
    b2b = 0
    fresh = 0
    ks = 69
    event = 'onKeyPress'
    limit = 11
    fb = 1
    suggestion_type = 'KEYWORD'
    _ = 1551464006702

    url = 'https://completion.amazon.com/api/2017/suggestions'

    # The parameters for the request
    params = {
        'session-id': session_id,
        'customer-id': customer_id,
        'request-id': request_id,
        'page-type': page_type,
        'lop': lop,
        'site-variant': site_variant,
        'client-info': client_info,
        'mid': mid,
        'alias': alias,
        'b2b': b2b,
        'fresh': fresh,
        'ks': ks,
        'event': event,
        'limit': limit,
        'fb': fb,
        'suggestion-type': suggestion_type,
        '_': _
    }

    alphabets_en = list("abcdefghijklmnopqrstuvwxyz")

    suggestions_list = []

    for letter in alphabets_en:
        params["prefix"] = letter + keyword + letter
        response = requests.get(url, params=params)
        suggestions = json.loads(response.text)["suggestions"]
        for suggestion in suggestions:
            value = suggestion["value"]
            suggestions_list.append(value)

    return jsonify(suggestions=suggestions_list)

if __name__ == '__main__':
    app.run(debug=True)
