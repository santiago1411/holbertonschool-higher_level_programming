#!/usr/bin/python3
"""
Function that prints a square with the character #.
"""


def print_square(size):
    """
    Function that prints a square with the character #.
    Size must be an integer and > 0
    """
    if type(size) != int or type(size) == float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
