#!/usr/bin/python3
"""Define append write function"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)

    Args:
       filename (str): The name of the file to write.
       text (str): The text to write to the file.

    Returns:
       The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
