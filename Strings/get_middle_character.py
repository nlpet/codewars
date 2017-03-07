"""
Get the Middle Character



You are going to be given a word. Your job is to return the middle character of
the word. If the word's length is odd, return the middle character. If the word's
length is even, return the middle 2 characters.

Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def get_middle(s):
    n = len(s)
    if n % 2 == 0:
        return s[n // 2 - 1: n // 2 + 1]
    else:
        return s[n // 2]


def run_tests():
    with Test() as test:
        test.assert_equals(get_middle("test"), "es")
        test.assert_equals(get_middle("testing"), "t")
        test.assert_equals(get_middle("middle"), "dd")
        test.assert_equals(get_middle("A"), "A")
        test.assert_equals(get_middle("of"), "of")


if __name__ == '__main__':
    run_tests()
