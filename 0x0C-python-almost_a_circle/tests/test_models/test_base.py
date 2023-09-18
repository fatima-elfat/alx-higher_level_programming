#!/usr/bin/python3
"""
Unittest for Base Class
"""


import os
import unittest
from models import base
from models import rectangle
from models import square
import pep8
Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square

class TestPep8(unittest.TestCase):
    """
    Pep8 PEP 8 validated"""
    def test_pep8(self):
        """
        tests pep8.
        """
        a = 0
        b = pep8.StyleGuide(quiet=False)
        files = ["models/base.py", "tests/test_models/test_base.py"]
        a += b.check_files(files).total_errors
        self.assertEqual(a, 0, 'Try and fix Pep8')

class TestBase(unittest.TestCase):
    """
    tests fo Class Base in models/base.py.
    """
    def test_no_arg(self):
        a1 = Base()
        a2 = Base()
        self.assertEqual(a1.id, a2.id - 1)

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            Base(20, 20)

    def test_None_id(self):
        a1 = Base(None)
        a2 = Base(None)
        self.assertEqual(a1.id, a2.id - 1)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(23).__nb_instances)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)
        self.assertEqual(float('inf'), Base(float('inf')).id)
        self.assertEqual("Heeey", Base("Heeey").id)
        self.assertEqual(b'Heeey', Base(b'Heeey').id)
        self.assertEqual(1.2, Base(1.2).id)
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)
        self.assertEqual(True, Base(True).id)
        self.assertEqual((1, 2), Base((1, 2)).id)
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)
        self.assertEqual(complex(5), Base(complex(5)).id)
        self.assertEqual(range(5), Base(range(5)).id)

    def test_json_(self):
        b1 = Rectangle(6, 5, 4, 3, 2)
        b2 = Rectangle(1, 2, 7, 1, 4)
        c1 = Square(5, 4, 3, 2)
        self.assertEqual(str, type(Base.to_json_string([b1.to_dictionary()])))
        self.assertTrue(len(Base.to_json_string([b1.to_dictionary()])) == 20)
        list_dicts = [b1.to_dictionary(), b2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 85)
        self.assertEqual(str, type(Base.to_json_string([c1.to_dictionary()])))
        self.assertTrue(len(Base.to_json_string([c1.to_dictionary()])) == 20)
