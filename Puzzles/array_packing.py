u"""
Simple Fun #9: Array Packing

Task

You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M as unsigned integer.

Note:
the phrase "first bits of M" refers to the least significant bits of M - the
right-most bits of an integer. For further clarification see the following example.
Example

For a = [24, 85, 0], the output should be 21784

An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.

After packing these into one number we get 00000000 01010101 00011000
(spaces are placed for convenience), which equals to 21784.
Input/Output

[input] integer array a
Constraints: 1 ≤ a.length ≤ 4 and 0 ≤ a[i] < 256

[output] an unsigned integer
More Challenge

Are you a One-Liner? Please try to complete the kata in one line(no test for it) ;-)
"""
from functools import reduce
from operator import add
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def array_packing(a):
    return int(reduce(add, (map(lambda x: '{0:08b}'.format(x), a[::-1]))), 2) if a else 0


def run_tests():
    with Test() as test:
        test.describe("Basic tests")
        test.assert_equals(array_packing([24, 85, 0]), 21784)
        test.assert_equals(array_packing([23, 45, 39]), 2567447)
        test.assert_equals(array_packing([1, 1]), 257)
        test.assert_equals(array_packing([0]), 0)
        test.assert_equals(array_packing([]), 0)
        test.assert_equals(array_packing([255, 255, 255, 255]), 4294967295)


if __name__ == '__main__':
    run_tests()
