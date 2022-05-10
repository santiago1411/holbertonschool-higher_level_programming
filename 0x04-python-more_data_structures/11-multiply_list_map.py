#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new = len(my_list).copy()
    if my_list:
        new *= number
    return new