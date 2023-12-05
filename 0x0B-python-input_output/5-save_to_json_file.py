#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, use JSON representation"""
    with open(filename, "w") as t:
        json.dump(my_obj, t)
