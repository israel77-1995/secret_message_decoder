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
        url = "https://www.example.com"
        data = fetch_data(url)
        self.assertIsNotNone(data, "Data can not be None")
        self.assertIsInstance(data, str, "Data should be a string")
        self.assertGreater(len(data), 0, "Data should not be empty")

    def test_parse_data(self):
        #Test with valid Google document URL
        url = "https://docs.google.com/document/d/1n3v1x4Q8k8k8k8k8k8/edit"
        data = fetch_data(url)
        parsed_data = parse_data(data)
        self.assertIsNotNone(parsed_data, "Parsed data can not be None")
        self.assertIsInstance(parsed_data, str, "Parsed data should be a string")
        self.assertGreater(len(parsed_data), 0, "Parsed data should not be empty")
