#!/usr/bin/python3

"""
    Attributes
"""


def add_attribute(obj, att, value):
    """ If possible add attribute """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
