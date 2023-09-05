#!/usr/bin/python3
""" Module of Divide a matrix"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.

    Args:
        matrix : list of ìnt`and `float`.
        div (int, float):  nbr of the divider.
    Raises:
        TypeError: div not int or float, or matrix not list of int and float.
            or the rows of matrix not same size.
        ZeroDivisionError: if dev equal to zero.
    Return: new matrix.
    """
    e1 = "matrix must be a matrix (list of lists) of integers/floats"
    e2 = "div must be a number"
    e3 = "division by zero"
    e4 = "Each row of the matrix must have the same size"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(e1)
    if not isinstance(div, (int, float)):
        raise TypeError(e2)
    if div == 0:
        raise ZeroDivisionError(e3)
    new_m = []
    len_m = len(matrix[0])
    for l_ in matrix:
        if type(l_) is not list:
            raise TypeError(e1)
        if len(l_) != len_m:
            raise TypeError(e4)
        l_2 = []
        for c in l_:
            if not isinstance(c, (int, float)):
                raise TypeError(e1)
            l_2.append(round(c/div, 2))
        new_m.append(l_2)
    return new_m
