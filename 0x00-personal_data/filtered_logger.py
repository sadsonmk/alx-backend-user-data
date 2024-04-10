#!/usr/bin/env python3
"""This is a module to implement a regex
    to replace occurrences of certain field values in user-data.
"""

import re


def filter_datum(fields: str, redaction: str, message: str, separator: str):
    """a function that returns the log message obfuscated

        Args:
            fields(str): a list of strings representing all
            fields to obfuscate

            redaction(str): a string representing by what the
            field will be obfuscated

            message(str): a string representing the log line

            separator(str): a string representing by which character
            is separating all fields in the log line (message)

        Return:
            returns the log message obfuscated
    """
    for val in fields:
        message = re.sub(val + '=.*?' + separator, val + '=' + redaction
                         + separator, message)
    return message
