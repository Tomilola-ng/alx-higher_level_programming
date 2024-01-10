#!/usr/bin/python3
""" convert Student class to JSON """


class Student:
    """ OOP Student class definition """

    def __init__(self, first_name, last_name, age):
        """ Instantiate data """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ simply return class in dict format """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}

            for i in attrs:
                try:
                    my_dict[i] = self.__dict__[i]
                except Exception:
                    pass
            return my_dict

    def reload_from_json(self, json):
        """ Update based on parsed JSON """
        for i in json:
            self.__dict__.update({i: json[i]})
