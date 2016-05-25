import unittest

from linked_list import ll

class TestLL(unittest.TestCase):
    def setUp(self):
        self.result = ll("abcdef")

    def test_get_head(self):
        self.assertEquals(self.result.value(), 'a')

    def test_get_next(self):
        self.assertEquals(self.result.next().value())
