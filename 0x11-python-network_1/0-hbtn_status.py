#!/usr/bin/python3
"""
"""


import urllib.request

if __name__ == "__main__":
    """
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {(html.decode('UTF-8'))}")
