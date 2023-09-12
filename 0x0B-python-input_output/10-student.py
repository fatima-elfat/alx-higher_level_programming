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

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance.

        Args:
            attrs : only attribute names contained
            in this list must be retrieved.
        """
        if (type(attrs) == list and
                all(isinstance(a, str) for a in attrs)):
            dic = {}
            for att in attrs:
                if att in self.__dict__:
                    dic[att] = self.__dict__.get(att)
            return dic
        return self.__dict__
