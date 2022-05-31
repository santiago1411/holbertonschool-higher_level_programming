#!/usr/bin/python3
"""
Print a text with 2 new lines after
each of these characters
. ? :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    """
    flag = True

    if type(text) != (str):
        raise TypeError("text must be a string")

    for i in text:
        if i == ' ' and flag is True:
            continue
        if i in ['.', '?', ':']:
            print(i, end="")
            print()
            print()
            flag = True
        else:
            print(i, end="")
            flag = False
