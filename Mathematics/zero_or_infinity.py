"""
Going to zero or to infinity?

Consider the following numbers (where n! is factorial(n)):

u1 = (1 / 1!) * (1!)

u2 = (1 / 2!) * (1! + 2!)

u3 = (1 / 3!) * (1! + 2! + 3!)

un = (1 / n!) * (1! + 2! + 3! + ... + n!)

Which will win: 1 / n! or (1! + 2! + 3! + ... + n!)?

Are these number going to 0 because of 1/n! or to infinity due to the sum of factorials?

Task:

Calculate (1 / n!) * (1! + 2! + 3! + ... + n!) for a given n. Call this
function "going(n)" where n is an integer greater or equal to 1.

To avoid discussions about rounding, if the result of the calculation is
designed by "result", going(n) will return "result" truncated to 6 decimal places.

Examples:

1.0000989217538616 will be truncated to 1.000098

1.2125000000000001 will be truncated to 1.2125
"""
from decimal import Decimal, getcontext
import functools
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


FACTORIAL_SUM = {}


@functools.lru_cache(maxsize=None)
def range_prod(lo, hi):
    if lo + 1 < hi:
        mid = (hi + lo) // 2
        return range_prod(lo, mid) * range_prod(mid + 1, hi)
    if lo == hi:
        return lo
    return lo * hi


def fac(n):
    if n < 2:
        return 1
    return range_prod(1, n)


def get_factorial_sum(num):
    if num in FACTORIAL_SUM:
        return FACTORIAL_SUM[num]
    else:
        sf = fac(num)
        for x in range(num - 1, 0, -1):
            if x in FACTORIAL_SUM:
                sf += FACTORIAL_SUM[x]
                break
            else:
                sf += fac(x)
        FACTORIAL_SUM[num] = sf
        return FACTORIAL_SUM[num]


def going(n):
    getcontext().prec = 8
    ans = (Decimal(1.000000) / fac(n)) * get_factorial_sum(n)

    sans = str(ans)
    if len(sans) > 8:
        return float(sans[:8].strip('0'))
    return ans


def run_tests():
    with Test() as test:
        test.assert_equals(going(5), 1.275)
        test.assert_equals(going(6), 1.2125)
        test.assert_equals(going(7), 1.173214)


if __name__ == '__main__':
    run_tests()
