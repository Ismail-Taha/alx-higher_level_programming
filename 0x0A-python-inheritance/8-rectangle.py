#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """contains a rectangle using BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
