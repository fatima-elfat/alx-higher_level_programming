#!/usr/bin/python3
"""Class Square"""


class Square:
    """
    Definition of class Square.

    Args:
       __size : size of the side.
    """
    __size = None
    def __init__(self, sizeval):
        """
        Initializes the square.

        Attributes:
            sizeval: size of the side.
        """
        self.__size = sizeval
