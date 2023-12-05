#!/usr/bin/python3
#3-print_reversed_list_integer.py
def print_reversed_list_integer(my_list=[]):
    """print all integers in my_list"""
    counter = len(my_list)
    for j in my_list:
        print('{:d}'.format(my_list[counter-j]))
