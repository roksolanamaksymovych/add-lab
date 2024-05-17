import unittest
from max_amount_of_experience_6 import find_max_experience


class TestFindMaxExperience(unittest.TestCase):

    def test_max_experience_calculation(self):
        levels = 3
        experience = [
            [3],
            [4, 2],
            [6, 5, 7]
        ]

        self.assertEqual(find_max_experience(levels, experience), 13)

    def test_zero_experience(self):
        levels = 1
        experience = [
            [0]
        ]
        self.assertEqual(find_max_experience(levels, experience), 0)

    def test_max_experience_with_single_level(self):
        levels = 1
        experience = [
            [5]
        ]
        self.assertEqual(find_max_experience(levels, experience), 5)

if __name__ == '__main__':
    unittest.main()
