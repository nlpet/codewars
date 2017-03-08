"""
Floating-point Approximation (I)

Consider the function

f: x -> sqrt(1 + x) - 1 at x = 1e-15.

We get: f(x) = 4.44089209850062616e-16

or something around that, depending on the language.

This function involves the subtraction of a pair of similar numbers when x
is near 0 and the results are significantly erroneous in this region.
Using pow instead of sqrt doesn't give better results.

A good answer is 4.99999999999999875... * 1e-16.

Can you modify f(x) to give a good approximation of f(x) in the neigbourhood of 0?

Note:

Don't round or truncate your results, you will pass the tests if

abs((your_result - expected) / expected) <= 1e-12.
"""
from decimal import Decimal
from math import fabs, expm1, log1p
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def f(x):
    return float((Decimal(1) + Decimal(x)) ** Decimal(0.5) - 1)


def f2(x):
    return expm1(log1p(x) / 2)


def run_tests():
    with Test() as test:

        def assertFuzzyEquals(actual, expected, msg=""):
            # max error
            merr = 1e-12
            if expected == 0:
                inrange = fabs(actual) <= merr
            else:
                e = fabs((actual - expected) / expected)
                inrange = e <= merr
            if msg == "":
                msg = "Expected value near {:.16e}, but got {:.16e}. Relative error: {:.16e}"
                msg = msg.format(expected, actual, e)
            return test.expect(inrange, msg)

        test.describe("f")
        test.it("Basic tests")
        assertFuzzyEquals(f(2.6e-08), 1.29999999155e-08)
        assertFuzzyEquals(f(1.4e-09), 6.999999997549999e-10)
        assertFuzzyEquals(f(5.0e-06), 2.499996875007812e-06)
        assertFuzzyEquals(f(2.4e-07), 1.1999999280000085e-07)


if __name__ == '__main__':
    run_tests()
