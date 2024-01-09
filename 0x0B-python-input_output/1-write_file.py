#!/usr/bin/python3
"""Define write file function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)

    Args:
       filename (str): The name of the file to write.
       text (str): The text to write to the file.

    Returns:
       The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
