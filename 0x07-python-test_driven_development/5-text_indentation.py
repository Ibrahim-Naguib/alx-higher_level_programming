#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these chars: ., ? and :

    Args:
        text: the string to add chars to.

    Raises:
        TypeError: if the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    line = ''

    for i in text:
        line += i
        if i in chars:
            print(line.strip(" "), end="")
            line = ''
            print('\n')
    if line:
        print(line.strip(" "))
