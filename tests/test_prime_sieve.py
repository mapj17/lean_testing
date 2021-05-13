import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import unittest
import src.prime_sieve as sieve

class TestPrimeSieve(unittest.TestCase):
    def setUp(self):
        self.sieve = sieve.PrimeSieve(1000)

    def test_prime_sieve_is_prime_for_prime(self):
        prime = 13
        expected = True
        actual = self.sieve.is_prime(prime)
        self.assertEqual(expected, actual)

    def test_prime_sieve_is_prime_for_non_prime(self):
        non_prime = 14
        expected = False
        actual = self.sieve.is_prime(non_prime)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
