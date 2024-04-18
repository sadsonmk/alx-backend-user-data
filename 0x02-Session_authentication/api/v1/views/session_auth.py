#!/usr/bin/env python3
""" Module for a new Flask view that handles all
    routes for the Session authentication
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv
from typing import Tuple
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> Tuple[str, int]:
    """ POST /api/v1/auth_session/login
    Return:
      the dictionary representation of the User
    """
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            return jsonify({"error": "email missing"}), 400
        password = request.form.get('password')
        if not password:
            return jsonify({"error": "password missing"}), 400
        user = User.search({"email": email})
        if not user:
            return jsonify({"error": "no user found for this email"}), 404
        if not user[0].is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        session_id = auth.create_session(getattr(user[0], 'id'))
        resp = jsonify(user[0].to_json())
        resp.set_cookie(getenv('SESSION_NAME'), session_id)
        return resp


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def auth_session_logout():
    """DELETE /api/v1/auth_session/logout
        Return:
        an empty JSON dictionary with the status code 200
    """
    destroyed = auth.destroy_session(request)
    if not destroyed:
        abort(404)
    return jsonify({}), 200
