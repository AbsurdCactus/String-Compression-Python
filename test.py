import unittest
import main

class TestMain(unittest.TestCase):

    def test_aabcccccaaa(self):
        self.assertEqual(main.string_compresser(
            given_string = "aabcccccaaa"
        ), "a2b1c5a3")