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
        f = "{}.json".format(cls.__name__)
        with open(f, "w", encoding='utf-8') as save_file:
            save_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns a list object from the JSON string representation:

        Args:
            json_string (str): JSON string to be converted to respective object

        Returns:
            An object (likely a list) from the JSON string
        """
        list_dict = None
        if json_string:
            list_dict = json.loads(json_string)
        else:
            list_dict = []
        return list_dict

    @classmethod
    def create(cls, **dictionary):
        """returns an class instance with all attributes already set

        Args:
            dictionary (dict): dictionary conatining attributes of the instance

        Returns:
            A class instance with attributes same as that of the dictionary
        """
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        else:
            inst = cls(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances for a given class from file

        Returns:
            returns a list of a given class instance loaded from file
        """
        file_name = "{}.json".format(cls.__name__)
        list_objs = []
        try:
            with open(file_name, 'r', encoding='utf-8') as json_list:
                json_string = json_list.read()
                list_dict = Base.from_json_string(json_string)
                for inst in list_dict:
                    list_objs.append(cls.create(**inst))
                return list_objs
        except Exception:
            return list_objs
