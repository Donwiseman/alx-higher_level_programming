#!/usr/bin/python3
"""Has a Class called Student which defines a student"""


class Student:
    """Defines the student class

    Class is instantiated with its attribute and has a function which


    Attributes:
        first_name (str): Student first name
        last_name (str): student last name
        age (int): student age

    """
    def __init__(self, first_name, last_name, age):
        """Instantiates the class

        Args:
            first_name (str): Student first name
            last_name (str): student last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dict representation containing class attributes"""
        return self.__dict__
