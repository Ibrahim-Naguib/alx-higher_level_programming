#!/usr/bin/python3
"""Define unittests for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseInstantiation(unittest.TestCase):
    """Define unittests for Base instantiation"""

    def test_noargs(self):
        """Test Base instantiation without arguments"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_withargs(self):
        """Test Base instantiation with arguments"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)


class TestBaseToJsonString(unittest.TestCase):
    """Define unittests for Base to_json_string"""

    def test_to_json_string(self):
        """Test converting Base object to JSON string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected = '[{"id": 3, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_dictionary, expected)

    def test_to_json_none(self):
        """Test converting None to JSON string"""
        json_dictionary = Base.to_json_string(None)
        expected = []
        self.assertEqual(json_dictionary, expected)

    def test_to_json_empty(self):
        """Test converting empty list to JSON string"""
        json_dictionary = Base.to_json_string([])
        expected = []
        self.assertEqual(json_dictionary, expected)


class TestRectangleFromJsonString(unittest.TestCase):
    """Define unittests for Rectangle from_json_string"""

    def test_from_json_string(self):
        """Test converting JSON string to list of dictionaries"""
        list_input = [
          {'id': 89, 'width': 10, 'height': 4},
          {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_from_json_string_none(self):
        """Test converting None to empty list"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty(self):
        """Test converting empty string to empty list"""
        list_output = Rectangle.from_json_string("")
        self.assertEqual(list_output, [])


class TestRectangleSaveToFile(unittest.TestCase):
    """Define unittests for Rectangle save_to_file"""

    def test_save_to_file(self):
        """Test saving Rectangle objects to file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(Rectangle.from_json_string
                                 (f.read())), 2)

    def test_save_to_file_None(self):
        """Test saving None to file"""
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as f:
            self.assertEqual(Rectangle.from_json_string
                             (f.read()), [])


class TestRectangleCreate(unittest.TestCase):
    """Define unittests for Rectangle create"""

    def test_create(self):
        """Test creating Rectangle object from dictionary"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (4) 1/0 - 3/5", str(r1))
        self.assertEqual("[Rectangle] (4) 1/0 - 3/5", str(r2))


class TestRectangleLoadFromFile(unittest.TestCase):
    """Define unittests for Rectangle load_from_file"""

    def test_load_from_file(self):
        """Test loading Rectangle objects from file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)

    def test_file_not_found(self):
        """Test loading from a non-existent file"""
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 0)


if __name__ == "__main__":
    unittest.main()
