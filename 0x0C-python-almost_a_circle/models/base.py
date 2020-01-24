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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON representation to file.

        The method first converts the objects passed
        into dictionary representations of themselves
        using the to_dictionary method included in all
        Base subclasses. These dictionaries are stored
        in a temp list, converted to JSON strings and
        returned.

        Arguments
            list_objs: list of subclass instances
        """
        if not list_objs:  # if empty/None, save empty list
            list_objs = []

        dict_list = []
        for obj in list_objs:  # convert objs to dicts
            dict_list.append(obj.to_dictionary())

        with open((cls.__name__ + '.json'), mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dict_list))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of a class with
        attributes already initialized.

        Argument:
            dictionary: a dictionary representation of an object
        """
        new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation or argument

        Arguments
            list_dictionaries: a list of dictionaries
        """
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return Python object from JSON string.

        Argument:
            json_string: string representation of list of dicts
        """
        if not json_string:
            return []
        return json.loads(json_string)
