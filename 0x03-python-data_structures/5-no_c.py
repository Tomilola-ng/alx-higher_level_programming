#!/usr/bin/python3
#5-no_c.py
def no_c(my_string):
    """ return string without char c or C"""
    new_str = ""
    for char in my_string:
        if char == "c" or char == "C":
            continue
        new_str += char
    return new_str
