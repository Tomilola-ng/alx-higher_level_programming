#!/usr/bin/python3
"""
    Program to append str to a .txt file,
    Returns length of char appended
"""


def append_write(filename="", text=""):
    """ Append to .txt file and return charlen """
    with open(filename, mode="a", encoding="UTF8") as appendfile:
        return appendfile.write(text)
