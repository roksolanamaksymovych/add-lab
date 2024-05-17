import unittest
from max_wire_length_9 import max_wire_length
import math


def test_max_wire_length_large(self):
    # Тестуємо функцію з великими вхідними даними
    distance_between_poles = 8
    pole_heights = [9, 4, 11, 5, 15, 6, 12]
    self.assertAlmostEqual(max_wire_length(distance_between_poles, pole_heights), 48.64, places=2)


def test_max_wire_length_same_height(self):
    # Тестуємо функцію з опорами однакової висоти
    distance_between_poles = 5
    pole_heights = [5, 5, 5, 5, 5]
    self.assertAlmostEqual(max_wire_length(distance_between_poles, pole_heights), 25.00, places=2)


def test_max_wire_length_single_pole(self):
    # Тестуємо функцію з однією опорою
    distance_between_poles = 5
    pole_heights = [10]
    self.assertAlmostEqual(max_wire_length(distance_between_poles, pole_heights), 0.00, places=2)


if __name__ == '__main__':
    unittest.main()
