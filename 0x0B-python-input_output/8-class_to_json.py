#!/usr/bin/python3
"""Returns a dictionary containing a class attributes and description"""


def class_to_json(obj):
    """Returns a dict decription of a class based on it's attributes

    Args:
        obj: instance of a class

    Returns:
        Dictionary representing a decription of the class based on Attr

    """
    return obj.__dict__
