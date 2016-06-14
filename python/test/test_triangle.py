import unittest

from random import randint

from triangle import solution, solution2

class Test(unittest.TestCase):
    def test(self):
        A = [ 1, 2, 3, 4, 5 ]
        result = solution(A)
        self.assertEqual(result, 1)

    def test_no_triangle(self):
        A = [ 0 ] * 100000
        result = solution(A)
        self.assertEqual(result, 0)

    def test_equilateral(self):
        A = [ 1 ] * 100
        result = solution(A)
        self.assertEqual(result, 1)

class TestTwoApproachesAgree(unittest.TestCase):
    def test_random_samples(self):
        for i in range(5000):
            A = [ randint(1, 50) for i in range(200) ]
            result = solution(A)
            result2 = solution2(A)
            self.assertEqual(result, result2)
