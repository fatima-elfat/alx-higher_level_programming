#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    else:
        r = []
        for i in matrix:
            r.append(list(map(lambda a: a**2, i)))
        return (r)
