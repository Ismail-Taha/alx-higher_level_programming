#!/usr/bin/python3
""" Module that contains class Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ define class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square.

         Args:
            size (int): The size of the Square.
            x (int): The x coordinate of the Square.
            y (int): The y coordinate of the Square.
            id (int): The identity of the Square.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """str special method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Update Square."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
