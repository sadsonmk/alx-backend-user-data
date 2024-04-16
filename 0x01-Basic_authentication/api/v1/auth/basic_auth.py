#!/usr/bin/env python3
"""This is a module that contains the class BasicAuth"""


from api.v1.auth.auth import Auth
import base64


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
            return tuple(decoded_base64_authorization_header.split(':'))
