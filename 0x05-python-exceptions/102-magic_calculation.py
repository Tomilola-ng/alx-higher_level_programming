#!/usr/bin/python3

def magic_calculation(a, b):
    answer = 0
    for cnt in range(1, 3):
        try:
            if (cnt > a):
                raise (Exception('Too far'))
            else:

                answer = (((a ** b) / cnt) + answer)
        except (Exception):
            answer = (b + a)
            break
    return (answer)
