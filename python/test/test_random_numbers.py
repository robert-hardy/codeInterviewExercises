import unittest

from random_numbers import grade

class Test(unittest.TestCase):
    def test_grade(self):
        self.assertEqual(grade(60), 'D')
        self.assertEqual(grade(59.999), 'F')
