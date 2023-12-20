#!/usr/bin/python3
for index in range(0, 10):
    for col in range(1, 10):
        if index >= col:
            continue
        if index == 8 and col == 9:
            print("{:d}{:d}".format(index, col))
        else:
            print("{:d}{:d}".format(index, col), end=", ")
