import unittest

from binary_tree import add

class TestFoo(unittest.TestCase):
    def test_simple_tree(self):
        tree = [ 'a', [], [] ]
        left, right = tree[1:]
        left.extend(['b', [], []])
        right.extend(['c', [], []])
        self.assertEqual(tree, ['a', ['b', [], []], ['c', [], []]])

    def test_add_to_empty_node(self):
        root = []
        add(root, 'a')
        self.assertEqual(root, ['a', [], []])

    def test_add_two_values(self):
        root = []
        add(root, 'a')
        add(root, 'b')
        self.assertEqual(root, ['a', ['b', [], []], []])
