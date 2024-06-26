#!/usr/bin/env python3
"""This is a module that contains the class BasicAuth"""

from models.user import User
from api.v1.auth.auth import Auth
import base64
from typing import (
        TypeVar,
        )


class BasicAuth(Auth):
    """inherits from the Auth class"""
    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """returns the Base64 part of the Authorization
            header for a Basic Authentication
        """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string
            base64_authorization_header
        """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except (TypeError, base64.binascii.Error):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """returns the user email and password from
            the Base64 decoded value
        """
        if not decoded_base64_authorization_header:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        else:
            return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            match = User.search({'email': user_email})
        except Exception:
            return None

        for user in match:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        auth_header = self.authorization_header(request)

        if not auth_header:
            return None
        encode_header = self.extract_base64_authorization_header(auth_header)

        if not encode_header:
            return None

        decode = self.decode_base64_authorization_header(encode_header)
        if not decode:
            return None

        email, password = self.extract_user_credentials(decode)
        if not email or not password:
            return None

        user = self.user_object_from_credentials(email, password)
        return user
