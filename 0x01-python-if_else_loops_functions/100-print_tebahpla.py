#!/usr/bin/python3
for index in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(index, chr(index - 33)), end="")
