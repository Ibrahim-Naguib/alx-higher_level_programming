#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """define unittest for max_integer([..])"""

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_unordered_list(self):
        self.assertEqual(max_integer([3, 4, 5, 2, 1]), 5)

    def test_negative_list(self):
        self.assertEqual(max_integer([-2, -3, -1, -4, -5]), -1)

    def test_dup_list(self):
        self.assertEqual(max_integer([1, 5, 2, 3, 2, 4, 4]), 5)


if __name__ == "__main__":
    unittest.main()
