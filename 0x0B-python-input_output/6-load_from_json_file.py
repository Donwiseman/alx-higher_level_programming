#!/usr/bin/python3
"""Contains a function that creates an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """Deserializes a json file to a python object

    Args:
        filename (str): path name to JSON file

    Returns:
        A python object deserialized from the JSON file

    """
    with open(filename, 'r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile)
