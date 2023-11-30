#!/usr/bin/python3
"""Task 6. Find a peak"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    based on binary search.
    """
    midle = int(len(list_of_integers)//2)
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[0] < list_of_integers[len(list_of_integers) - 1]:
        return find_peak(list_of_integers[midle:])
    else:
        return find_peak(list_of_integers[:midle + 1])