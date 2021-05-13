import numpy as np


class PrimeSieve:
    def __init__(self, upper_bound):
        self.upper_bound = upper_bound
        self.sieve = np.array(list(range(upper_bound + 1)))
        self.sieve[1] = 0
        idx = self._get_idx_next_non_zero_element(0)
        while idx >= 0:
            self.sieve[2 * idx::idx] = 0
            idx = self._get_idx_next_non_zero_element(idx)

    def _get_idx_next_non_zero_element(self, prev_idx):
        for i in range(prev_idx + 1, len(self.sieve)):
            if self.sieve[i]:
                return i
        return -1

    def is_prime(self, num):
        if num > self.upper_bound:
            raise Exception('Number not contained in sieve')
        else:
            return self.sieve[num] > 0


def get_primes_trial_division(num):
    primes = []
    for i in range(2, num + 1):
        while num % i == 0:
            num = num / i
            primes.append(i)
        if num == 1:
            return primes
    return primes


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_primes_up_to(num):
    assert num >= 2
    return [x for x in range(2, num + 1) if is_prime(x)]
