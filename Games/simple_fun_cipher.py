"""
Simple Fun #49: Decipher.

Task

Consider the following ciphering algorithm:

For each character replace it with its code.
Concatenate all of the obtained numbers.
Given a ciphered string, return the initial one if it is known that it
consists only of lowercase letters.

Note: here the character's code means its decimal ASCII code, the numerical
representation of a character used by most modern programming languages.
Example

For cipher = "10197115121", the output should be "easy".

Explanation:

charCode('e') = 101,
charCode('a') = 97,
charCode('s') = 115
charCode('y') = 121.
"""

import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def decipher(cipher):
    plaintext, i, lch, ls = [], 0, 0, len(cipher)
    while i < ls:
        if cipher[i] == '1':
            lch = 3
        else:
            lch = 2
        plaintext.append(chr(int(cipher[i: i + lch])))
        i += lch
    return ''.join(plaintext)


def run_tests():
    with Test() as test:
        test.describe('Basic Tests')
        test.it('It should works for basic tests.')
        test.assert_equals(decipher("10197115121"), "easy")
        test.assert_equals(decipher("98"), "b")
        test.assert_equals(decipher("122"), "z")


if __name__ == '__main__':
    run_tests()
