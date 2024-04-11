#!/usr/bin/env python3
"""This is a module to implement a regex
    to replace occurrences of certain field values in user-data.
"""

import re


def filter_datum(fields: str, redaction: str, message: str, separator: str):
    """a function that returns the log message obfuscated
    """
    for val in fields:
        message = re.sub(val + '=.*?' + separator, val + '=' + redaction
                         + separator, message)
    return message
