import unittest

from random_numbers import collect_many_random_integers

class Test(unittest.TestCase):
    def test_basic_randint(self):
        result = collect_many_random_integers()
        self.assertEqual(result, set(range(10)))
