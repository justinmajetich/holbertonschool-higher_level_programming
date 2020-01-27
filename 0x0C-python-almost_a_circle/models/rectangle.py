#!/usr/bin/python3
"""This module defines a class, Rectangle, inheriting
from Base class.
"""


import json
from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate class object.

        Arguments
            width: width of rectangle
            height: height of rectangle
            x: x axis offset
            y: y axis offset
            id: object id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Compute area of rectangle object"""
        return self.__width * self.__height

    def display(self):
        """Prints representation of object with '#'s"""
        print('\n' * self.__y +
              ((' ' * self.__x) +
               ('#' * self.__width) + '\n') *
              self.__height, end='')

    def __str__(self):
        """Returns string representation of object"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def to_dictionary(self):
        """Returns dictionary representation of object"""
        clean = {}
        for key, val in self.__dict__.items():
            clean[key.split('_')[-1]] = val
        return clean

    def update(self, *args, **kwargs):
        """Update attributes"""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    @property
    def width(self):
        """Return value of private variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value of private variable width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Return value of private variable height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set value of private variable height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Return value of private variable x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set value of private variable x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Return value of private variable y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set value of private variable y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
