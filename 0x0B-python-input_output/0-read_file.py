#!/usr/bin/python3
"""
    Program that reads text files (UTF8) then  printout:
"""


def read_file(filename=""):
    """ Using inbuilt with function """
    with open(filename, encoding="UTF-8") as readfile:
        print(readfile.read(), end="")
