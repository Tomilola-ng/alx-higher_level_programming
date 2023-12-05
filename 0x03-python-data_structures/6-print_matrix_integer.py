#!/usr/bin/python3
#6-print_matrix_integer.py
def print_matrix_integer(matrix=[[]]):
    """ Arrays of Arrays """
    if not matrix:
        print()
    for _arr in matrix:
        print(_arr)
        # print(" ".join("{:d}".format(_arr)))
        # for i in _arr:
        # print(" ".join("{:d}".format(i) for i in _arr))