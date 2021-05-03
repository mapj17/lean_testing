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

if __name__ == '__main__':
    unittest.main()
