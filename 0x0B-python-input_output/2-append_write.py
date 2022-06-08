#!/usr/bin/python3
"""appends file"""


def append_write(filename="", text=""):
    """Function that writes a string to a text file (UTF8)
    and returns the number of characters written"""

    with open(filename, 'a', encoding="utf-8") as ap:
        return ap.write(text)
