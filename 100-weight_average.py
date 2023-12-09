#!/usr/bin/python3
def total_weigh(scores):
    list_weights = list(map(lambda a: a[1], scores))
    return sum(list_weights)


def promedium(scores):
    list_promediums = list(map(lambda a: a[0] * a[1], scores))
    return sum(list_promediums)


def weight_average(my_list=[]):
    if len(my_list) != 0:
        average = promedium(my_list) / total_weigh(my_list)
        return average
    return 0        
