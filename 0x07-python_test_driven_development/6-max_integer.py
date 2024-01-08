#!/usr/bin/python3
"""
    BIGGEST INT IN A PARSED LIST
"""


def max_integer(list=[]):
    """
    Find and return the maximum integer in a list of integers.

    If the list is empty, the function returns None.

    Args:
    - lst (list): List of integers.

    Returns:
    - int or None: The maximum integer in the list or None if the list is empty.
    """

    if len(list) == 0:
        return None

    max = list[0]
    i = 1

    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1

    return max
