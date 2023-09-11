#!/usr/bin/python3
"""
The module of 2. Exact same object.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an
    instance of the specified class ; otherwise False.

    Return: True if an instance of the specified class, otherwise False.
    """
    return type(obj) == a_class
