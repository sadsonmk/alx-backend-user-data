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
    try:
        db_user = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
        db_password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
        db_host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
        my_db = os.environ.get("PERSONAL_DATA_DB_NAME")

        conn = mysql.connector.connect(
                user=db_user,
                password=db_password,
                host=db_host,
                database=my_db
                )
        return conn
    except mysql.connector.Error as err:
        return None


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


def main():
    """The function will obtain a database connection using get_db
        and retrieve all rows in the users table and display
        each row under a filtered format
    """
    conn = get_db()
    if not conn:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    hdrs = [v[0] for v in cursor.description]
    logger = get_logger()
    for row in cursor:
        value = ''
        for r, c in zip(row, hdrs):
            value += f"{c}={(r)}; "
        logger.info(value)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
