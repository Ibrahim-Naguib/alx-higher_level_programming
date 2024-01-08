#!/usr/bin/python3
"""Define is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object
            is an instance of a class that inherited from, the
            specified class ; otherwise False
    Args:
       obj: The object to check.
       a_class: The class to match the type of obj to
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
