#!/usr/bin/python3
def pow(num_1, num_2):
    res = 1
    base = 1
    numb = 0
    if num_2 < 0:
        numb = num_2
        num_2 = (-1) * num_2
    for i in range(num_2):
        res *= num_1
        base = res * res
    if numb < 0:
        res /= base
    return res
