import unittest

from generate_binary_sequences import gen

class TestFoo(unittest.TestCase):
    def test_generator(self):
        seq = gen()
        self.assertEqual(seq.next(), '0')
