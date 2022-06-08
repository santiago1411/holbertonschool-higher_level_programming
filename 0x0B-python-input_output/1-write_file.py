#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8)
    and returns the number of characters written"""

    with open(filename, 'w', encoding="utf-8") as wt:
        return wt.write(text)
