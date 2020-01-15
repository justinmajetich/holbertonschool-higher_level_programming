#!/usr/bin/python3
"""This module defines a class, rectangle"""


class Rectangle:
    """Defines a rectangle by height/wdith

    Attributes:
        numer_of_instances: tracks the number of class instances
        print_symbol: chr to print in rectangle representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiates class object

        Attributes:
            width: rectangle width (private)
            height: rectangle height (private)
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Delete instance"""
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.width is 0 or self.height is 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles by area"""
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new class instance"""
        return cls(size, size)

    def __str__(self):
        """String representation of class object"""
        if self.width is 0 or self.height is 0:
            return ''
        else:
            return (((str(self.print_symbol) * self.width) + '\n'
                     ) * self.height)[:-1]

    def __repr__(self):
        """Code representation of instance"""
        return 'Rectangle({}, {})'.format(self.width, self.height)

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
