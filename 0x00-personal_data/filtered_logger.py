#!/usr/bin/env python3
"""This is a module to implement a regex
    to replace occurrences of certain field values in user-data.
"""

import re
from typing import List
import os
import logging
import mysql.connector
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """connects to a secure holberton database to read a users table"""
    user = os.environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    host = os.environ.get('PERSONAL_DATA_DB_HOST', "localhost")
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    database = os.environ.get('PERSONAL_DATA_DB_NAME')

    myDatabase = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
            )
    return myDatabase


def get_logger() -> logging.Logger:
    """creates a logger which return a logger object"""
    my_logger = logging.getLogger("user_data")
    my_logger.setLevel(logging.INFO)
    my_logger.propagate = False
    hdlr = logging.StreamHandler()
    hdlr.setFormatter(RedactingFormatter(PII_FIELDS))
    my_logger.addHandler(hdlr)
    return my_logger


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
