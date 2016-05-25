import unittest

from linked_list import (
    create_ll,
    li,
    remove_duplicates,
    remove_duplicates_without_buffer,
    trim_duplicates_from_front,
    is_in,
    to_string
)

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
        self.assertEqual(to_string(result), "ab")

    def test_remove_duplicates_without_buffer(self):
        ll = create_ll("ababcc")
        result = remove_duplicates_without_buffer(ll)
        self.assertEqual(to_string(result), "abc")
        ll = create_ll("ababccaac")
        result = remove_duplicates_without_buffer(ll)
        self.assertEqual(to_string(result), "bac")

    def test_trim_duplicates_from_front(self):
        ll = create_ll("aab")
        result = trim_duplicates_from_front(ll)
        self.assertEqual(to_string(result), "ab")

class TestMembershipFunctions(unittest.TestCase):
    def test_is_in(self):
        ll = create_ll("abc")
        self.assertTrue(is_in('a', ll))
        self.assertFalse(is_in('d', ll))

class TestHelpers(unittest.TestCase):
    def test_to_string(self):
        ll = create_ll("abc")
        self.assertEqual(to_string(ll), "abc")
