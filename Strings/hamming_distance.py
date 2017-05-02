"""
Simple Fun #141: Hamming Distance

Task

The hamming distance between a pair of numbers is the number of binary bits that differ in their binary notation.

Example

For a = 25, b= 87, the result should be 4

25: 00011001
87: 01010111
The hamming distance between these two would be 4 ( the 2nd, 5th, 6th, 7th bit ).

Input/Output

[input] integer a

First Number. 1 <= a <= 2^20
[input] integer b

Second Number. 1 <= b <= 2^20
[output] an integer

Hamming Distance
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def hamming_distance(n1, n2):
    n1 = bin(n1)[2:]
    n2 = bin(n2)[2:]
    ln1, ln2 = len(n1), len(n2)

    if ln1 > ln2:
        n2 = n2.zfill(ln1)
    else:
        n1 = n1.zfill(ln2)

    return sum([1 for x, y in zip(n1, n2) if x != y])


def short_hamm_distance(n1, n2):
    return bin(n1 ^ n2).count('1')


def run_tests():
    with Test() as test:
        test.it("Basic tests")
        test.assert_equals(hamming_distance(25, 87), 4)
        test.assert_equals(hamming_distance(256, 302), 4)
        test.assert_equals(hamming_distance(543, 634), 4)
        test.assert_equals(hamming_distance(34013, 702), 7)


if __name__ == '__main__':
    run_tests()
