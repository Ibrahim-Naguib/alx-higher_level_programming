#!/usr/bin/python3
"""Define base_geometry class"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Not implemented area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value

        Args:
           name: name to check
           value: value to validate

        Raises:
           TypeError: if value is not an integer
           ValueError: if value is less or equal than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
