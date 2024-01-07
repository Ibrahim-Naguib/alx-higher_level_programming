#!/usr/bin/python3
"""Add integer module"""


def add_integer(a, b=98):
    """Function Adds two integers

    Args:
        a: first number.
        b: second number.

    Raises:
        TypeError: if a or b not integers.

    Returns:
        The sum of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
