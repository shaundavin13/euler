"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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


def get_prime_sum_below(n):
    prime = 0
    total = 0
    gen = create_prime_gen()
    while prime < n:
        total += prime
        prime = next(gen)

    return total


answer = get_prime_sum_below(2 * 10 ** 6)
