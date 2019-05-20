#!/usr/bin/python3

##      Small test file as a little bonus

import unittest
from is_anagram import is_anagram

class TestAnagram(unittest.TestCase):

    # When strings are not anagrams
    def test_false(self):
        self.assertFalse(is_anagram("mariya", "cybel"))
        self.assertFalse(is_anagram(" pythonn", "python"))
        self.assertFalse(is_anagram("vim", "miv emacs"))

    # When both strings are simple words
    def test_one_word(self):
         self.assertTrue(is_anagram("restful", "fluster"))
         self.assertTrue(is_anagram("caller", "recall"))
         self.assertTrue(is_anagram("discounter", "reductions"))

    # When both strings contain multiple words
    def test_multiple_words(self):
         self.assertTrue(is_anagram("eleven plus two", "twelve plus one"))
         self.assertTrue(is_anagram("forty five", "over fifty"))
         self.assertTrue(is_anagram("I am Lord Voldemort", "Tom Marvolo Riddle"))

    # When one string is a word and another contain multiple words
    def test_one_multi_words(self):
         self.assertTrue(is_anagram("funeral", "real fun"))
         self.assertTrue(is_anagram("adultery", "true lady"))
         self.assertTrue(is_anagram("dormitory", "dirty room"))

    # When strings contain some capital letters or number
    def test_untrimmed(self):
         self.assertTrue(is_anagram("    placebo ", " obe calp  "))
         self.assertTrue(is_anagram("rail1safety", "fairy tales1"))
         self.assertTrue(is_anagram("AlerteD12", "T1readl2e"))

if __name__ == '__main__':
    unittest.main()
