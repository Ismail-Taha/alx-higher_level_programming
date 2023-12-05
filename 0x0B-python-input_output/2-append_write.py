#!/usr/bin/python3
"""Defines function appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""

    with open(filename, "a", encoding="utf-8") as t:
        return t.write(text)
