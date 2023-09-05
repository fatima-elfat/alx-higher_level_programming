#!/usr/bin/python3
"""Module say_my_name"""


def say_my_name(first_name, last_name=""):
    """
     prints My name is <first name> <last name>.

     Args:
        first_name: first name.
        last_name : last name.
    Raises:
        TypeError :.:wq
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    elif type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
