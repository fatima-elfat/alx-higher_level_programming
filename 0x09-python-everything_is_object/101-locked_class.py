#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    It prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.

    AttributeError: 'LockedClass' object has no attribute 'last_name'.
    """

    __slots__ = ["first_name"]
