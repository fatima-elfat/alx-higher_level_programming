#!/usr/bin/python3
"""
The module of 1. My list.
"""


class MyList(list):
    """
    Inherits from list.
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
