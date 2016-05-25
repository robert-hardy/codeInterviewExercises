import unittest

from linked_list import create_ll, li

class TestCreateLinkedList(unittest.TestCase):
    def setUp(self):
        self.result = create_ll("abcdef")

    def test_get_head(self):
        self.assertEquals(self.result.value(), 'f')

    def test_get_next(self):
        self.assertEquals(self.result.next().value(), 'e')

class TestLI(unittest.TestCase):
    def test_get_value(self):
        result = li('a', None)
        self.assertEqual(result.value(), 'a')

    def test_get_next_value(self):
        foo = li('a', None)
        bar = li('b', foo)
        self.assertEqual(bar.value(), 'b')
        self.assertEqual(bar.next().value(), 'a')
