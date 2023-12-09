#!/usr/bin/python3
def get_sum_weight(scores):
    jk_list = list(map(lambda a: a[1], scores))
    return sum(jk_list)

def prom(scores):
    jk_list = list(map(lambda a: a[0] * a[1], scores))
    return sum(jk_list)

def weight_average(my_list=[]):
    if len(my_list) != 0:
        average = prom(my_list) / get_sum_weight(my_list)
        return average
    return 0
