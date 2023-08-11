#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    l_a = len(argv)
    a = {"+": add, "-": sub, "*": mul, "/": div}
    if l_a != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    if argv[2] not in a:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(
        int(argv[1]),
        argv[2],
        int(argv[3]),
        a[argv[2]](int(argv[1]), int(argv[3]))
        ))
