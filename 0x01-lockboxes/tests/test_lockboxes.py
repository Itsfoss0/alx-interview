#!/usr/bin/env python3

"""
This module  contains unit test for
the lockboxes inteview question
"""

from unittest import TestCase
from unlock_boxes import canUnlockAll


class TestUnlockBoxes(TestCase):

    def test_function_docs(self):
        """
        function well documented?
        """
        self.assertIsNotNone(canUnlockAll.__doc__)

    def test_function_annotations(self):
        """
        Type hinting can be a good thing
        """
        self.assertTrue(bool(canUnlockAll.__annotations__))

    def test_functionality(self):
        self.assertTrue(canUnlockAll([[1], [2], [3], [4], []]))
        self.assertTrue(canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]))
        self.assertFalse(canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]))
        with self.assertRaises(TypeError):
            canUnlockAll("Sherlock Holmes")
