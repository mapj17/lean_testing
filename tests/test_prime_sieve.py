import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import unittest
import src.prime_sieve as sieve

class TestPrimeSieve(unittest.TestCase):
    def setUp(self):
        self.sieve = sieve.PrimeSieve(1000)

    def test_prime_sieve_is_prime_for_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 991]
        expected = True
        for prime in primes:
            actual = self.sieve.is_prime(prime)
            self.assertEqual(expected, actual)

    def test_prime_sieve_is_prime_for_non_primes(self):
        non_primes = [4, 6, 8 ,9 , 14, 1000]
        expected = False
        for non_prime in non_primes:
            actual = self.sieve.is_prime(non_prime)
            self.assertEqual(expected, actual)
    def test_prime_sieve_sum(self):
        tmp_sieve = sieve.PrimeSieve(5)
        expected = 10
        actual = tmp_sieve.sum_of_primes_in_sieve()
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
