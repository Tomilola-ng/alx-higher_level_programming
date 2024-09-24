#!/usr/bin/python3

"""
    Is Inherited and match parents
"""


def inherits_from(obj, a_class):
    """
        Return True or False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
