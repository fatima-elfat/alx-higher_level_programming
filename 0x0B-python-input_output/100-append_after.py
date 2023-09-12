#!/usr/bin/python3
"""
the module of 13. Search and update.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """

    with open(filename, mode="r+", encoding="utf-8") as f:
        text = ""
        for line in f:
            text += line
            if search_string in line:
                text += new_string
        f.seek(0)
        f.write(text)
