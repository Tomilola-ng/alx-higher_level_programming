#!/usr/bin/python3
"""
    Program to write to a txt file,
    Returns length of char written
"""


def write_file(filename="", text=""):
    """ Write and return number func """
    with open(filename, mode="w", encoding="UTF8") as writefile:
        return writefile.write(text)
