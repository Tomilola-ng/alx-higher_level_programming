#!/usr/bin/python3
"""Class definition for Square"""


class Square:
    """Represents a square with a defined size.

    Attributes:
        __size (int): Size of a side of the square
    """

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): Size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculates the square's area.

        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Getter for __size.

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size.

        Args:
            value (int): The size of a side of the square
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

    def __lt__(self, other):
        """Compares if the square is less than another by area.

        Args:
            other (Square): Square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compares if the square is less than or equal to another by area.

        Args:
            other (Square): Square to compare against
        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compares if the square is equal to another by area.

        Args:
            other (Square): Square to compare against
        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compares if the square is not equal to another by area.

        Args:
            other (Square): Square to compare against
        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compares if the square is greater than or equal to another by area.

        Args:
            other (Square): Square to compare against
        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compares if the square is greater than another by area.

        Args:
            other (Square): Square to compare against
        Returns:
            True or False
        """
        return self.size > other.size
