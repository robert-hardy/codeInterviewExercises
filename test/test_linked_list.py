import unittest

from linked_list import ll

class TestLL(unittest.TestCase):
    def test_constructor(self):
        result = ll("abcdef")
        self.assertIsNotNone(result)
