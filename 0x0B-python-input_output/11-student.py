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

    def to_json(self):
        """Retrieve dict representation of instance
        """
        return self.__dict__
