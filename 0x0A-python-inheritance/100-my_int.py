#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """class MyInt inherits from int"""

    def __eq__(self, other):
        """Override == operator to invert behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator to invert behavior."""
        return super().__eq__(other)
