#!/usr/bin/python3
"""
the module of 0. Read file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename : the name of the file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
