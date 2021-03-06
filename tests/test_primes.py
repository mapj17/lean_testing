import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import unittest
import src.primes as pr

class TestPrimes(unittest.TestCase):

    def test_prime_returns_itself(self):
        prime = 13
        expected = [prime]
        actual = pr.get_primes_trial_division(prime)
        self.assertEqual(expected, actual)

    def test_factor_primes_for_composite_number(self):
        prime = 4
        expected = [2, 2]
        actual = pr.get_primes_trial_division(prime)
        self.assertEqual(expected, actual)

    def test_factor_primes_for_other_composite_number(self):
        prime = 1
        expected = []
        actual = pr.get_primes_trial_division(prime)
        self.assertEqual(expected, actual)

    def test_get_primes_up_to_prime(self):
        num = 13
        expected = [2, 3, 5, 7, 11, 13]
        actual = pr.get_primes_up_to(num)
        self.assertEqual(expected, actual)

    def test_get_primes_up_to_non_prime(self):
        num = 16
        expected = [2, 3, 5, 7, 11, 13]
        actual = pr.get_primes_up_to(num)
        self.assertEqual(expected, actual)

    def test_get_first_n_primes(self):
        n = 5
        expected = [2,3,5,7,11]
        actual = pr.get_n_first_primes(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
