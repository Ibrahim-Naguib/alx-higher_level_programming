#!/usr/bin/python3
"""Define unittests for square.py"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Define unittests for Square class"""

    def test_square_id(self):
        """Test the id attribute of Square objects"""
        s1 = Square(10)
        s2 = Square(10, 2)
        s3 = Square(10, 2, 3)
        s4 = Square(10, 2, 3, 4)
        self.assertEqual(s1.id, 25)
        self.assertEqual(s2.id, 26)
        self.assertEqual(s3.id, 27)
        self.assertEqual(s4.id, 4)

    def test_square_size(self):
        """Test the size attribute of Square objects"""
        s1 = Square(10)
        s2 = Square(10, 2)
        s3 = Square(10, 2, 3)
        s4 = Square(10, 2, 3, 4)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s4.size, 10)

    def test_size_not_int(self):
        """Test that a TypeError is raised when size is not an integer"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")

    def test_size_negative(self):
        """Test that a ValueError is raised when size is negative"""
        with self.assertRaisesRegex(ValueError, "width must be >= 0"):
            Square(-10)

    def test_str(self):
        """Test the __str__ method of Square objects"""
        s1 = Square(10, 2, 3, 4)
        s2 = Square(10, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (4) 2/3 - 10")
        self.assertEqual(s2.__str__(), "[Square] (4) 2/3 - 10")

    def test_update_args(self):
        """Test the update method of Square objects"""
        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s1))

        s1.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s1))

        s1.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s1))

        s1.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s1))

        s1.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s1))

    def test_square_kwargs(self):
        """Test the update method of Square objects with keyword arguments"""
        s1 = Square(10, 10, 10, 10)
        s1.update(id=89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s1))

        s1.update(size=1)
        self.assertEqual("[Square] (89) 10/10 - 1", str(s1))

        s1.update(x=2)
        self.assertEqual("[Square] (89) 2/10 - 1", str(s1))

        s1.update(y=3)
        self.assertEqual("[Square] (89) 2/3 - 1", str(s1))

        s1.update(id=89, size=1, x=2, y=3)
        self.assertEqual("[Square] (89) 2/3 - 1", str(s1))

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square objects"""
        s1 = Square(10, 2, 3, 4)
        self.assertEqual(s1.to_dictionary(), {'id': 4, 'size': 10,
                                              'x': 2, 'y': 3})
