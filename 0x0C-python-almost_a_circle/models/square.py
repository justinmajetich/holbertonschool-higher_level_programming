#!/usr/bin/python3
"""This module defines a class, Square, which inherits
from classes Base and Rectangle
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square, and inherits
    from classes Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a class object.

        Attributes
            size: size of square
            x: x axis offset
            y: y axis offset
            id: object id
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update class attributes"""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def __str__(self):
        """Returns a string representation of object"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Retrieve the value of size variable"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of size variable"""
        self.width = value
        self.height = value
