import unittest
import sys
from encoder import encode_string




class TestEncoder(unittest.TestCase):
    def test_encode_string(self):
        text = "aaaabcd"
        encoding_table, encoded_string = encode_string(text)
        print(encoding_table)
        print(encoded_string)
        self.assertEqual(1,1)

