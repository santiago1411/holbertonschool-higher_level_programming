#!/usr/bin/python3
"""
"""


from cgitb import html
import requests

if __name__ == "__main__":
    """
    """
    html = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(html.text)}")
    print(f"\t- content: {(html.text)}")
