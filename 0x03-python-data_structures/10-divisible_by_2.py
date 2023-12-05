#!/usr/bin/python3
#10-divisible_by_2.py
def divisible_by_2(my_list=[]):
    """ Oh my Cin """
    new_list = []
    if my_list:
        for j in my_list:
            new_list.append(False if j % 2 else True)
    return new_list