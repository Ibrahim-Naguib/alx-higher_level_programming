#!/usr/bin/python3
"""Define add_attribute function"""


def add_attribute(cls, name, value):
    """function that adds a new attribute to an object if it’s possible
    Args:
       cls: The class to add attr.
       name: The attr name
       value: The attr value

    Args:
       TypeError: if the attribute exists.
    """
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
