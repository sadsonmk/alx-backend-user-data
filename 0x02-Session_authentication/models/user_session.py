#!/usr/bin/env python3
"""module for the usersession model that inherits from the base model"""


from models.base import Base


class UserSession(Base):
    """a class for the user session"""
    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a User instance
        """
        super().__init__(*args, **kwargs)
        self.user_id: str = kwargs.get('user_id')
        self.session_id: str = kwargs.get('session_id')
