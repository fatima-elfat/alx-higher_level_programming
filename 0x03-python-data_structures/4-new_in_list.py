#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list.copy()
    if idx < len(my_list) and idx >= 0:
        a[idx] = element
    return a
