import unittest

from itertools_exercises import (
    tabulate
)

class TestTabulate(unittest.TestCase):
    def test_first_value(self):
        def f(n):
            return n**2
        table = tabulate(f)
        result = table.next()
        self.assertEqual(result, 0)

    def test_a_few_values(self):
        def f(n):
            return n**2
        table = tabulate(f)
        result = [ table.next() for i in range(3) ]
        self.assertEqual(result, [ 0, 1, 4])
