#!/usr/bin/python3
"""Object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename, 'w') as wt:
        wt.write(json.dumps(my_obj))
