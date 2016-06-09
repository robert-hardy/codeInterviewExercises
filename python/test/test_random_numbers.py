import unittest

from random_numbers import (
    make_right_cts_step_function,
    make_left_cts_step_function,
    make_inv_dist_func
)

class TestRightCtsStepFunction(unittest.TestCase):
    def setUp(self):
        self.func = make_right_cts_step_function(
            step_points=[60, 70, 80, 90],
            plateaus='FDCBA'
        )

    def test_leftmost(self):
        self.assertEqual(self.func(30), 'F')

    def test_intermediate(self):
        self.assertEqual(self.func(60), 'D')

    def test_rightmost(self):
        self.assertEqual(self.func(95), 'A')

class TestLeftCtsStepFunction(unittest.TestCase):
    def setUp(self):
        self.func = make_left_cts_step_function(
            step_points=[60, 70, 80, 90],
            plateaus='FDCBA'
        )

    def test_leftmost(self):
        self.assertEqual(self.func(30), 'F')

    def test_intermediate(self):
        self.assertEqual(self.func(60), 'F')

    def test_rightmost(self):
        self.assertEqual(self.func(95), 'A')

class TestInverseDistributionFunction(unittest.TestCase):
    def test_create_inv_dist_func(self):
        func = make_inv_dist_func(
            random_nums=[1, 2, 3],
            probabilities=[0.1, 0.5, 0.4]
        )
        self.assertEqual(func(0.09), 1)
        self.assertEqual(func(0.1), 1)
        self.assertEqual(func(0.11), 2)
        self.assertEqual(func(0.59), 2)
        self.assertEqual(func(0.60), 2)
        self.assertEqual(func(0.65), 3)
