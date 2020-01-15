#!/usr/bin/python3
"""This module defines a class, rectangle"""


class Rectangle:
    """Defines a rectangle by height/wdith"""
    def __init__(self, width=0, height=0):
        """Instantiates class object

        Attributes:
            width: rectangle width (private)
            height: rectangle height (private)
        """
        self.width = width
        self.height = height

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.width is 0 or self.height is 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of class object"""
        if self.width is 0 or self.height is 0:
            return ''
        else:
            return ((('#' * self.width) + '\n') * self.height)[:-1]

    @property
    def width(self):
        """Get rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Get rectangle height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
