#!/usr/bin/python3
""" This defines the base class of this package named `Base` which helps
    maintains the id of various instances of the class and store/retrieve
    in JSON format.
"""

import json


class Base(object):
    """ This defines the base class used in this package.

    This base class has 5 mthods which help serialize and deserialize the
    various class instance to and from JSON format.

    Attributes:
        id (int): the id of the class intance.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates the Base class

        Args:
            id (int, optional): the specific id for the class instance

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries.

        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        This taks a lists of instances of same class that inherits from Base
        and save the information in JSON format in the current working
        directory as <Class name>.json

        Args:
            list_objs (list): list of instances who inherits of Base

        """
        list_dict = []
        if list_objs:
            for inst in list_objs:
                list_dict.append(inst.to_dictionary())
        json_str = Base.to_json_string(list_dict)
        with open("{}.json".format(cls.__name__), "w") as save_file:
            save_file.write(json_str)
