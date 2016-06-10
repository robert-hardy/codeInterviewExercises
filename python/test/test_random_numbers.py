import unittest

from collections import Counter
from decimal import Decimal
from random import seed

from random_numbers import (
    make_inv_dist_func,
    make_generator,
    RandomGen
)

class TestInverseDistributionFunctionFactory(unittest.TestCase):
    def setUp(self):
        self.func = make_inv_dist_func(
            random_nums=[1, 2, 3],
            probabilities=[0.2, 0.5, 0.3]
        )

    def test_create_inv_dist_func(self):
        self.assertEqual(self.func(0),    1)
        self.assertEqual(self.func(0.19), 1)
        self.assertEqual(self.func(0.2),  1)
        self.assertEqual(self.func(0.21),  2)
        self.assertEqual(self.func(0.69),  2)
        self.assertEqual(self.func(0.70),  2)
        self.assertEqual(self.func(0.71),   3)
        self.assertEqual(self.func(1),      3)


class TestErrorHandling(unittest.TestCase):
    def test_throws_error_when_misspecified(self):
        with self.assertRaises(ValueError) as context:
            func = make_inv_dist_func(
                random_nums=[1, 2],
                probabilities=[0.1, 0.5]
            )
        with self.assertRaises(ValueError) as context:
            func = make_inv_dist_func(
                random_nums=[1, 2],
                probabilities=[Decimal('0.1'), Decimal('0.5')]
            )


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
        # Both agree exactly at the step point
        self.assertEqual(func_fixed_point(Decimal('0.1')), 1)
        self.assertEqual(func_float_point(         0.1),   1)
        # Just to the right we can get an incorrect value if we use floats but
        # okay with Decimal ...
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


class TestRandomGenClass(unittest.TestCase):
    def test_given_example(self):
        gen = RandomGen(
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
        result = [ gen.next_num() for i in range(1000) ]
        count = sorted([ (k, v) for (k, v) in Counter(result).iteritems() ],
                key=lambda x: x[0])
        self.assertEqual(count, [(-1, 15), (0, 288), (1, 583), (2, 109), (3, 5)])
        seed(1)
        result = [ gen.next_num() for i in range(1000) ]
        count = sorted([ (k, v) for (k, v) in Counter(result).iteritems() ],
                key=lambda x: x[0])
        self.assertEqual(count, [(-1, 10), (0, 282), (1, 591), (2, 109), (3, 8)])
