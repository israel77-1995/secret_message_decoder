import unittest
from message_decoder import *

class TestMessageDecoder(unittest.TestCase):
    def test_fetch_data(self):
        #Test with valid URL
        url = "https://jsonplaceholder.typicode.com/posts"
        data = fetch_data(url)
        self.assertIsNotNone(data, "Data can not be None")
        self.assertIsInstance(data, str, "Data should be a string")
        self.assertGreater(len(data), 0, "Data should not be empty")
        

    def test_fetch_data_invalid_url(self):
        #Test with invalid URL
        url = "https://invalid-url"
        data = fetch_data(url)
        self.assertIsNone(data, "Data should be None for invalid URL")

    def test_fetch_data_non_json(self):
        #Test with non-JSON response
        url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
        data = fetch_data(url)
        self.assertIsNotNone(data, "Data can not be None")
        self.assertIsInstance(data, str, "Data should be a string")
        self.assertGreater(len(data), 0, "Data should not be empty")

    def test_parse_data(self):
        #Test with valid Google document URL
        url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
        data = fetch_data(url)
        parsed_data = parse_data(data)
        self.assertIsNotNone(parsed_data, "Parsed data can not be None")
        self.assertIsInstance(parsed_data, list, "Parsed data should be a list")
        self.assertGreater(len(parsed_data), 0, "Parsed data should not be empty")

    def test_parse_triplet_data(self):
        parsed_data = ['0', '█', '0', '0', '█', '1', '0', '█', '2', '1', '▀', '1', '1', '▀', '2', '2', '▀', '1', '2', '▀', '2', '3', '▀', '2']
        expected = [(0, 0, '█'), (0, 1, '█'), (0, 2, '█'), (1, 1, '▀'), (1, 2, '▀'), (2, 1, '▀'), (2, 2, '▀'), (3, 2, '▀')]
        result = parse_triplet_data(parsed_data)
        self.assertEqual(result, expected, "Parsed triplet data does not match expected output")

    def test_grid_builder(self):
        triplets = [(0, 0, '█'), (0, 1, '█'), (0, 2, '█'), (1, 1, '▀')]
        expected = [
    ['█', ' '],
    ['█', '▀'],
    ['█', ' '],

]

        result = grid_builder(triplets)
        self.assertEqual(result, expected, "Grid builder output does not match expected output")

    