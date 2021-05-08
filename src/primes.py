def get_primes_trial_division(num):
    primes = []
    for i in range(2,num + 1):
        while num % i == 0:
            num = num / i
            primes.append(i)
        if num == 1:
            return primes
    return primes


def is_prime(num):
    for i in range((num // 2) + 1):
        if i % num == 0:
            return False
    return True


def get_primes_up_to(num):
    return [x if is_prime(x) for x in range(num + 1)]


