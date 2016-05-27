import unittest

from binary_tree import (
    add,
    traverse
)

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

    def test_add_three_values(self):
        root = []
        add(root, 'a')
        add(root, 'b')
        add(root, 'c')
        self.assertEqual(root, ['a', ['b', [], []], ['c', [], []]])

    def test_add_four_values(self):
        root = []
        add(root, 'a')
        add(root, 'b')
        add(root, 'c')
        add(root, 'd')
        self.assertEqual(root, ['a', ['b', ['d', [], []], []], ['c', [], []]])

class TestTraversing(unittest.TestCase):
    def test_empty_tree(self):
        tree = []
        result = traverse(tree, 'pre')
        self.assertEqual(result, [])

    def test_traverse(self):
        tree = []
        add(tree, 'a')
        add(tree, 'b')
        add(tree, 'c')
        result = traverse(tree, 'pre')
        self.assertEqual(result, ['a', 'b', 'c'])
