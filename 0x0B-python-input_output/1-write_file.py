#!/usr/bin/python3
"""Defines a function for writing a string to a text file."""


def write_file(filename="", text=""):
    """writes a string to a text file using (UTF8)"""

    with open(filename, "w", encoding="utf-8") as t:
        return t.write(text)
