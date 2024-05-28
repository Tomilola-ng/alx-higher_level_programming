#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    mycnt = 0
    for item in range(x):
        try:
            print(f'{my_list[item]}', end='')
        except (IndexError):
            continue
        mycnt += 1
    print()
    return (mycnt)
