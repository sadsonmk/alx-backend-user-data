#!/usr/bin/env python3
"""module that creates a basic flask app"""
from auth import Auth
from flask import Flask, jsonify, request

app = Flask(__name__)
auth = Auth()


@app.route('/', methods=['GET'])
def index():
    """defines the home route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """end-point to register a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = auth.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
