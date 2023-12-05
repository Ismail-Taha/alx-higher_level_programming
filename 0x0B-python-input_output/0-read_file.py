#!/usr/bin/python3
"""Defines a function to read and print a text file."""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as t:
        print(t.read(), end="")
