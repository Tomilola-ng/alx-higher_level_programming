#!/usr/bin/python3
"""
    Create empty rectangle class
"""


class Rectangle:
    """
        An empty rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Set up rectangle size """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """ Height setter """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Area of rectangle """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Perimeter of rectangle """

        if self.__height == 0 or self.__width == 0:
            return 0

        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """ Print ## for Rectangle size """

        if self.__width == 0 or self.__height == 0:
            return ""

        hash_str = ""

        for i in range(self.__height):
            for j in range(self.__width):
                hash_str += str(self.print_symbol)
            hash_str += "\n"

        return hash_str

    def __repr__(self):
        """ Representation of func """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Print custom msg when to delete """

        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Always returns rect with bigger Area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
            This is a new inctance creator
        """

        return cls(size, size)
