import unittest
import src.primes as pr

class TestPrimes(unittest.TestCase):

    def test_prime_returns_itself(self):
        prime = 13
        expected = [prime]
        actual = pr.get_primes_trial_division(prime)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
