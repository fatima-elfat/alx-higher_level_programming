#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    l_l = len(my_list)
    if idx >= 0 and idx < l_l:
        del my_list[idx]
    return my_list
