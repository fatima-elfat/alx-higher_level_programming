#!/usr/bin/python3
"""Module of Integers addition"""


def add_integer(a, b=98):
    """
    Adds two numbers as integers.

    Args:
        a (int, float): first number.
        b (int, float): second number.
    Raises:
            TypeError: If `a` or `b` types are not `int` or `float`.
    Return: a+b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
