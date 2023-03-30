import random

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/advice')
def get_random_string():
    with open('strings.txt', 'r') as file:
        strings = file.readlines()
    random_string = random.choice(strings)
    return jsonify({'advice': random_string.strip()})


if __name__ == "__main__":
    app.run()
