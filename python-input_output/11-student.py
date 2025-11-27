#!/usr/bin/python3
"""
This module defines a class Student based on 10-student.py.
"""


class Student:
    """
    Defines a student by first_name, last_name and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a strings, only attributes in that list are retrieved.
        """
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            filtered_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered_dict[key] = self.__dict__[key]
            return filtered_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for key, value in json.items():
            self.__dict__[key] = value
