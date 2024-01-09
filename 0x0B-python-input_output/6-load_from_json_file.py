#!/usr/bin/python3
"""Define load from json file function"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”:

    Args:
       filename: file to write from.
    """
    with open(filename) as f:
        return json.load(f)
