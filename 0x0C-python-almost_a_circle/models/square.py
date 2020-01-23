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

    def __str__(self):
        """Returns a string representation of object"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)
