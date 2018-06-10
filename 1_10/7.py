"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import itertools


def is_divisible(num, primes):
    for prime in primes:
        if num % prime == 0:
            return True
    return False


def create_prime_gen():
    saved_primes = set()
    for num in itertools.count(2):
        if is_divisible(num, saved_primes):
            continue
        saved_primes.add(num)
        yield num


def get_nth_prime(n):
    gen = create_prime_gen()
    for i in range(n - 1):
        next(gen)
    return next(gen)


answer = get_nth_prime(10001)