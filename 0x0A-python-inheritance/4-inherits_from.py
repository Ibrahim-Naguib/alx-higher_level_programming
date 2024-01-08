#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
           (directly or indirectly) from the specified class ; otherwise False
    Args:
       obj: The object to check.
       a_class: The class to match the type of obj to
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
