#!/usr/bin/python3
""" module for base class."""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file."""
        f_name = cls.__name__ + ".json"
        with open(f_name, "w") as json_f:
            if list_objs is None:
                json_f.write("[]")
            else:
                list_dict = [ob.to_dictionary() for ob in list_objs]
                json_f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_inst = cls(1, 1)
            else:
                new_inst = cls(1)
            new_inst.update(**dictionary)
            return new_inst


    @classmethod
    def load_from_file(cls):
        """Return a list of classes from a file of JSON strings."""
        f_name = str(cls.__name__) + ".json"
        try:
            with open(f_name, "r") as json_f:
                list_dict = Base.from_json_string(json_f.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
