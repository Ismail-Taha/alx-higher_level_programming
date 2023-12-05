#!/usr/bin/python3
"""Defines the BaseGeometry class"""


class BaseGeometry:
    """Base class for geometry objects"""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name
            value (int): int
			 """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

