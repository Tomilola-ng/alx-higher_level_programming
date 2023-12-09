#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    result_arr = []
    for item in a_dictionary:
        result_arr.append(item)
    result_arr.sort()
    for item in result_arr:
        print('{}: {}'.format(item, a_dictionary[item]))
