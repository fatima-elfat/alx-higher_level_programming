#!/usr/bin/python3
"""
the module of 12. Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    if n <= 0:
        return []
    triList = [[1]]
    while len(triList) != n:
        tri = triList[-1]
        a = [1]
        for i in range(len(tri) - 1):
            a.append(tri[i] + tri[i + 1])
        a.append(1)
        triList.append(a)
    return triList