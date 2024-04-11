#!/usr/bin/env python3
"""This is a module to implement a regex
    to replace occurrences of certain field values in user-data.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """a function that returns the log message obfuscated
    """
    for val in fields:
        message = re.sub(rf'{val}=.*?{separator}',
                         f'{val}={redaction}{separator}', message)
    return message
