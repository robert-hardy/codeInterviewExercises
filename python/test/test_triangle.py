import unittest

from triangle import solution

class Test(unittest.TestCase):
    def test(self):
        A = [ 1, 2, 3, 4, 5 ]
        result = solution(A)
        self.assertEqual(result, 1)

    def test_no_triangle(self):
        A = [ 0 ] * 1000
        result = solution(A)
        self.assertEqual(result, 0)
