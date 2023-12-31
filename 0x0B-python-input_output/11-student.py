#!/usr/bin/python3
"""
the module of 11. Student to disk and reload.
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
            for key in attrs:
                if hasattr(self, key):
                    key = getattr(self, key)
            return key
        return self.__dict__

    def reload_from_json(self, json):
        """
        defines a student by: (based on 10-student.py).

        Args:
            json : key will be the public attribute name,
            a value will be the value of the public attribute.
        """
        for key, val in json.items():
            setattr(self, key, val)
