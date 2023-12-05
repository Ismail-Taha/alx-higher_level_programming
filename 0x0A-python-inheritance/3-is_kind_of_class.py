#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Returns:
        True If obj is an instance or inherited instance of a_class.
        Otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
