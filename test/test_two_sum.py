import unittest

from two_sum import (
    all_permutations,
    get_first_sum_to_target
)

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

    def test_sum_function(self):
        combos = [
            ((0, 1), (1, 2)),
            ((0, 1), (2, 3)),
            ((1, 2), (2, 3))
        ]
        result = get_first_sum_to_target(combos, 4)
        self.assertEqual(result, ((0, 1), (2, 3)))

        result = get_first_sum_to_target(combos, 7)
        self.assertEqual(result, None)
