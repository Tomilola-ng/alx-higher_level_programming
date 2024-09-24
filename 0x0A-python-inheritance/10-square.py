#!/usr/bin/python3

"""
    Rectangle 
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class from Rectangle Base Model """

    def __init__(self, size):
        """ Init function """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
