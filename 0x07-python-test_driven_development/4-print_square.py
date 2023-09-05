#!/usr/bin/python3
"""A module of print_square."""


def print_square(size):
    """
    prints a square with the character #.

    Return: str #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    r = '#' * size
    for i in range(size):
        print(r)
