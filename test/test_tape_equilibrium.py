import unittest

from tape_equilibrium import all_slices

class TestIterTools(unittest.TestCase):
    def test_create_all_slices(self):
        result = all_slices(range(3))
        self.assertEqual(
            result,
            [
                [[0], [1, 2]],
                [[0, 1], [2]]
            ]
        )
