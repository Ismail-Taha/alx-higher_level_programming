#!/usr/bin/python3

"""Defines a function that adds attributes to objects."""


def add_attribute(obj, atrb, val):

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atrb, val)
