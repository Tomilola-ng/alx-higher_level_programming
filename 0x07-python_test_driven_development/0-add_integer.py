#!/usr/bin/python3
"""
Module 0-add_integer
Contains one method that returns an int sum
Accepts two values, int or float and casts to int then add
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    - a: int or float
    - b: int or float (default is 98)

    Returns:
    - int: the sum of a and b

    Raises:
    - TypeError: if a or b is not an int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
