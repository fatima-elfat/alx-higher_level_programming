#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    vals = []
    for i in my_list:
        vals.append((i % 2 == 0))
    return vals
