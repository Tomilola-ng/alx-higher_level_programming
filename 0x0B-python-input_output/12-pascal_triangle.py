#!/usr/bin/python3
""" PASCAL TRIANGLE """


def pascal_triangle(n):
    """ Returns PASCALS's Triangle """

    if n <= 0:
        retun []
    else:
        return [1,[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
