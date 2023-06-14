#!/usr/bin/python3
"""Has a single function that returns the JSON representation of an object"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object in string format

    Args:
        my_obj (obj): given object to be serialized

    Returns:
        JSON string representation of the object

    """
    return json.dumps(my_obj, sort_keys=True)
