#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    r = 0
    a = argv
    l_a = len(a) - 1
    if (l_a > 1):
        for i in range(1, l_a + 1):
            r += (int(a[i]))
    print("{:d}".format(r))
