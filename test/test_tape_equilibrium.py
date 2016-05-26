import unittest

from tape_equilibrium import (
    all_slices,
    make_sums,
    make_abs_diff
)

class TestIterTools(unittest.TestCase):
    def test_create_all_slices(self):
        result = all_slices(range(3))
        self.assertEqual(
            result,
            [
                ([0], [1, 2]),
                ([0, 1], [2])
            ]
        )

    def test_create_all_slices_with_letters(self):
        result = all_slices(list("abc"))
        self.assertEqual(
            result,
            [
                (['a'], ['b', 'c']),
                (['a', 'b'], ['c'])
            ]
        )

    def test_sums(self):
        lst = [
            ([0], [1, 2]),
            ([0, 1], [2])
        ]
        result = make_sums(lst)
        self.assertEqual(result, [(0, 3), (1, 2)])

    def test_abs_diff(self):
        lst = [(0, 3), (1, 2)]
        result = make_abs_diff(lst)
        self.assertEqual(result, [3, 1])
        self.assertEqual(min(result), 1)
