"""
Perimeter of squares in a rectangle

The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8.
It's easy to see that the sum of the perimeters of these squares is :
4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle
when there are n + 1 squares disposed in the same manner as in the drawing:
"""
import functools
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def perimeter(n):
    return sum([fib(i) for i in range(1, n + 2)]) * 4


def run_tests():
    with Test() as test:
        test.assert_equals(perimeter(5), 80)
        test.assert_equals(perimeter(7), 216)
        test.assert_equals(perimeter(20), 114624)
        test.assert_equals(perimeter(30), 14098308)
        test.assert_equals(perimeter(100), 6002082144827584333104)


if __name__ == '__main__':
    run_tests()
