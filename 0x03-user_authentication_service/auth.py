#!/usr/bin/env python3
"""a module that define a _hash_password method that takes
    in a password string arguments and returns bytes
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """a function that define a method that
        takes a string and return bytes
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
