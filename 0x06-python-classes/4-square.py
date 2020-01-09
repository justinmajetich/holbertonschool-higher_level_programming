#!/usr/bin/python3
"""Define a class Square with attributes"""


class Square:
    """Defines a class square"""
    def __init__(self, size=0):
        """Instantiates class object with size attribute

        Args:
            size: size of square

        Raises:
            TypeError: if size is not integer
            ValueError: if size is < 0
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Takes area of a square

        Returns:
            The area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """"""
        return self.__size

    @size.setter
    def size(self, value):
        """"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
