import unittest

import contextlib
from StringIO import StringIO
import sys

from binary_tree import (
    add,
    traverse_print,
    traverse_yield,
    traverse_via_helper
)

@contextlib.contextmanager
def redirect_stdout():
    s = StringIO()
    try:
        sys.stdout = s
        yield s
    finally:
        sys.stdout = sys.__stdout__
        s = s.close()

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
        with redirect_stdout() as s:
            traverse_print(tree, 'pre')
            result = s.getvalue().split('\n')[:-1]
        self.assertEqual(result, [])

    def test_traverse_print(self):
        tree = []
        add(tree, 'a')
        add(tree, 'b')
        add(tree, 'c')
        with redirect_stdout() as s:
            traverse_print(tree, 'pre')
            result = s.getvalue().split('\n')[:-1]
        self.assertEqual(result, ['a', 'b', 'c'])

    def test_traverse_yield(self):
        tree = []
        add(tree, 'a')
        add(tree, 'b')
        add(tree, 'c')
        result = list(traverse_yield(tree))
        self.assertEqual(result, ['a', 'b', 'c'])

class TestTraverseGlobalVar(unittest.TestCase):
    def test_traverse_global_var(self):
        tree = []
        add(tree, 'a')
        add(tree, 'b')
        add(tree, 'c')
        result = list(traverse_via_helper(tree))
        self.assertEqual(result, ['a', 'b', 'c'])
