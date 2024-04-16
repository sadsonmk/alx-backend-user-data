#!/usr/bin/env python3
"""This is a module containing the Auth class"""


from flask import request
from typing import (
        List,
        TypeVar
        )


class Auth:
    """The class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """a method for paths that require authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """a method for the authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """a method to check the current user"""
        return None
