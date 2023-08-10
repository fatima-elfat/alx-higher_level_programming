#!/usr/bin/python3
def remove_char_at(str, n):
    r = ""
    for i in range(len(str)):
        if i != n:
            r += str[i]
    return r
