#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = argv
    l_a = len(a) - 1
    print("{:d} {:s}".format(l_a, 'argument'), end="")
    if l_a == 0:
        print("{:s}".format('s.'))
    elif l_a == 1:
        print("{:s}".format(':'))
    elif l_a > 1:
        print("{:s}".format('s:'))
    for i in range(1, l_a + 1):
        print('{:d}: {:s}'.format(i, a[i]))
