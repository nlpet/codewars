"""
Find the odd int

Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""
from collections import Counter
from functools import reduce
from operator import xor
import sys

sys.path.append('..')
from helpers.test_wrapper import Test


def find_it(seq):
    is_odd = lambda pair: pair[1] % 2 != 0
    return list(filter(is_odd, Counter(seq).items()))[0][0]


# faster
def find_it_xor(seq):
    return reduce(xor, seq)


def run_tests():
    with Test() as test:
        test.describe("Example")
        test.assert_equals(
            find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
        lst = [x for x in range(100000)] + [x for x in range(100000)] + [2]
        test.assert_equals(find_it(lst), 2)

    with Test() as test:
        test.describe("Example xor")
        test.assert_equals(
            find_it_xor([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
        lst = [x for x in range(100000)] + [x for x in range(100000)] + [2]
        test.assert_equals(find_it_xor(lst), 2)


if __name__ == '__main__':
    run_tests()
