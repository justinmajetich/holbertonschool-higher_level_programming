#!/usr/bin/python3
"""This module defines a class, BaseGeometry"""


class BaseGeometry:
    """A class defining a geometric shape"""

    def area(self):
        """Take area of shape"""
        raise Exception('area() is not implemented')
