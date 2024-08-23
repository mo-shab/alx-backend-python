#!/usr/bin/env python3
"""Unitest for utils"""

from parameterized import parameterized

import unittest

access_nested_map = __import__('utils').access_nested_map



class TestAccessNestedMap(unittest.TestCase):
    """Class Test Access Nested Map.
    Inhereat from unittest.TestCase
    """
    @parameterized.expand(
        [
            ({"a" : 1}, {"a",}, 1),
            ({"a": {"b": 2}}, {"a",}, {'b': 2}),
            ({"a": {"b": 2}}, {"a", "b"}, 2),
        ])

    def test_access_nested_map(self, nested_map, path, expected):
        """Methode test of access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == '__main__': 
    unittest.main() 