#!/usr/bin/python3
"""
My Code FUNC
"""


def matrix_divided(matrix, div):
    """
    MATRIX DivideR
    """
    a_list = []
    response = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(response)

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(response)
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        list_tmp = []
        for number in row:
            if type(number) is not int and type(number) is not float:
                raise TypeError(message)
            list_tmp.append((round((number / div), 2)))
        a_list.append(list_tmp)
    return a_list
