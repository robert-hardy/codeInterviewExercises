import unittest

from random_numbers import (
    make_right_cts_step_function,
    make_left_cts_step_function
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

class TestLefCtsStepFunction(unittest.TestCase):
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
