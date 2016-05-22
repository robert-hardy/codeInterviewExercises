import unittest

from sum_of_cubes import find_one_pair

class TestSumOfCubes(unittest.TestCase):
    def test_can_find_one_under_one_thousand(self):
        result = find_one_pair();
        self.assertTrue(result is not None)
