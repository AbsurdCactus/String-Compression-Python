import unittest
import main

class TestMain(unittest.TestCase):

    def test_aabcccccaaa(self):
        self.assertEqual(main.string_compresser(
            given_string = "aabcccccaaa"
        ), "a2b1c5a3")

    def test_aaabbbccc(self):
        self.assertEqual(main.string_compresser(
            given_string= "aaabbbccc"
        ), "a3b3c3")

    def test_abc(self):
        self.assertEqual(main.string_compresser(
            given_string= "abc"
        ),"a1b1c1")

    def test_aabbcc(self):
        self.assertEqual(main.string_compresser(
            given_string="aabbcc"
        ), "aabbcc")