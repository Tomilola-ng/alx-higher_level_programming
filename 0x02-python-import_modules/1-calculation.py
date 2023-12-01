#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import sub, div, mul, add

    a = 10
    b = 5

    mul_answer = mul(a, b)
    add_answer = add(a, b)
    div_answer = div(a, b)
    sub_answer = sub(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, add_answer))
    print("{:d} - {:d} = {:d}".format(a, b, sub_answer))
    print("{:d} * {:d} = {:d}".format(a, b, mul_answer))
    print("{:d} / {:d} = {:d}".format(a, b, div_answer))
