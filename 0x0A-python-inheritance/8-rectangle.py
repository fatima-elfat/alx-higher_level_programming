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