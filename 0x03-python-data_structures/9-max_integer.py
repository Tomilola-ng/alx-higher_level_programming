#!/usr/bin/python3
#9-max_integer.py
def max_integer(my_list=[]):
    """Whats going on"""
    if my_list:
        max_el = my_list[0]
        for j in my_list:
            if j > max_el:
                max_el = j
        return max_el
    return None