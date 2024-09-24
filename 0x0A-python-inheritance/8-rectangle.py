#!/usr/bin/python3

""" Base Geometry Class Inheritance """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class based on Base Geometry Class """

    def __init__(self, width, height):
        """
            Function to initialize a class
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
