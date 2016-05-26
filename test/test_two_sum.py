import unittest

from two_sum import all_permutations

class TestFoo(unittest.TestCase):
    def test_all_permutations(self):
        lst = list("abc")
        result = all_permutations(lst)
        self.assertEqual(
            result,
            [
                ((0, 'a'), (1, 'b')),
                ((0, 'a'), (2, 'c')),
                ((1, 'b'), (2, 'c'))
            ]
        )
