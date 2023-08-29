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
        if type(sizeval) is not int:
            raise TypeError("size must be an integer")
        if sizeval < 0:
            raise ValueError('size must be >= 0')
        self.__size = sizeval

    @property
    def size(self):
        """"
        Getter function.

        Return: size of the side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter function.

        Args:
            value: value of the side.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns the area of square.

        Returns:
            the value of area.
        """
        return (self.__size)**2

    def __eq__(self, other):
        """
        Return: if equal.
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Return: if not equal.
        """
        return self.size != other.size

    def __gt__(self, other):
        """
        Return: if greater than.
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Return: if greater or eaual than.
        """
        return self.size >= other.size

    def __lt__(self, other):
        """
        Return: if lesser than.
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Return: if lesser or equal than.
        """
        return self.size <= other.size
