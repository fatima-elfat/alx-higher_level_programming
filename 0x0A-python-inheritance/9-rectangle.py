#!/usr/bin/python3
"""
The module of 8. Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry (7-base_geometry.py).
    """
    def __init__(self, width, height):
        """
        Initiates width and height.

        Args:
            width : ...
            height : ...
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return: the value of the arera.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return: rectangle description: [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
