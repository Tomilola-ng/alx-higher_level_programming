#!/usr/bin/python3
""" convert Student class to JSON"""


class Student:
    """ OOP Student class definition """

    def __init__(self, first_name, last_name, age):
        """ Instantiate data """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ simply return class in dict format """
        return self.__dict__
