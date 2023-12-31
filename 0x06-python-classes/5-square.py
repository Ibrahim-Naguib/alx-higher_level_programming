#!/usr/bin/python3

"""define Class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):

        """Initialize a new Square

        Args:
            size (int): The square size

        """
        self.__size = size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
