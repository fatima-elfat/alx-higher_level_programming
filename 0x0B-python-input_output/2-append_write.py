#!/usr/bin/python3
"""
the module of 2. Append to a file.
"""


def append_write(filename="", text=""):
    """
    
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
