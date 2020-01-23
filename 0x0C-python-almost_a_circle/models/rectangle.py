#!/bin/usr/python3
"""This module defines a class, Rectangle, inheriting
from Base class.
"""


from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate class object.

        Arguments
            width: width of rectangle
            height: height of rectangle
            x:
            y:
            id: object id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return value of private variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value of private variable width"""
        self.__width = value

    @property
    def height(self):
        """Return value of private variable height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set value of private variable height"""
        self.__height = value

    @property
    def x(self):
        """Return value of private variable x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set value of private variable x"""
        self.__x = value

    @property
    def y(self):
        """Return value of private variable y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set value of private variable y"""
        self.__y = value
