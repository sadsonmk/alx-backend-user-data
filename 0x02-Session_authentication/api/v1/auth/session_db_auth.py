#!/usr/bin/env python3
"""This is a module for a class SessionDBAuth that inherits
    from SessionExpAuth and stores sessions in a database
"""
from datetime import datetime, timedelta
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """inherits from SessionExpAuth and stores sessions in a database"""

    def create_session(self, user_id=None):
        """creates and stores new instance of UserSession
            and returns the Session ID
        """
        session_id = super().create_session(user_id)
        if isinstance(session_id, str):
            session_kwargs = {
                    'user_id': user_id,
                    'session_id': session_id,
                    }
            user_sess = UserSession(**session_kwargs)
            user_sess.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """returns the User ID by requesting UserSession
            in the database based on session_id
        """
        try:
            session = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if len(session) <= 0:
            return None
        now = datetime.now()
        delta = timedelta(seconds=self.session_duration)
        if session[0].created_at + delta < now:
            return None
        return session[0].user_id

    def destroy_session(self, request=None) -> bool:
        """destroys the UserSession based on the
            Session ID from the request cookie
        """
        session_id = self.session_cookie(request)
        try:
            session = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if len(session) <= 0:
            return False
        session[0].remove()
        return True
