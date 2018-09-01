"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


import itertools


def find_pythagorean_triplet():
    for a in itertools.count(1):
        for b in range(1000 - a, 0, -1):
            c = (a ** 2 + b ** 2) ** 0.5
            if a + b + c == 1000:
                return a * b * c


answer = find_pythagorean_triplet()
