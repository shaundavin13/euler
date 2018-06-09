"""
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.

"""


def last_10():
    base = 2
    for i in range(7830457 - 1):
        base *= 2
        if base > 10 ** 10:
            base = base % (10 ** 10)
    result = base * 28433 + 1
    return result % (10 ** 10)


answer = last_10()
