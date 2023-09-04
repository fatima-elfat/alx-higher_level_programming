#!/usr/bin/python3
"""The Nqueens problem"""


import sys


def queen(q_val):
    """
    the queen position validator.

    Args:
        q_val: queen val.
    """
    for i in range(size):
        n = 0
        for j in range(q_val):
            qv = q_vals[j]
            if i == qv or i + q_val == qv + j or i - q_val == qv - j:
                n = 1
                break
        if n == 1:
            n == 0
            continue
        if q_val != size - 1:
            q_vals[q_val + 1] = 0
            q_vals[q_val] = i
            queen(q_val + 1)
        else:
            q_vals[q_val] = i
            print("[[0, ", q_vals[0], "]", sep="", end="")
            for j, i in enumerate(q_vals[1:], 1):
                print(", [", j, ", ", i, "]", sep="", end="")
            print("]")


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    size = int(sys.argv[1])
except (ValueError, TypeError):
    print("N must be a number")
    sys.exit(1)
if size < 4:
    print("N must be at least 4")
    sys.exit(1)
q_vals = [0] * size
queen(0)
