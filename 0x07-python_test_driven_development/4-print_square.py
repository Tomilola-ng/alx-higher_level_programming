#!/usr/bin/python3
"""
    My Code FUNC
"""


def print_square(size):
    """
    # SHAPE PRINTER
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        hash_str = ""

        for i in range(size):
            for j in range(size):
                hash_str += "#"
            hash_str += "\n"

        print(hash_str)
