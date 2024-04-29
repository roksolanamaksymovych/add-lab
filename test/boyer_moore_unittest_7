import unittest
from boyer_moore_7 import boyer_moore

class TestBoyerMoore(unittest.TestCase):

    def test_needle_not_in_haystack(self):
        result = boyer_moore("this is a haystack", "needle")
        self.assertEqual(result, [])

    def test_needle_at_beginning(self):
        result = boyer_moore("needle in a haystack", "needle")
        self.assertEqual(result, [0])

    def test_needle_multiple_occurrences(self):
        result = boyer_moore("needle needle in the haystack", "needle")
        self.assertEqual(result, [0, 7])

if __name__ == '__main__':
    unittest.main()
