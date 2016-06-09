import unittest

from random_numbers import step_function

class Test(unittest.TestCase):
    def test_grade(self):
        self.assertEqual(step_function(60), 'D')
        self.assertEqual(step_function(59.999), 'F')
