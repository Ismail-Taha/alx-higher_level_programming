#!/usr/bin/python3
""" This module defines a Square class. """


class Square:
    """
    Square: A geometric square.

    Attributes:
        __size: The size of the square.

    Methods:
        __init__: Initializes the size attribute for each instance.
    """

    def __init__(self, size):
        """
        Initializes attributes for instances.

        Args:
            size: The size of the square.
        """
        self.__size = size
