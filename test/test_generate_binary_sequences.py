import unittest

from generate_binary_sequences import gen

class TestFoo(unittest.TestCase):
    def test_generator(self):
        seq = gen()
        self.assertEqual(seq.next(), '0')
        self.assertEqual(seq.next(), '1')
        self.assertEqual(seq.next(), '00')
        self.assertEqual(seq.next(), '01')
        self.assertEqual(seq.next(), '10')
        self.assertEqual(seq.next(), '11')
        self.assertEqual(seq.next(), '000')
        self.assertEqual(seq.next(), '001')
        self.assertEqual(seq.next(), '010')
        self.assertEqual(seq.next(), '011')
