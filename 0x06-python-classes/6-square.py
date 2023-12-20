#!/usr/bin/python3
"""Defining a Square class"""

class Square:
    """Represents a square with a defined size.

    Attributes:
        __size (int): stores size
    """
    def __init__(self, size=0, position=(0, 0)):
        """Check if type is an int
        Args:
            size (int): non-negative values
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """area of square

        Returns:
            Area
        """
        return (self.__size * self.__size)

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

    @property
    def position(self):
        """
        pos of square getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        pos of square setter
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Square printer

        Returns:
            None
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
