#!/usr/bin/python3
"""
"""


import requests
from sys import argv

if __name__ == "__main__":
    """
    """
    html = requests.get(argv[1])
    print((html.headers).get("X-Request-Id"))
