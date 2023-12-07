#!/usr/bin/python3

"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """add text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    txt = ""
    with open(filename) as f:
        for lin in f:
            txt += lin
            if search_string in lin:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
