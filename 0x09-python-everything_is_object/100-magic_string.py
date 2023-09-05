#!/usr/bin/python3
def magic_string():
    magic_string.count = getattr(magic_string, 'len_', 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.len_)])
