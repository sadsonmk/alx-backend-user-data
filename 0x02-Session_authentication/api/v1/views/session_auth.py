#!/usr/bin/env python3
""" Module for a new Flask view that handles all
    routes for the Session authentication
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models.user import User
from os import getenv
from typing import Tuple


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> Tuple[str, int]:
    """ POST /api/v1/auth_session/login
    Return:
      the dictionary representation of the User
    """
    email = request.form.get('email')
    if not email:
        return json({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return json({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return json({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(password):
        return json({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(getattr(user[0], 'id'))
    resp = jsonify(user[0].to_json())
    resp.set_cookie(getenv('SESSION_NAME'), session_id)
    return resp
