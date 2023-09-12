#!/usr/bin/python3
"""
the module of 9. Student to JSON.
"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student.

        Args:
            first_name : the first name.
            last_name (str): the last name.
            age (int): the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__
