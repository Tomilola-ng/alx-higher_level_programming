#!/usr/bin/python3
def print_last_digit(num_parsed):
    if num_parsed < 0:
        num_parsed = ((-1) * num_parsed) % 10
    else:
        num_parsed = num_parsed % 10
    print("{:d}".format(num_parsed), end="")
    return num_parsed
