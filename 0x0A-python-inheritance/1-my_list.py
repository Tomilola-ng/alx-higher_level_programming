#!/usr/bin/python3

""" A List Class Methods """


class MyList(list):
    """ Main Class """

    def print_sorted(self):
        """ Print Sorted Values out,"""
        print(sorted(self))
