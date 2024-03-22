import unittest
from billboards_merge_sort import merge_sort, paint_billboards


class TestPaintBillboards(unittest.TestCase):

    def test_equal_painters_and_billboards(self):

        k = 4
        t = 7
        lengths = [10, 15, 20, 25]
        expected_time = max(lengths) * t
        self.assertEqual(paint_billboards(k, t, lengths), expected_time)

    def test_more_painters_than_billboards(self):

        k = 5
        t = 4
        lengths = [10, 20, 15]
        expected_time = sum(lengths) * t
        self.assertEqual(paint_billboards(k, t, lengths), expected_time)

    def test_less_painters_than_billboards(self):

        k = 2
        t = 5
        lengths = [10, 20, 15, 30, 25]
        expected_time = max(lengths) * t
        self.assertEqual(paint_billboards(k, t, lengths), expected_time)


if __name__ == '__main__':
    unittest.main()
