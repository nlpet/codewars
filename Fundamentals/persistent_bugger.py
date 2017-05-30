"""
Persistent Bugger

Write a function, persistence, that takes in a positive parameter num and
returns its multiplicative persistence, which is the number of times you
must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
"""
from functools import reduce
from operator import mul

import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def persistence(n, p=0):
    sn = str(n)
    digits = [int(i) for i in sn]
    if len(digits) == 1:
        return p
    else:
        return persistence(reduce(mul, digits), p + 1)


def run_tests():
    with Test() as test:
        test.it("Basic tests")
        test.assert_equals(persistence(39), 3)
        test.assert_equals(persistence(4), 0)
        test.assert_equals(persistence(25), 2)
        test.assert_equals(persistence(999), 4)

if __name__ == '__main__':
    run_tests()
