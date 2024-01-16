#!/usr/bin/python3
""" Base Class """


class Base:
    """ Base Class Definition """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiate data """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects