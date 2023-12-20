#!/usr/bin/python3
"""defines a class square"""


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
        self.size = size

    def area(self):
        """area of square

        Returns:
            Area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """size getter
        Returns:
           Square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter
        Args:
            value (int): square side size
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
