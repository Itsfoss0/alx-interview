#!/usr/bin/env python3

"""
unittest for the interview question
"""

from unittest import TestCase
import triangle


class TestTriangle(TestCase):
    """
    Test suites for the function
    """

    def test_function_documenation(self):
        """
        Esure the function is well documented
        """
        self.assertIsNotNone(triangle.pascal_triangle.__doc__)

    def test_module_documentation(self):
        """
        Esure the module is well documented
        """
        self.assertIsNotNone(triangle.__doc__)

    def test_input_exceptions(self):
        """
        Esure the function raises the exception
        """
        with self.assertRaises(TypeError):
            triangle.pascal_triangle("taylorshow")
            triangle.pascal_triangle("Jane Doe")
            triangle.pascal_triangle({"show": "blindspot"})
