#!/usr/bin/python3

"""
    Base Int Class
"""


class MyInt(int):
    """ Class to invert integers """

    def __eq__(self, value):
        """ Operator to override positively """
        return self.real != value

    def __ne__(self, value):
        """ Operator to override negatively """
        return self.real == value
