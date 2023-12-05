#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Returns:
        True If obj is an inherited instance of a_class.
        Otherwise - False.
    """

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
