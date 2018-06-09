"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

from collections import defaultdict
import itertools
from functools import reduce


def continuously_divide(num, quotient):
    frequency = 0
    while num % quotient == 0:
        num /= quotient
        frequency += 1
    return int(num), frequency


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
    while prime <= original_num ** 0.5:
        num, frequency = continuously_divide(num, prime)
        if frequency:
            factors += [prime] * frequency
        prime = next(gen)

    factors.append(num)
    return factors


def generate_frequency_dict(some_list):
    frequencies = defaultdict(int)
    for item in some_list:
        frequencies[item] += 1
    return frequencies


def lcm(*factors):
    prime_factor_frequency_dicts = [generate_frequency_dict(find_prime_factors(factor)) for factor in factors]

    master_frequency_dict = defaultdict(int)

    for freq_dict in prime_factor_frequency_dicts:
        for factor, frequency in freq_dict.items():
            master_frequency_dict[factor] = max(master_frequency_dict[factor], frequency)

    relevant_factors = itertools.chain(*[[value] * freq for value, freq in master_frequency_dict.items()])

    return reduce(lambda x, y: x * y, relevant_factors)


answer = lcm(*range(1, 21))
