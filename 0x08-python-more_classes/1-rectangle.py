#!/usr/bin/python3
"""
    Create empty rectangle class
"""


class Rectangle:
    """
        An empty rectangle class
    """

    def __init__(self, width=0, height=0):
        """ Set up rectangle size """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width Setter """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
