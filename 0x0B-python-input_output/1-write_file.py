#!/usr/bin/python3
"""Contains a function that writes a string to the current working directory"""


def write_file(filename="", text=""):
    """Writes a given text to the provided file

    Args:
        filename (str, optional): file path to required file
        text (str, optional): text to be written

    Returns:
        return the number of characters written

    """
    with open(filename, 'w', encoding='utf-8') as file_write:
        for line in text:
            file_write.write(line)
        return file_write.tell()
