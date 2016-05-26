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
        result = add(root, 'a')
        self.assertEqual(result, ['a', [], []])
