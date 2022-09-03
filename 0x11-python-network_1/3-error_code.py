#!/usr/bin/python3
"""
Python script non-importable
"""


import urllib.error
import urllib.request
from sys import argv

if __name__ == "__main__":
    """
    script that takes in a URL, sends a request to
    the URL and displays the body of the response.
    """
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode("utf-8"))

    except urllib.error.HTTPError as errr:
        print("Error code: {}".format(errr.code))
