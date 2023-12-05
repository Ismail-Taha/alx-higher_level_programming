#!/usr/bin/python3
"""Defines a function to read a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file."""
    with open(filename) as o:
        return json.load(o)
