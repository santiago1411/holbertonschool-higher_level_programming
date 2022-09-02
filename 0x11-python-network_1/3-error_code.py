#!/usr/bin/python3
"""
"""


import urllib.error
import urllib.request
from sys import argv

if __name__ == "__main__":
    """
    """
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode("utf-8"))

    except urllib.error.HTTPError as errr:
        print("Error code: {}".format(errr.code))
