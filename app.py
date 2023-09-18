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

    # Define the headers to match the cURL request
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'ubid-main=132-5223720-0201760; i18n-prefs=USD; lc-main=en_US; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-ubid-main=351-8882824-5732501; regStatus=registered; session-id-apay=259-7339787-7938938; s_vnum=2119338178916%26vn%3D1; s_nr=1687338195171-New; s_dslv=1687338195173; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6ImRiYWRkNTY6V1FqV2M2SlhXbFVJeGVpa29hNk9KQVlFaHBZUk1acDF5VzE0N1RiVT0ifQ.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoicTh3Y2JVa2JxaCtcL1BOa1N5THRpM0N0TFBUUWp1XC9xRXJjTXZuMzlRRWVzPSIsImFybiI6ImFybjphd3M6aWFtOjo2NDQzNjI0NTI2MTc6cm9vdCIsInVzZXJuYW1lIjoibGFtcGEifQ.e7sYDw16L9ly3sMeTq_ZQVrU1xZgj0HqjFfDm4HiAq2qrVGWgYooHT9Ux_MFKw4QBX5Jpk_gC8DCSmd1Uk-nXQ',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'none',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    
    # Define the URL with the keyword parameter
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
    
# Make the request using the headers and parameters
    response = requests.get(url, headers=headers, params=params)

    alphabets_en = list("abcdefghijklmnopqrstuvwxyz")

    suggestions_list = []

    for letter in alphabets_en:
        params["prefix"] = letter + keyword + letter
        response = requests.get(url, params=params, headers=headers)
        suggestions = json.loads(response.text)["suggestions"]
        for suggestion in suggestions:
            value = suggestion["value"]
            suggestions_list.append(value)

    return jsonify(suggestions=suggestions_list)

if __name__ == '__main__':
    app.run(debug=True)

