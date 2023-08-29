#!/usr/bin/python3
"""Class Square"""


class Square:
    """
    Definition of class Square.

    Args:
       __size (int): size of the side.
       __position (int, int): position in square.
    """
    __size = None
    __position = None

    def __init__(self, sizeval=0, positionval=(0,0)):
        """
        Initializes the square.

        Attributes:
            sizeval (int): size of the side.
            positionval (int, int): position in square.
        Raises:
            ValueError: If `sizeval` is less than `0`.
            TypeError: If `sizeval` type is not `int`, or
            `positionval` not a tuple of 2 positive integers.
        """
        if type(sizeval) is not int:
            raise TypeError("size must be an integer")
        if sizeval < 0:
            raise ValueError('size must be >= 0')
        if type(positionval) is not tuple or len(positionval) != 2 or\
           type(positionval[0]) is not int or type(positionval[1]) is not int\
           or positionval[0] < 0 or positionval[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = sizeval
        self.__position = positionval

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

    @property
    def position(self):
        """"
        Getter function.

        Return: position of the squre.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter function.

        Args:
            value: value of the position.
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        returns the area of square.

        Returns:
            the value of area.
        """
        return (self.__size)**2

    def my_print(self):
        """
        Prints in stdout the square with the character #,
        position should be use by using space.
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
