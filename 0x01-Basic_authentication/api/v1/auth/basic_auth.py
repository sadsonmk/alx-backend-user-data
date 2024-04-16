#!/usr/bin/env python3
"""This is a module that contains the class BasicAuth"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """inherits from the Auth class"""
    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """def extract_base64_authorization_header(self,
        authorization_header: str) -> str:
        """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.split(' ')[1]
