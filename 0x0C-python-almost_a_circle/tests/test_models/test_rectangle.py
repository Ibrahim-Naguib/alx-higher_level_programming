#!/usr/bin/python3
"""Define unittests for rectangle.py"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Define unittests for Rectangle class"""

    def test_rectangle_id(self):
        """Test if the rectangle id is assigned correctly"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 16)
        self.assertEqual(r2.id, 17)

    def test_rectangle_width(self):
        """Test if the rectangle width is assigned correctly"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)

    def test_width_not_int(self):
        """Test if TypeError is raised when width is not an integer"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_width_negative(self):
        """Test if ValueError is raised when width is negative"""
        with self.assertRaisesRegex(ValueError, "width must be >= 0"):
            Rectangle(-10, 2)

    def test_rectangle_height(self):
        """Test if the rectangle height is assigned correctly"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 10)

    def test_height_not_int(self):
        """Test if TypeError is raised when height is not an integer"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_height_negative(self):
        """Test if ValueError is raised when height is negative"""
        with self.assertRaisesRegex(ValueError, "height must be >= 0"):
            Rectangle(10, -2)

    def test_rectangle_x(self):
        """Test if the rectangle x-coordinate is assigned correctly"""
        r1 = Rectangle(10, 2, 3)
        r2 = Rectangle(2, 10, 3)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r2.x, 3)

    def test_x_not_int(self):
        """Test if TypeError is raised when x is not an integer"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")

    def test_x_negative(self):
        """Test if ValueError is raised when x is negative"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_rectangle_y(self):
        """Test if the rectangle y-coordinate is assigned correctly"""
        r1 = Rectangle(10, 2, 3, 4)
        r2 = Rectangle(2, 10, 3, 4)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r2.y, 4)

    def test_y_not_int(self):
        """Test if TypeError is raised when y is not an integer"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")

    def test_y_negative(self):
        """Test if ValueError is raised when y is negative"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -4)

    def test_rectangle_area(self):
        """Test if the rectangle area is calculated correctly"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 20)

    def test_update_args(self):
        """Test the update method with positional arguments"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_kwargs(self):
        """Test the update method with keyword arguments"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/1", str(r))

        r.update(width=1, x=2)
        self.assertEqual("[Rectangle] (10) 2/10 - 1/1", str(r))

        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Rectangle] (89) 3/1 - 2/1", str(r))

        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_to_dict(self):
        """Test the to_dictionary method"""
        r = Rectangle(10, 2, 1, 9)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, {'x': 1, 'y': 9, 'id': 24,
                                  'height': 2, 'width': 10})


if __name__ == "__main__":
    unittest.main()
