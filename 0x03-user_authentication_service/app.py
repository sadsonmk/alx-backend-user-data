#!/usr/bin/env python3
"""module that creates a basic flask app"""
from auth import Auth
from flask import (
        Flask,
        jsonify,
        request,
        make_response,
        abort,
        redirect,
        url_for
        )

app = Flask(__name__)
AUTH = Auth()


@app.route('/users', methods=['POST'])
def users():
    """end-point to register a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """create a new session for the user,
        store it the session ID as a cookie
    """
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    valid_logn = AUTH.valid_login(email, password)
    if valid_logn:
        res = make_response(jsonify({"email": email, "message": "logged in"}))
        res.set_cookie('session_id', valid_logn)
        return res
    abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """logouts the user and destroys the session"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        authy.destroy_session(user.id)
        return redirect(url_for('index'))
    else:
        abort(403)


@app.route('/', methods=['GET'])
def index():
    """defines the home route"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
