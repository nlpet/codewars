"""
Perfect power problem on codewars.

URL: https://www.codewars.com/kata/whats-a-perfect-power-anyway
"""
import sys
sys.path.append('..')

from codewars.helpers.test_wrapper import Test
from random import random, randrange
from math import log, floor, sqrt


def is_pp(n):
    for m in range(2, int(sqrt(n) + 1)):
        k = int(round(log(n, m)))
        if m ** k == n:
            return [m, k]
    return None


def run_tests():
    with Test() as test:
        test.describe("perfect powers")
        test.it("should work for some examples")
        test.assert_equals(is_pp(4), [2, 2], "4 = 2^2")
        test.assert_equals(is_pp(9), [3, 2], "9 = 3^2")
        test.assert_equals(is_pp(5), None, "5 isn't a perfect power")

        test.it("should work for the first perfect powers")
        pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81,
              100, 121, 125, 128, 144, 169, 196, 216,
              225, 243, 256, 289, 324, 343, 361, 400, 441, 484]
        for item in pp:
            msg = "the perfect power " + str(item) + " wasn't recognized as one"
            test.expect(is_pp(item) is not None, msg)

        test.it("should work for random perfect powers")
        for i in range(100):
            m = 2 + floor(random() * 255)
            k = 2 + floor(random() * log(268435455) / log(m))
            l = m ** k
            r = is_pp(l)
            if r is None:
                test.expect(r is not None, str(l) + " is a perfect power")
                break
            elif r[0] ** r[1] != l:
                msg = "your pair ({}, {}) doesn't work for {}".format(r[0], r[1], l)
                test.assert_equals(r[0] ** r[1], l, msg)
                break

        test.it("should return valid pairs for random inputs")
        for i in range(100):
            l = randrange(65535)
            r = is_pp(l)
            if r is not None and r[0] ** r[1] != l:
                msg = "your pair ({}, {}) doesn't work for {}".format(r[0], r[1], l)
                test.assert_equals(r[0] ** r[1], l, msg)
                break


if __name__ == '__main__':
    run_tests()
