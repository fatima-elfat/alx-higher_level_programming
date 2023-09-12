#!/usr/bin/python3
"""
the odule of 1. Write to a file.
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    (UTF8) and returns the number of characters written.

    Args:
        filename : The name of the file.
        text : The text to write.
    Return: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
