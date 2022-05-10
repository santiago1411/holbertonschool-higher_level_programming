#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_list = matrix[:]

    for i in range(len(new_list)):
        new_list[i] = (list(map(lambda x: x ** 2, new_list[i])))

    return new_list
