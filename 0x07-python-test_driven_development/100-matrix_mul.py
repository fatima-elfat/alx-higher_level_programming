#!/usr/bin/python3
"""a module 100-matrix_mul.py"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices.

    Args:
        m_a : first matrix.
        m_b : second matrix.
    Return: multiplied matrix.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for l_ in m_a:
        if not isinstance(l_, list):
            raise TypeError("m_a must be a list of lists")
    for l_ in m_b:
        if not isinstance(l_, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0 or m_a == [[]] or m_b == [[]]:
        raise ValueError("{} can't be empty".format(
            "m_a" if len(m_a) == 0 or m_a == [[]] else "m_b"
            ))
    for i in m_a:
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        if len(i) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_m = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            r = 0
            for k in range(len(m_a[0])):
                r += m_a[i][k] * m_b[k][j]
            row.append(r)
        new_m.append(row)
    return new_m
