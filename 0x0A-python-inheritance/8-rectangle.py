#!/usr/bin/python3
"""This module defines a class, Rectangle"""


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


class Rectangle(BaseGeometry):
    """A class definig a rectangle """
    def __init__(self, width, height):
        """Instantiates class object

        Arguments:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
