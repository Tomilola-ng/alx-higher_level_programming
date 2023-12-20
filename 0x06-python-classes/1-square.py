#!/usr/bin/python3
"""Defining a Square class"""

class Square:
    """Square depending on parsed size.

    Attributes:
        __size (int): parsed size
    """
    def __init__(self, size):
        """Initializes a square

        Args:
            size (int): size of a size of the square

        Returns: None
        """
        self.__size = size
