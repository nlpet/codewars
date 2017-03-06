"""
Character with longest repetition

For a given string s find the character c with longest consecutive repetition
and return a tuple (c, l) (in Haskell Just (Char, Int), in C# Tuple<char?, int>,
in Shell a String of comma-separated values c,l) where l is the length of the
repetition. If there are two or more characters with the same l return the first.
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def longest_repetition(s):
    if not s:
        return ('', 0)

    longest = ('', 0)
    current, count = '', 0
    for ch in s:
        if ch == current:
            count += 1
        else:
            if count > longest[1]:
                longest = (current, count)
            current = ch
            count = 1
    if count > longest[1]:
        longest = (current, count)
    return longest


def longest_repetition2(chars):
    from itertools import groupby
    return max(((char, len(list(group))) for char, group in groupby(chars)),
               key=lambda char_group: char_group[1], default=("", 0))


def longest_repetition3(s):
    import re
    if not s:
        return ("", 0)

    longest = max(re.findall(r"((.)\2*)", s), key=lambda x: len(x[0]))
    return (longest[1], len(longest[0]))


def run_tests():
    with Test() as test:
        test.describe("Example Tests")

        tests = [
            # [input, expected],
            ["aaaabb", ('a', 4)],
            ["bbbaaabaaaa", ('a', 4)],
            ["cbdeuuu900", ('u', 3)],
            ["abbbbb", ('b', 5)],
            ["aabb", ('a', 2)],
            ["ba", ('b', 1)],
            ["", ('', 0)],
        ]

        for inp, exp in tests:
            test.assert_equals(longest_repetition(inp), exp)


if __name__ == '__main__':
    run_tests()
