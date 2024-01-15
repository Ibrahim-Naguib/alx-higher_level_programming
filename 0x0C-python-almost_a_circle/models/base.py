#!/usr/bin/python3
"""Define Base class"""
import json


class Base:
    """the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
           id: The id of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.

        Args:
           list_dictionaries: A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
           list_objs: A list of inherited Base instances.
        """
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                new_list = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string.

        Args:
           json_string: string representing a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.

        Args:
           dictionary: like a double pointer to a dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(2, 4)
            else:
                dummy = cls(2)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from json file."""
        try:
            with open("{}.json".format(cls.__name__), "r",
                      encoding="utf=8") as f:
                new_list = Base.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in new_list]
        except FileNotFoundError:
            return []
