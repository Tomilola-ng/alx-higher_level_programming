#!/usr/bin/python3
def uppercase(str_parsed):
    for index in str_parsed:
        if ord(index) > 96 and ord(index) < 123:
            index = chr(ord(index) - 32)
        print("{}".format(index), end="")
    print()
