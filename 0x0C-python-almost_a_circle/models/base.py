#!/usr/bin/python3
""" This defines the base class of this package named `Base` which helps
    maintains the id of various instances of the class and store/retrieve
    in JSON format.
"""

import json
import csv
import turtle


class Base(object):
    """ This defines the base class used in this package.

    This base class has 7 methods which help serialize and deserialize the
    various class instance to and from JSON format and CSV format.

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of class objects to csv format

        The method save the file to the current working directory as
        <class name>.csv

        Args:
            list_objs (list): list of class instances

        """
        rectangle_fields = ["id", "width", "height", "x", "y"]
        square_fields = ["id", "size", "x", "y"]
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "w", encoding="utf-8", newline='') as csv_file:
            if cls.__name__ == 'Rectangle':
                writer = csv.DictWriter(csv_file, fieldnames=rectangle_fields)
            else:
                writer = csv.DictWriter(csv_file, fieldnames=square_fields)
            writer.writeheader()
            if list_objs:
                for inst in list_objs:
                    writer.writerow(inst.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances for a given class from csv file

        Returns:
            returns a list of a given class instance loaded from csv file
        """
        file_name = "{}.csv".format(cls.__name__)
        list_objs = []
        try:
            with open(file_name, 'r', encoding='utf-8', newline='') as csv_fil:
                reader = csv.DictReader(csv_fil)
                for inst in reader:
                    real_dict = {}
                    for key, value in inst.items():
                        real_dict[key] = int(value)
                    list_objs.append(cls.create(**real_dict))
                return list_objs
        except Exception:
            return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Uses Turtle module to draw instances of Base class in a window

        Args:
            list_rectangles (list): List of rectangle classes to be drawn
            list_squares (list): List of square instances to be drawn

        """
        draw = turtle.Turtle()
        screen = draw.getscreen()
        screen.title("Welcome to the Base draw Window")
        if list_rectangles:
            for num, rect in enumerate(list_rectangles):
                screen.title("Drawing Rectangle {}".format(num))
                draw.penup()
                draw.goto(rect.x, rect.y)
                draw.pen(shown=False, pendown=True, pencolor="blue",
                         fillcolor="red", pensize=4, speed=4)
                for i in range(2):
                    draw.forward(rect.width)
                    draw.right(90)
                    draw.forward(rect.height)
                    draw.right(90)
                draw.reset()
        if list_squares:
            for num, sqr in enumerate(list_squares):
                screen.title("Drawing Square {}".format(num))
                draw.penup()
                draw.goto(sqr.x, sqr.y)
                draw.pen(shown=False, pendown=True, pencolor="blue",
                         fillcolor="red", pensize=4, speed=4)
                for i in range(4):
                    draw.forward(sqr.size)
                    draw.right(90)
                draw.reset()
        screen.bye()
