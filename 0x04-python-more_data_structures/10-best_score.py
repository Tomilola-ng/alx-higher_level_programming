#!/usr/bin/python3
def best_score(a_dictionary):
    best_name = ""
    top_score = 0
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > top_score:
                top_score = a_dictionary[key]
                best_name = key
        return best_name
    return None
