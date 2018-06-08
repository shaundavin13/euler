"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def is_multiple(num, *args):
    results = [num % arg == 0 for arg in args]
    return True in results


def find_multiples():
    answer = 0
    num = 0
    while num < 1000:
        if is_multiple(num, 3, 5):
            answer += num
        num += 1

    return answer


answer = find_multiples()
