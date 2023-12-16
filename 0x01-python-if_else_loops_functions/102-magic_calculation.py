#!/usr/bin/python3
def magic_calculation(index, col, num):
    if index < col:
        return num
    if num > col:
        return index + col
    return index * col - num
