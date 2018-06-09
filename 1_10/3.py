"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import itertools


def continuously_divide(num, quotient):
    frequency = 0
    while num % quotient == 0:
        num /= quotient
        frequency += 1
    return num, frequency


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


def find_prime_factors(num):
    factors = []
    gen = create_prime_gen()
    prime = next(gen)
    original_num = num
    while prime < original_num ** 0.5:
        num, frequency = continuously_divide(num, prime)
        if frequency:
            factors += [prime] * frequency
        prime = next(gen)

    factors.append(num)
    return max(factors)


answer = find_prime_factors(600851475143)

