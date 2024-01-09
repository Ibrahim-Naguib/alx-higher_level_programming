#!/usr/bin/python3
"""Define save to json file function"""
import json


def save_to_json_file(my_obj, filename):
    """function writes an Object to a text file, using a JSON representation

    Args:
       my_obj: object to write from.
       filename: file to write to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
