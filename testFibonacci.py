import unittest
from recursive import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_factotial(self):
        val = fibonacci(10)
        self.assertEqual(55,val)

    def test_factotial_a0(self):
        val = fibonacci(0)
        self.assertEqual(1,val)
    
    def test_factotial_a1(self):
        val = fibonacci(1)
        self.assertEqual(1,val)