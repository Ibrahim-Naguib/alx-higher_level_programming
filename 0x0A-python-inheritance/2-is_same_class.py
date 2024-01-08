#!/usr/bin/python3
"""Define is_same_class function"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance
            of the specified class otherwise False
    Args:
       obj: The object to check.
       a_class: The class to match the type of obj to
    """
    if type(obj) == a_class:
        return True
    else:
        return False
