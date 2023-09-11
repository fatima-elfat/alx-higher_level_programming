#!/usr/bin/python3
"""
The module of 6. Improve Geometry based on 5. Geometry module.
"""


class BaseGeometry:
    """
    Class BaseGeometry.
    """
    def area(self):
        """
        Raises: NOt implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Raises:
            TypeError : ...
            ValueError : ...
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 1:
            raise ValueError("{:s} must be greater than 0".format(name))
