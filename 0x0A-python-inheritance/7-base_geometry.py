#!/usr/bin/python3

"""
    Base Geometry
"""


class BaseGeometry:
    """ Main Base Geometry Class """

    def area(self):
        """ Tmp function still remains """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Checks if value is an integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
