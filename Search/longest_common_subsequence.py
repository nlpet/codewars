"""
Longest Common Subsequence problem on codewars.com.

Write a function called LCS that accepts two sequences, and
returns the longest subsequence common to the passed in sequences.

Subsequence

A subsequence is different from a substring. The terms of a
subsequence need not be consecutive terms of the original sequence.

Example subsequence

Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc"

LCS examples

lcs( "abcdef" , "abc" ) => returns "abc"
lcs( "abcdef" , "acf" ) => returns "acf"
lcs( "132535365" , "123456789" ) => returns "12356"


Notes

* Both arguments will be strings
* Return value must be a string
* Return an empty string if there exists no common subsequence
* Both arguments will have one or more characters (in JavaScript)
* All tests will only have a single longest common subsequence.
* Don't worry about cases such as LCS( "1234", "3412" ), which
  would have two possible longest common subsequences: "12" and "34".

"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


# Recursive solution
def lcsr(ox, oy):
    if not ox or not oy:
        return ''
    x, xs, y, ys = ox[0], ox[1:], oy[0], oy[1:]
    if x == y:
        return x + lcsr(xs, ys)
    else:
        return max(lcsr(ox, ys), lcsr(xs, oy), key=len)


# Dynamic Programming solution
def lcsd(xs, ys):
    lx, ly = len(xs), len(ys)
    result = []
    lengths = [[0] * (ly + 1) for _ in range(lx + 1)]

    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

    while lx > 0 and ly > 0:
        if lengths[lx][ly] == lengths[lx - 1][ly]:
            lx -= 1
        elif lengths[lx][ly] == lengths[lx][ly - 1]:
            ly -= 1
        else:
            result.insert(0, xs[lx - 1])
            lx -= 1
            ly -= 1
    return ''.join(result)


def run_tests():
    with Test() as test:
        test.describe('Recursive solution')
        test.it('Finds the longest common subsequence between two strings')
        test.assert_equals(lcsr("a", "b"), "")
        test.assert_equals(lcsr("abcdef", "abc"), "abc")
        test.assert_equals(lcsr("abcdef", "acf"), "acf")
        test.assert_equals(lcsr("132535365", "123456789"), "12356")
        test.assert_equals(lcsr("132535365", "123456789"), "12356")
        test.assert_equals(lcsr("XMJYAUZ", "MZJAWXU"), "MJAU")

    with Test() as test:
        test.describe('Dynamic Programming solution')
        test.it('Finds the longest common subsequence between two strings')
        test.assert_equals(lcsd("a", "b"), "")
        test.assert_equals(lcsd("abcdef", "abc"), "abc")
        test.assert_equals(lcsd("abcdef", "acf"), "acf")
        test.assert_equals(lcsd("132535365", "123456789"), "12356")
        test.assert_equals(lcsd("132535365", "123456789"), "12356")
        test.assert_equals(lcsd("XMJYAUZ", "MZJAWXU"), "MJAU")


if __name__ == '__main__':
    run_tests()
