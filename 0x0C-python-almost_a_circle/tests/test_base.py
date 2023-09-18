#!/usr/bin/python3
"""
Unittest for Base Class
"""


import os
import unittest
from models import base
from models import rectangle
import pep8
Base = base.Base
Rectangle = rectangle.Rectangle


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
        a += b.check_files(files).total_a
        self.assertEqual(a, 0, 'Try and fix Pep8')

class TestBase(unittest.TestCase):
    """
    tests fo Class Base in models/base.py.
    """
    def test_no_arg(self):
        a1 = Base()
        a2 = Base()

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
