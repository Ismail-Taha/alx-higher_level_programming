#!/usr/bin/python3
""" module for base class."""


class Base:
    """Represent the base module.
    Represents the "base" for all other classes in project 0x0C."""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
