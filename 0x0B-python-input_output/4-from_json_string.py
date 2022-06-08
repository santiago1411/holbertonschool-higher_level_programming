#!/usr/bin/python3
"""To JSON string"""


import json


def from_json_string(my_str):
    """Function that returns an object (Python data structure)
    represented by a JSON string:"""

    return json.loads(my_str)
