#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance of a class """
    if type(obj) == a_class:
        return True
    return False
