"""
Strings Mix

Given two strings s1 and s2, we want to visualize how different the two strings
are. We will only take into account the lowercase letters (a to z). First let
us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2.
In the following we will not consider letters when the maximum of their occurrences
is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb"
where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4.
In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears
as many times as its maximum if this maximum is strictly greater than 1; these
letters will be prefixed by the number of the string where they appear with their
maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh;
it contains the prefix) will be in decreasing order of their length and
when they have the same length sorted in ascending lexicographic order
(letters and digits - more precisely sorted by codepoint); the different
groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
"""
from collections import Counter, defaultdict
import re
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def merge_dicts_highest_count(d1, d2):
    merged = {}
    for k in set(d1.keys()).union(d2.keys()):
        if d1.get(k, 0) >= d2.get(k, 0):
            merged[k] = d1[k]
        else:
            merged[k] = d2[k]

    return merged


def mix(s1, s2):
    s1 = ''.join(re.findall(r'[a-z]', s1))
    s2 = ''.join(re.findall(r'[a-z]', s2))
    c1 = dict(filter(lambda t: t[1] > 1, Counter(s1).items()))
    c2 = dict(filter(lambda t: t[1] > 1, Counter(s2).items()))
    merged = merge_dicts_highest_count(c1, c2)
    reverse_common = defaultdict(str)
    first = []
    second = []
    common = defaultdict(str)
    res = ''

    for k, v in merged.items():
        reverse_common[v] += k

    for count, ws in sorted(reverse_common.items(), key=lambda t: t[0], reverse=True):
        for ch in sorted(ws):
            if c1.get(ch) == count and c2.get(ch) == count:
                common[count] += ch
            elif c1.get(ch) == count:
                first.append((count, ch * count))
            else:
                second.append((count, ch * count))

    while first or second:
        if first and second:
            if first[0][0] >= second[0][0]:
                res += '1:{}/'.format(first[0][1])
                first.pop(0)
            else:
                res += '2:{}/'.format(second[0][1])
                second.pop(0)
        elif first:
            res += '1:{}/'.format(first[0][1])
            first.pop(0)
        else:
            res += '2:{}/'.format(second[0][1])
            second.pop(0)

    for count, ws in sorted(common.items(), key=lambda t: t[0], reverse=True):
        for ch in ws:
            res += '=:{}/'.format(count * ch)

    return res[:-1]


def run_tests():
    with Test() as test:
        test.describe("Mix")
        test.it("Basic tests")
        test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        test.assert_equals(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        test.assert_equals(mix("codewars", "codewars"), "")
        test.assert_equals(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")


if __name__ == '__main__':
    run_tests()
