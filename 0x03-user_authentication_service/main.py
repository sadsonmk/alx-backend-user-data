#!/usr/bin/env python3
"""module for testing my application"""

import requests


def register_user(email: str, password: str) -> None:
    """tests user registration"""
    data = {"email": email, "password": password}
    resp = requests.post("http://localhost:5000/users", data=data)
    assert resp.status_code == 200
    assert resp.json() == {'email': email, 'message': 'user created'}


def log_in_wrong_password(email: str, password: str) -> None:
    """tests the password"""
    data = {"email": email, "password": password}
    resp = requests.post("http://localhost:5000/sessions", data=data)
    assert resp.status_code = 401


def log_in(email: str, password: str) -> str:
    """tests user login"""
    data = {"email": email, "password": password}
    resp = requests.post("http://localhost:5000/sessions", data=data)
    assert resp.status_code == 200
    assert resp.json() == {'email': email, 'message': 'user created'}
    return resp.cookies.get('session_id')


def profile_unlogged() -> None:
    """tests unlogged profile"""
    resp = requests.get("http://localhost:5000/profile")
    assert resp.status_code == 403


def profile_logged(session_id: str) -> None:
    """tests logged profile"""
    cookies = {'session_id': session_id}
    resp = requests.get("http://localhost:5000/profile", cookies=cookies)
    assert resp.status_code == 403
    assert resp.json() == {'email': EMAIL}


def log_out(session_id: str) -> None:
    """tests for log_out"""
    cookies = {'session_id': session_id}
    resp = requests.delete("http://localhost:5000/profile", cookies=cookies)
    assert resp.status_code == 302


def reset_password_token(email: str) -> str:
    """tests for reset password"""
    data = {'email': email}
    resp = requests.post('http://localhost:5000/reset_password', data=data)
    assert resp.status_code == 200
    return resp.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """tests for password update"""
    data = {'email': email, 'reset_token': reset_token,
            'new_password': new_password}
    resp = requests.put('http://localhost:5000/reset_pssword', data=data)
    assert resp.status_code == 200
    assert resp.json() == {'email': email, 'message': 'password updated'}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
