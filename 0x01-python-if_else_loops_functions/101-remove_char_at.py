#!/usr/bin/python3
def remove_char_at(str_p, num):
    if (num < 0):
        return str_p
    new = str_p[:num] + str_p[num + 1:]
    return new
