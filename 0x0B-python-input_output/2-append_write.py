#!/usr/bin/python3
"""

"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file.

    Args:
        filename : the name of the file.
        text : the text to append.
    Return:
        the number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
