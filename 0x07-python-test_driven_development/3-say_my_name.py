#!/usr/bin/python3
""" This module contains a function that prints the first and last name

Testing of this function is done via docfile in tests/3-say_my_name.txt

"""


def say_my_name(first_name, last_name=""):
    """ prints My name is <first name> <last name>

    Args:
        first_name (str): first name of a given individual
        last_name (str): last name of given individual

    Raises:
        TypeError: if arguments are not strings

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
