#!/usr/bin/python3

"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """add text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    t = ""
    with open(filename) as f:
        for l in f:
            t += l
            if search_string in l:
                t += new_string
    with open(filename, "w") as w:
        w.write(t)
