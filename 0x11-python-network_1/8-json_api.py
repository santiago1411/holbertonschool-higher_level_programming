#!/usr/bin/python3
"""
"""


import requests
from sys import argv

if __name__ == "__main__":
    """
    """
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        dato = r.json()
        if dato == {}:
            print("No result")
        else:
            print("[{}] {}".format(dato.get("id"), dato.get("name")))
    except ValueError:
        print("Not a valid JSON")
