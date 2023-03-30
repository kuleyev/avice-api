import random

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/advice')
def get_random_string():
    with open('strings.txt', 'r') as file:
        strings = file.readlines()
    random_string = random.choice(strings)
    return jsonify({'advice': random_string.strip()})
