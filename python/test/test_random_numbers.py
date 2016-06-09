import unittest

from math import isnan
from random import randint

from random_numbers import collect_many_random_integers

class Test(unittest.TestCase):
    def test_big_random_integers(self):
        self.assertFalse(isnan(randint(0, 10 ** 100)))

    def test_basic_randint(self):
        result = collect_many_random_integers()
        self.assertEqual(result, set(range(10)))
