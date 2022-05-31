#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix
    """

    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    div1 = "div must be a number"
    div2 = "division by zero"

    if not type(div) in (float, int):
        raise TypeError(div1)
    if div == 0:
        raise ZeroDivisionError(div2)

    if not type(matrix) is (list) or len(matrix) == 0:
        raise TypeError(err1)
    for array in matrix:
        if not type(array) is (list):
            raise TypeError(err1)

        if len(matrix[0]) is not len(array):
            raise TypeError(err2)
        for new in array:
            if not type(new) in (float, int):
                raise TypeError(err1)

    return[[round(new / div, 2) for new in i] for i in matrix]
