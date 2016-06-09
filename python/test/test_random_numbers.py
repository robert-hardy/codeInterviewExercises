import unittest

from collections import Counter
from decimal import Decimal
from random import seed

from random_numbers import (
    make_left_cts_step_function,
    make_inv_dist_func,
    cumulative_sum,
    make_generator
)

class TestStepFunctionFactory(unittest.TestCase):
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


class TestInverseDistributionFunctionFactory(unittest.TestCase):
    def setUp(self):
        self.func = make_inv_dist_func(
            random_nums=[1, 2, 3],
            probabilities=[0.1, 0.5, 0.4]
        )

    def test_create_inv_dist_func(self):
        self.assertEqual(self.func(0.09), 1)
        self.assertEqual(self.func(0.1), 1)
        self.assertEqual(self.func(0.11), 2)
        self.assertEqual(self.func(0.59), 2)
        self.assertEqual(self.func(0.60), 2)
        self.assertEqual(self.func(0.65), 3)

    def test_value_at_zero_and_at_one(self):
        self.assertEqual(self.func(0), 1)
        self.assertEqual(self.func(1), 3)

    def test_throws_error_when_misspecified(self):
        pass


class TestFixedVsFloatingPoint(unittest.TestCase):
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
        # Just to the right we can get an incorrect value if we use floats ...
        self.assertEqual(func_fixed_point(Decimal('0.1000000000000000001')), 2)
        self.assertEqual(func_float_point(         0.1000000000000000001),   1)
        self.assertEqual(func_fixed_point(Decimal('0.100000000000000001')), 2)
        self.assertEqual(func_float_point(         0.100000000000000001),   1)
        self.assertEqual(func_fixed_point(Decimal('0.10000000000000001')), 2)
        self.assertEqual(func_float_point(         0.10000000000000001),   1)
        # ... until we are far enough away
        self.assertEqual(func_fixed_point(Decimal('0.1000000000000001')), 2)
        self.assertEqual(func_float_point(         0.1000000000000001),   2)


class TestGenerator(unittest.TestCase):
    def test_uniform_probabilities(self):
        gen = make_generator(
            random_nums=range(10),
            probabilities=[Decimal('0.1')] * 10
        )
        seed(0)
        result = [ gen() for i in range(1000) ]
        count = [ (k, v) for (k, v) in Counter(result).iteritems() ]
        self.assertEqual(count, [
            (0, 114), (1, 87), (2, 95), (3, 102), (4, 110),
            (5, 89), (6, 109), (7, 104), (8, 86), (9, 104)
        ])
        seed(1)
        result = [ gen() for i in range(1000) ]
        count = [ (k, v) for (k, v) in Counter(result).iteritems() ]
        self.assertEqual(count, [
            (0, 95), (1, 85), (2, 100), (3, 102), (4, 91),
            (5, 114), (6, 87), (7, 108), (8, 115), (9, 103)
        ])

    def test_ten_percent_heads(self):
        gen = make_generator(
            random_nums=['H', 'T'],
            probabilities=[Decimal('0.1'), Decimal('0.9')]
        )
        seed(0)
        result = [ gen() for i in range(1000) ]
        count = [ (k, v) for (k, v) in Counter(result).iteritems() ]
        self.assertEqual(count, [ ('H', 114), ('T', 886) ])
        seed(1)
        result = [ gen() for i in range(1000) ]
        count = [ (k, v) for (k, v) in Counter(result).iteritems() ]
        self.assertEqual(count, [ ('H', 95), ('T', 905) ])

    def test_given_example(self):
        gen = make_generator(
            random_nums=[-1, 0, 1, 2, 3],
            probabilities=[
                Decimal('0.01'),
                Decimal('0.3'),
                Decimal('0.58'),
                Decimal('0.1'),
                Decimal('0.01')
            ]
        )
        seed(0)
        result = [ gen() for i in range(1000) ]
        count = sorted([ (k, v) for (k, v) in Counter(result).iteritems() ],
                key=lambda x: x[0])
        self.assertEqual(count, [(-1, 15), (0, 288), (1, 583), (2, 109), (3, 5)])
        seed(1)
        result = [ gen() for i in range(1000) ]
        count = sorted([ (k, v) for (k, v) in Counter(result).iteritems() ],
                key=lambda x: x[0])
        self.assertEqual(count, [(-1, 10), (0, 282), (1, 591), (2, 109), (3, 8)])
