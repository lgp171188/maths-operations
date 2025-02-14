"""
This module contains the unit tests for the mathematical operations
implemented in operations.py
"""

import unittest

from operations import add


class TestOperations(unittest.TestCase):
    """
    Tests for the mathematical operations.
    """
    def test_add_integers(self):
        """
        Test that the add() function can add two integers.
        """
        result = add(1, 2)
        self.assertEqual(result, 3)
