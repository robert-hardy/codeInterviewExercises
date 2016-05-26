import unittest

class TestFoo(unittest.TestCase):
    def test_simple_tree(self):
        tree = [ 'a', [], [] ]
        left, right = tree[1:]
        left.extend(['b', [], []])
        right.extend(['c', [], []])
        self.assertEqual(tree, ['a', ['b', [], []], ['c', [], []]])
