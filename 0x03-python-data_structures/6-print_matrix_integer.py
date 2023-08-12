#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        t = 0
        for j in i:
            l = len(i) - 1
            if t == l:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            t += 1
        print()
