#!/usr/bin/env python3
"""Unitest for utils"""

from parameterized import parameterized
from unittest.mock import patch, Mock

import unittest


access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


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
    def test_access_nested_map(self, nested_map, path, expected):
        """Methode test of access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
            [
                ({}, ["a", ]),
                ({"a": 1}, ["a", "b"]),
            ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        """Methode test exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class for Test Get JSON methods"""
    @patch('requests.get')
    def test_get_json(self, mock_get):
        """Methode to test get_json method"""

        # Define the test Cases.
        test_cases = [
            {"test_url": "http://example.com", "test_payload":
             {"payload": True}},
            {"test_url": "http://holberton.io", "test_payload":
             {"payload": False}},
        ]
        for case in test_cases:
            test_url = case['test_url']
            test_payload = case['test_payload']

            # Set up the Mock response object with the desired json output
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function with the test URL
            result = get_json(test_url)

            # Assert that the function returns the correct payload
            self.assertEqual(result, test_payload)

            # Assert that the correct URL was used in the GTE request
            mock_get.assert_called_once_with(test_url)

            # Reset the mock for the next iteration
            mock_get.reset_mock()
