import unittest

from linked_list import ll

class TestLL(unittest.TestCase):
    def test_get_head(self):
        result = ll("abcdef").value()
        self.assertIsNotNone(result)
