#!/usr/bin/python3
"""Say my name module"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>

    Args:
        first_name: the first name to be printed.
        last_name: the second name to be printed

    Raises:
        TypeError: if names are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
