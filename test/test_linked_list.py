import unittest

from linked_list import ll, li

class TestLL(unittest.TestCase):
    def setUp(self):
        self.result = ll("abcdef")

    def test_get_head(self):
        self.assertEquals(self.result.value(), 'f')

    def test_get_next(self):
        import ipdb; ipdb.set_trace()
        self.assertEquals(self.result.next().value())

class TestLI(unittest.TestCase):
    def test_get_value(self):
        result = li('a', None)
        self.assertEqual(result.value(), 'a')

    def test_get_next_value(self):
        foo = li('a', None)
        bar = li('b', foo)
        self.assertEqual(bar.value(), 'b')
        self.assertEqual(bar.next().value(), 'a')
