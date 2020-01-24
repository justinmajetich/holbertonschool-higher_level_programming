#!/usr/bin/python3
"""This module defines a class, Base.
"""


import json


class Base:
    """This class, Base, provides a base class for
    future classes.

    Attributes
        __nb_objects: count of class instantiations
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instatiates class object with id.

        Arguments
            id: object id
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation or argument

        Arguments
            list_dictionaries: a list of dictionaries
        """
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)
