#!/usr/bin/python3
"""Define a class Square with attributes"""


class Square:
    """This class defines a square by size"""
    def __init__(self, size=0):
        """Instantiates class object with attribute

        Attributes:
           __size: size of square
        """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
