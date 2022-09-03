#!/usr/bin/python3
"""
Python script
"""


import requests
from sys import argv

if __name__ == "__main__":
    """
    Script that takes in a URL, sends a request to the URL
    and displays the value of the variable X-Request-Id in
    the response header
    """
    html = requests.get(argv[1])
    print((html.headers).get("X-Request-Id"))
