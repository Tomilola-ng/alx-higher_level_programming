#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for col in matrix:
        tmp_col = []
        for num in col:
            tmp_col.append(num * num)
        square.append(tmp_col)
    return square
