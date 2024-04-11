#!/usr/bin/env python3
"""Implement a hash_password function that expects one string argument
    name password and returns a salted, hashed password,
    which is a byte string.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a given password using bycrypt with a random salt"""

    salt = bcrypt.gensalt()
    hashed_pswd = bcrypt.hashpw(password.encode(), salt)
    return hashed_pswd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """uses bcrypt to check if a password matches the hashed password given"""
    return bcrypt.checkpw(password.encode(), hashed_password)
