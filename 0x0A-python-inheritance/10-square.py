#!/usr/bin/python3
"""Define Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """creates a new square

        Args:
           size: square size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        super().__str__()
