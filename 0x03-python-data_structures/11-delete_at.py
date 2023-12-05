#!/usr/bin/python3
#11-delete_at.py
def divisible_by_2(my_list=[]):
    """ Too Young """
    new_list = []
    if my_list:
        for _arr in my_list:
            new_list.append(False if _arr % 2 else True)
    return new_list
