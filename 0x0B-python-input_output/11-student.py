#!/usr/bin/python3
"""Define a student class"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
           first_name: The first name of the student.
           last_name: The last name of the student.
           age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
           attrs: The attributes to represent.
        """
        if isinstance(attrs, list) and (isinstance(i, str) for i in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json: The key/value pairs to replace attributes with.
        """
        for i, j in json.items():
            setattr(self, i, j)
