#!/usr/bin/python3
"""Define read file function"""


def read_file(filename=""):
    """function that reads a file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
