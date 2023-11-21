#!/usr/bin/python3
""" Module containing the Square class. """

class Square:
    """
    Square: Defines a square.
    Attributes:
        size (int): Size of a square.
    Methods:
        __init__: Initializes the size for each instance.
        area: Returns the area of the square.
    """

    def __init__(self, size=0):
        """ Initializes attributes for instances.
        Args:
            size (int): Size of the square.
        """
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """ Returns the area of the square. """
        return self.__size ** 2
