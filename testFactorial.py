import unittest
from recursive import factorial

class TestFactorial(unittest.TestCase):

    def test_factotial(self):
        val = factorial(4)
        self.assertEqual(24,val)

    def test_factotial_a0(self):
        val = factorial(0)
        self.assertEqual(1,val)
    
    def test_factotial_a1(self):
        val = factorial(1)
        self.assertEqual(1,val)