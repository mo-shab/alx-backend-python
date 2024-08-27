#!/usr/bin/env python3
"""Unitest for utils"""

from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Dict

import unittest


access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class Test Access Nested Map.
    Inhereat from unittest.TestCase
    """
    @parameterized.expand(
        [
            ({"a": 1}, ["a", ], 1),
            ({"a": {"b": 2}}, ["a", ], {'b': 2}),
            ({"a": {"b": 2}}, ["a", "b"], 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        """Methode test of access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
            [
                ({}, ["a", ]),
                ({"a": 1}, ["a", "b"]),
            ]
    )
    def test_access_nested_map_exception(self, nested_map, path) -> None:
        """Methode test exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class for Test Get JSON methods"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://http://holberton.io", {"payload": False}),
    ])

    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Tests `get_json`'s output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            """Test Memoize methode"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method", return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
