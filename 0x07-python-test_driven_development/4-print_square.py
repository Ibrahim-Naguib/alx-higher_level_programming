#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size: the size length of the square.

    Raises:
        TypeError: if size not an integer.
        ValueError: if size is less than 0.
        TypeError: if size is a float and is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
