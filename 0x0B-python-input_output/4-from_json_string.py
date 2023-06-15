#!/usr/bin/python3
"""Contains a function that returns an object from a json string"""

import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): JSON string

    Returns:
        return a python object from the string

    """
    return json.loads(my_str)
