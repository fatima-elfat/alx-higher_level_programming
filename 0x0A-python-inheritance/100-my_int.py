#!/usr/bin/python3
"""the module of 12. My integer"""


class MyInt(int):
    """
    MyInt Class
    """

    def __init__(self, myint):
        """
        Initialize
        """
        self.myint = myint

    def __eq__(self, intVal):
        """
        Return: True if not equal.
        """
        return self.myint != intVal

    def __ne__(self, intVal):
        """
        Return: True if equal.
        """
        return self.myint == intVal
