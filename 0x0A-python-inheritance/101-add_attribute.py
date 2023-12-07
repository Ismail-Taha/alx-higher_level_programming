#!/usr/bin/python3

"""Defines a function that adds attributes to objects."""


def add_attribute(obj, atrb, val):
    """Add attribute to an object if possible.
    Args:
        obj (any): The object to add an attribute to.
        atrb (str): The name of the attribute to add to obj.
        val (any): The value of atrb.
    Raises:
        TypeError: If the attribute can't be added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atrb, val)
