import unittest

from random_numbers import (
    step_function,
    make_right_cts_step_function,
    make_left_cts_step_function
)

class Test(unittest.TestCase):
    def test_right_cts(self):
        self.assertEqual(step_function(60), 'D')

    def test_left_cts(self):
        self.assertEqual(step_function(60, right_cts=False), 'F')

    def test_leftmost(self):
        self.assertEqual(step_function(30), 'F')
        self.assertEqual(step_function(30, right_cts=False), 'F')

    def test_rightmost(self):
        self.assertEqual(step_function(95), 'A')
        self.assertEqual(step_function(95, right_cts=False), 'A')

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
