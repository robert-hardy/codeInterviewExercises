import unittest

from decimal import Decimal

from random_numbers import (
    make_right_cts_step_function,
    make_left_cts_step_function,
    make_inv_dist_func,
    cumulative_sum
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

class TestHelperFunctions(unittest.TestCase):
    def test_cumul_sum(self):
        result = list(cumulative_sum([0, 1, 2, 3]))
        self.assertEqual(result, [0, 1, 3, 6])

    def test_cumul_sum_empty_list(self):
        result = list(cumulative_sum([]))
        self.assertEqual(result, [])

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

    def test_compare_fixed_vs_floating_point(self):
        func_fixed_point = make_inv_dist_func(
            random_nums=[1, 2, 3],
            probabilities=[Decimal('0.1'), Decimal('0.5'), Decimal('0.4')]
        )
        func_float_point = make_inv_dist_func(
            random_nums=[1, 2, 3],
            probabilities=[0.1, 0.5, 0.4]
        )
        # Both agree exactly at the point
        self.assertEqual(func_fixed_point(Decimal('0.1')), 1)
        self.assertEqual(func_float_point(         0.1),   1)
        # Just the the right we get an incorrect value if we use floats ...
        self.assertEqual(func_fixed_point(Decimal('0.1000000000000000001')), 2)
        self.assertEqual(func_float_point(         0.1000000000000000001),   1)
        self.assertEqual(func_fixed_point(Decimal('0.100000000000000001')), 2)
        self.assertEqual(func_float_point(         0.100000000000000001),   1)
        self.assertEqual(func_fixed_point(Decimal('0.10000000000000001')), 2)
        self.assertEqual(func_float_point(         0.10000000000000001),   1)
        # ... until we get far enough away
        self.assertEqual(func_fixed_point(Decimal('0.1000000000000001')), 2)
        self.assertEqual(func_float_point(         0.1000000000000001),   2)
