"""A disguised sequence (I)"""

from helpers.test_wrapper import Test

import sys
sys.path.append('..')


def fcn(n):
    f, s = 1, 2
    for _ in range(2, n + 1):
        nxt = (6 * f * s) // (5 * f - s)
        f, s = s, nxt
    return nxt


def fcn_bitwise(n):
    return 1 << n  # x << n == x * 2 ** n


def run_tests():
    with Test() as test:
        test.describe("fcn")
        test.it("Basic tests")
        test.assert_equals(fcn(17), 131072)
        test.assert_equals(fcn(21), 2097152)
        test.assert_equals(fcn(14), 16384)
        test.assert_equals(fcn(43), 8796093022208)
        test.assert_equals(fcn(19), 524288)

    with Test() as test:
        test.describe("fcn")
        test.it("Bitwise tests")
        test.assert_equals(fcn_bitwise(17), 131072)
        test.assert_equals(fcn_bitwise(21), 2097152)
        test.assert_equals(fcn_bitwise(14), 16384)
        test.assert_equals(fcn_bitwise(43), 8796093022208)
        test.assert_equals(fcn_bitwise(19), 524288)


if __name__ == '__main__':
    run_tests()
