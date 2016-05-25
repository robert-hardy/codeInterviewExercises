import unittest

from linked_list import create_ll, li, remove_duplicates

class TestCreateLinkedList(unittest.TestCase):
    def setUp(self):
        self.result = create_ll("abcdef")

    def test_get_head(self):
        self.assertEquals(self.result.value(), 'a')

    def test_get_next(self):
        self.assertEquals(self.result.next().value(), 'b')

class TestLI(unittest.TestCase):
    def test_get_value(self):
        result = li('a', None)
        self.assertEqual(result.value(), 'a')

    def test_get_next_value(self):
        foo = li('a', None)
        bar = li('b', foo)
        self.assertEqual(bar.value(), 'b')
        self.assertEqual(bar.next().value(), 'a')

class TestTermination(unittest.TestCase):
    def test_tail_of_end(self):
        ll = create_ll("ab")
        self.assertEqual(ll.value(), 'a')
        self.assertEqual(ll.next().value(), 'b')
        self.assertEqual(ll.next().next().value(), None)
        self.assertEqual(ll.next().next().next().value(), None)
        self.assertEqual(ll.next().next().next().next().value(), None)

class TestCleaningFunctions(unittest.TestCase):
    def test_remove_duplicates(self):
        ll = create_ll("abb")
        result = remove_duplicates(ll)
        self.assertEqual(ll.value(), 'a')
        self.assertEqual(ll.next().value(), 'b')
        self.assertEqual(ll.next().next().value(), None)
