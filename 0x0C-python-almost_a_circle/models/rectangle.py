#!/usr/bin/python3
""" My Rectangle Class inherted from Base """
from models.base import Base


class Rectangle(Base):
    """ Read the code """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiate Class """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ property width getter """

        return self.__width

    @width.setter
    def width(self, value):
        """ property Width setter """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ property height getter """

        return self.__height

    @height.setter
    def height(self, value):
        """ property height setter """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ property position x getter """

        return self.__x

    @x.setter
    def x(self, value):
        """ property position y setter """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ property y getter """

        return self.__y

    @y.setter
    def y(self, value):
        """ property y setter """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value