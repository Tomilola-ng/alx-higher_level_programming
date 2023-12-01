#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv)
    result = 0

    if arg_len > 1:
        for num in argv[1:]:
            result = result + int(num)
    
    print(result)