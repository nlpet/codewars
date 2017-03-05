"""
Simple Fun #176: Reverse Letter.

Task

Given a string str, reverse it omitting all non-alphabetic characters.
Example

For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".
Input/Output

[input] string str

A string consists of lowercase latin letters, digits and symbols.
[output] a string
"""
import re
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def reverse_letter(strng):
    alphabetic = re.findall(r'[A-z]', strng)
    return ''.join(alphabetic[::-1])


def run_tests():
    with Test() as test:
        test.describe("Basic Tests")
        test.it("It should works for basic tests.")

        test.assert_equals(reverse_letter("krishan"), "nahsirk")
        test.assert_equals(reverse_letter("ultr53o?n"), "nortlu")
        test.assert_equals(reverse_letter("ab23c"), "cba")
        test.assert_equals(reverse_letter("krish21an"), "nahsirk")


if __name__ == '__main__':
    run_tests()
