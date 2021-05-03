def get_primes_trial_division(num):
    primes = []
    for i in range(2,num + 1):
        while num % i == 0:
            num = num / i
            primes.append(i)
        if num == 1:
            return primes

if __name__=="__main__":
    print(get_primes_trial_division(52))
