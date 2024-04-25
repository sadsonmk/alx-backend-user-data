#!/usr/bin/env python3
"""creates a flask app"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', strictslashes=False, methods=['GET'])
def index():
    """defines the home route"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
