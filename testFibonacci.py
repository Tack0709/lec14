import unittest
from recursive import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        val = fibonacci(10)
        self.assertEqual(55, val)

    def test_fibonacci_a0(self):
        val = fibonacci(0)
        self.assertEqual(0, val)

    def test_fibonacci_a1(self):
        val = fibonacci(1)
        self.assertEqual(1, val)
