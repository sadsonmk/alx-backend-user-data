#!/usr/bin/env python3
"""a module that define a _hash_password method that takes
    in a password string arguments and returns bytes
"""
from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """a function that define a method that
        takes a string and return bytes
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """adds a user into the db if not already exists"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """checks whether the user exists or not"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                pswd = user.hashed_password
                return bcrypt.checkpw(password.encode('utf-8'), pswd)
            else:
                return False
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """generates a uuid"""
        import uuid
        return str(uuid.uuid4())
