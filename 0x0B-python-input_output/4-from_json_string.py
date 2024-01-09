#!/usr/bin/python3
"""Define from json string function"""
import json


def from_json_string(my_str):
    """function returns an object represented by a JSON string

    Args:
       my_str: string to be converted.
    """
    return json.loads(my_str)
