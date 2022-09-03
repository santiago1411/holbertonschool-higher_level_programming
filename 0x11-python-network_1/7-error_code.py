#!/usr/bin/python3
"""
Python script
"""


import requests
from sys import argv

if __name__ == "__main__":
    """
    Script that takes in a URL, sends a request to the URL
    and displays the body of the response.
    """
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
