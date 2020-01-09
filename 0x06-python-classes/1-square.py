#!/usr/bin/python3
"""Creates a class with size instance attribute"""


class Square:
    """This class defines a square by size"""
    def __init__(self, __size=0):
        """Instantiates a class object with size attribute

        Attributes:
            __size: size of square
        """
        self.__size = __size
