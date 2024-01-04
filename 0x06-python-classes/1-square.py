#!/usr/bin/python3
"""Defining a Square class"""

class Square:
    """Square depending on parsed size.

    Attributes:
        __size (int): parsed size
    """
    def __init__(self, size):
        """Check if type is an int
        Args:
            size (int): non-negative values
        Returns:
            None
        """
        self.__size = size
