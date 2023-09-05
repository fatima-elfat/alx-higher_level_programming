#!/usr/bin/python3
""" a module of text_indentation"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text : must be string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    a = 0
    len_ = len(text)
    while a < len_:
        b = a
        while b < len_ and text[b] == " ":
            b += 1
        a = b
        while a < len_ and text[a] != "."\
                and text[a] != "?" and text[a] != ":":
            a += 1
        if a < len_:
            a += 1
        print(text[b:a], end="")
        a -= 1
        if text[a] == "." or text[a] == "?" or text[a] == ":":
            print("\n")
        a += 1
