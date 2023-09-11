#!/usr/bin/python3
"""
The module of 10. Square #1.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle (9-rectangle.py).
    """
    def __init__(self, size):
        """
        Instantiation of size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
