#!/usr/bin/env python3
"""module for a class SessionExpAuth that inherits from SessionAuth"""
from datetime import datetime, timedelta
import os
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """a class that adds an expiration date to a Session ID"""

    def __init__(self):
        """initializes instance attributes on object creation"""
        super().__init__()
        self.session_duration = int(os.environ.get("SESSION_DURATION", 0))

    def create_session(self, user_id=None):
        """overloads the create_session from the parent class"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
                        'user_id': user_id,
                        'created_at': datetime.now()
                }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """overloads the user_id_for_session_id from the parent class"""
        if not session_id:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id['user_id']
        session_dict = self.user_id_by_session_id[session_id]
        if not session_dict:
            return None
        if 'created_at' not in session_dict:
            return None
        now = datetime.now()
        created_at = session_dict.get('created_at')
        delta = timedelta(seconds=self.session_duration)
        now = now - delta
        if created_at + timedelta(seconds=self.session_duration) < now:
            return None
        return session_dict.get('user_id', None)
