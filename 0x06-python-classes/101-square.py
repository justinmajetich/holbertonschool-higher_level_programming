#!/usr/bin/python3
"""Define a class Square with attributes"""


class Square:
    """Defines a class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiates class object with size attribute

        Args:
            size: size of square
            position: xy position of square
        """
        self.size = size
        self.position = position

    def my_print(self):
        """Print square with # characters"""
        if self.__size == 0:
            print('')
        else:
            for y in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for x in range(self.__position[0]):
                    print('', end=' ')
                for col in range(self.__size):
                    print('#', end='')
                print('')

    def area(self):
        """Takes area of a square

        Returns:
            The area of a square
        """
        return self.__size ** 2

    def __str__(self):
        if self.__size is 0:
            return ''
        else:
            return '{}'.format('\n' * self.__position[1] +
                               ((' ' * self.__position[0] +
                                ('#' * self.__size + '\n')
                                 ) * self.__size))[:-1]

    @property
    def size(self):
        """Gets value of size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value of size attribute

        Raises:
            TypeError: if size is not integer
            ValueError: if size is < 0
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Gets value of position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets value of position attribute

        Raises:
            TypeError: if value is not tuple of two positive integers
        """
        emess = 'position must be a tuple of 2 positive integers'
        if type(value) is not tuple:
            raise TypeError(emess)
        if len(value) is not 2:
            raise TypeError(emess)
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError(emess)
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError(emess)
        self.__position = value
