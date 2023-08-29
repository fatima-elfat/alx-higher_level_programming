#!/usr/bin/python3
"""Class Square"""


class Square:
    """
    Definition of class Square.

    Args:
       __size (int): size of the side.
    """
    __size = None

    def __init__(self, sizeval=0):
        """
        Initializes the square.

        Attributes:
            sizeval (int): size of the side.
        Raises:
            ValueError: If `sizeval` is less than `0`.
            TypeError: If `sizeval` type is not `int`.
        """
        if sizeval < 0:
            raise ValueError("size must be >= 0")
        if type(sizeval) is not int:
            raise TypeError('size must be an integer')
        self.__size = sizeval
