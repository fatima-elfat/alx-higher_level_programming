#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = argv
    l_a = len(a)
    print("{:d} {:s}".fortmat(l_a, 'argument'), end="")
    if l_a == 0:
        print("{:s}".fortmat('s.'))
    elif l_a == 1:
        print("{:s}".fortmat(':'))
    elif l_a > 1:
        print("{:s}".fortmat('s:'))
    for i in range(1, l_av + 1):
        print('{:d}: {}'.format(i, a[i]))
