#!/usr/bin/env python3

"""
unittest for the interview question
"""

from unittest import TestCase
from  triangle import pascal_triangle

class TestTriangle(TestCase):
    """
    Test suites for the function
    """

    def test_documenation(self):
        self.assertIsNotNone(pascal_triangle.__doc__)

    def test_inputs(self):
        with self.assertRaises(TypeError):
            pascal_triangle("taylorshow")