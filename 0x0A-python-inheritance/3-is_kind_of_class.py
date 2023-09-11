#!/usr/bin/python3
"""
The module of 3. Same class or inherit from.
"""


def is_kind_of_class(obj, a_class):
    """
    Return: True if the object is an instance of, or if
        the object is an instance of a class that inherited from,
        the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
