import unittest

from random_numbers import step_function

class Test(unittest.TestCase):
    def test_right_cts(self):
        self.assertEqual(step_function(60), 'D')

    def test_left_cts(self):
        self.assertEqual(step_function(60, right_cts=False), 'F')
