import unittest

from sum_of_cubes import create_triangle, collect_sums, filter_dict, go_for_it

class TestHelpers(unittest.TestCase):
    def test_triangle(self):
        result = create_triangle(3)
        self.assertEqual(result, [(1,1), (2,1), (2,2), (3,1), (3,2), (3,3)])

    def test_collect_sums(self):
        result = collect_sums(20)
        self.assertTrue(2 in result)
        self.assertTrue(9 in result)
        self.assertTrue(16 in result)

    def test_filter_dict(self):
        d = { 1: [ 1, 2 ], 2: [ 1], 3: [ 1, 2, 3 ] }
        result = filter_dict(d)
        self.assertEqual(result, { 1: [1, 2], 3: [1, 2, 3]})

class TestMain(unittest.TestCase):
    def test_all(self):
        result = go_for_it(15)
        self.assertEqual(result, {1729:[(10, 9), (12, 1)]})
