import unittest

from triangle import solution

class Test(unittest.TestCase):
    def test(self):
        A = [ 3, 4, 5 ]
        result = solution(A)
        self.assertEqual(result, (0, 1, 2))
