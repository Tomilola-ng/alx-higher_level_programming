#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    args_len = len(argv) - 1

    if args_len == 0:
        print("0 arguments.")
    elif args_len == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(args_len))

    for i in range(1, args_len + 1):
        print("{:d}: {}".format(i, argv[i]))
