#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    a = 0
    b = 0
    for i, j in my_list:
        a += j
        b += j * i
    if a == 0:
        return 0
    return b/a
