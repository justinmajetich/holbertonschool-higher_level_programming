#!/usr/bin/python3
"""This module defines a class, BaseGeometry"""


class BaseGeometry:
    """A class defining a geometric shape"""

    def integer_validator(self, name, value):
        """Validates name/value argument

        Arguments:
            name: name associated with value
            value: value (must be integer > 0)
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

    def area(self):
        """Take area of shape"""
        raise Exception('area() is not implemented')
