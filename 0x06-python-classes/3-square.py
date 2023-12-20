#!/usr/bin/python3
"""Defining a Square class"""

class Square:
    """Represents a square with a defined size.

    Attributes:
        __size (int): stores size
    """
    def __init__(self, size=0):
        """Check if type is an int
        Args:
            size (int): non-negative values
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """area of square

        Returns:
            Area
        """
        return (self.__size) ** 2
