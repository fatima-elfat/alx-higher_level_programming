#!/usr/bin/python3
"""module of 13. Can I?"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible.
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
