import unittest
from laba1 import is_monotonic


class TestIsMonotonic(unittest.TestCase):

    def test_increasing(self):
        self.assertTrue(is_monotonic([1, 2, 3, 4, 5]))

    def test_decreasing(self):
        self.assertTrue(is_monotonic([5, 4, 3, 2, 1]))

    def test_not_monotonic(self):
        self.assertFalse(is_monotonic([1, 2, 2, 3, 2, 4]))


if __name__ == '__main__':
    unittest.main()
