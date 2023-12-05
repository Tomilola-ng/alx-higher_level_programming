#!/usr/bin/python3
#6-print_matrix_integer.py
def print_matrix_integer(matrix=[[]]):
    """ Arrays of Arrays """
    for _arr in matrix:
        print(" ".join("{:d}".format(i) for i in _arr))
