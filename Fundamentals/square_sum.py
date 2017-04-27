"""
Square(n) Sum

Complete the squareSum method so that it squares each number
passed into it and then sums the results together.

For example:

square_sum([1, 2, 2]) # should return 9
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def square_sum(numbers):
    return sum(map(lambda x: x * x, numbers))


def run_tests():
    with Test() as test:
        test.expect(square_sum([1, 2]), 'squareSum did not return a value')
        test.assert_equals(square_sum([1, 2]), 5)
        test.assert_equals(square_sum([0, 3, 4, 5]), 50)


if __name__ == '__main__':
    run_tests()
