import unittest
from min_square_board_2 import min_square_size


class TestMinSquareSize(unittest.TestCase):
    def test_min_square_size_with_one_leaf(self):
        result = min_square_size(1, 2, 3)
        self.assertEqual(result, 3)

    def test_min_square_size_with_many_leaves(self):
        result = min_square_size(10, 2, 3)
        self.assertEqual(result, 9)

    def test_min_square_size_with_small_dimensions(self):
        result = min_square_size(1, 1, 1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
