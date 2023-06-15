#!/usr/bin/python3
"""This contains a function that writes an Object to a text file in JSON"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to be serialized
        filename (str): pathname to file to store serialized data

    """
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(my_obj, jsonfile)
