#!/usr/bin/python3
"""This module defines a class Student
"""


class Student:
    """This class Student defines object by...

    Attributes:
        first_name: first name of student
        last_name: last name of student
        age: age of student
    """
    def __init__(self, first_name, last_name, age):
        """Instantiate class object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dict representation of instance
        """
        valid_key = []
        return_dict = {}
        if type(attrs) is list:
            for item in attrs:
                if type(item) is str and item in self.__dict__:
                    return_dict.update({item: self.__dict__[item]})
            return return_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace class attributes with those provided in json
        """
        if len(json) != 0:
            self.__dict__ = json
