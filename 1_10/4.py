"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(string):
    return string == string[::-1]


def largest_palindrome():
    return max([x * y for x in range(100, 1000) for y in range(100, 1000) if is_palindrome(str(x*y))])


answer = largest_palindrome()
