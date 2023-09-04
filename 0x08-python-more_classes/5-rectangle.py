#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """
    Definition of class Rectangle.

    Args:
        width (int): the width.
        height (int): the height.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle.

        Attributes:
            width (int): the width.
            height (int): the height.
        """
        self.width = width
        self.height = height

    def __del__(self):
        """
        Deletes the instance.
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Getter.

        Return: the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter.

        Args:
            value: value of the width.
        Raises:
            ValueError: If `value` is less than `0`.
            TypeError: If `value` type is not `int`.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter.

        Return: the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter.

        Args:
            value: value of the height.
         Raises:
            ValueError: If `value` is less than `0`.
            TypeError: If `value` type is not `int`.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        Returns the informal definition.

        Returns: str def.
        """
        if self.width == 0 or self.height == 0:
            return ""
        r = ""
        for i in range(self.height - 1):
            r += '#' * self.width + '\n'
        r += '#' * self.width
        return r

    def __repr__(self):
        """
        Returns the new instance repe.

        Return: str repr."""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def area(self):
        """
        Calculates area.

        Return: the value of area.
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates the perimeter of rectangule.

        Return: the value of the perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.height * 2 + self.width * 2
