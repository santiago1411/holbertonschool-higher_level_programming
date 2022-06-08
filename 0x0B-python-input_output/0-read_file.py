#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, encoding="utf-8") as r:
        read_file = r.read()
        print(read_file, end="")
