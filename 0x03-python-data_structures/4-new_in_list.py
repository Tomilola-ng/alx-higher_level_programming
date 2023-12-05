#!/usr/bin/python3
#new_in_list.py
def new_in_list(my_list, idx, element):
    """ Returns a copy or orignal """
    copy_list = []
    for i in (my_list):
        copy_list.append(i)
    if idx < 0 or idx > len(my_list):
        return copy_list
    copy_list[idx] = element
    return copy_list
