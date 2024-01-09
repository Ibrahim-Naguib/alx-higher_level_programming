#!/usr/bin/python3
"""Define to json string function"""
import json


def to_json_string(my_obj):
    """function returns the JSON representation of an object

    Args:
       my_obj: object to be converted.
    """
    return json.dumps(my_obj)
