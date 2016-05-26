import unittest

from two_sum import all_permutations

class TestFoo(unittest.TestCase):
    def test_all_permutations(self):
        lst = range(3)
        result = all_permutations(lst)
        self.assertEqual(
            result,
            [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        )
