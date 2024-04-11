#!/usr/bin/env python3
"""This is a module to implement a regex
    to replace occurrences of certain field values in user-data.
"""

import re
from typing import List

import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes the objects of this class"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Implement the format method to filter values
            in incoming log records using filter_datum
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """a function that returns the log message obfuscated
    """
    for val in fields:
        message = re.sub(rf'{val}=.*?{separator}',
                         f'{val}={redaction}{separator}', message)
    return message
