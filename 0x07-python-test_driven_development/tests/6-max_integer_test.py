#!/usr/bin/python3
"""Unittest for 6-max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """run tests uni test """

    def test_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_function_docstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_positive(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([1, 2, 3, -4]), 5)
        self.assertEqual(max_integer([-1.5, -2.5]), -3.5)
        self.assertEqual(max_integer([10, -10, 10]), 10)

    def test_list_of_strings(self):
        self.assertEqual(max_integer("8899"), '9')
        self.assertEqual(max_integer("abc"), 'c')
        self.assertEqual(max_integer(['x', 'y', 'z']), 'z')

    def test_others(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2}, {3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
