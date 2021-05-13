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
