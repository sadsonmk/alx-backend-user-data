#!/usr/bin/env python3
"""This is a module containing the Auth class"""

from os import getenv
from flask import request
from typing import (
        List,
        TypeVar
        )


class Auth:
    """The class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """a method for paths that require authentication"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        for x in excluded_paths:
            if x[-1] == '*':
                result = x.split('*')
                if path.startswith(result[0]):
                    return False
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """a method for the authorization header"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """a method to check the current user"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if not request:
            return None
        _my_session_id = getenv('SESSION_NAME')
        return request.cookies.get(_my_session_id)
