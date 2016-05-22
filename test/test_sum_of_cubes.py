import unittest

from sum_of_cubes import find_one_pair, create_triangle

class TestSumOfCubes(unittest.TestCase):
    def test_can_find_one_under_one_thousand(self):
        result = find_one_pair();
        self.assertEqual(len(result.keys()), 1024)

    def test_triangle(self):
        result = create_triangle()
        self.assertEqual(len(result), 500500)
