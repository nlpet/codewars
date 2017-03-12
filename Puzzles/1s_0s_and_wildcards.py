"""
1s and 0s and wildcards

You are given a string containing 0's, 1's and one or more '?', where ? is a
wildcard that can be 0 or 1.

Return an array containing all the possibilities you can reach substituing the
? for a value.

Examples:

'101?' -> ['1010', '1011']
'1?1?' -> ['1010', '1110', '1011', '1111']
"""
from itertools import combinations
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


# TODO(fix): too slow, tests on codewars time out
def possibilities(strng):
    sl = list(strng)
    indices = [i for i, x in enumerate(sl) if x == '?']
    li = len(indices)
    results = []
    for cmb in set(combinations('01' * li, li)):
        res = sl[:]
        for i, ix in enumerate(indices):
            res[ix] = cmb[i]
        results.append(''.join(res))
    return results


def run_tests():
    with Test() as test:
        test.describe("basic tests")

        t1 = possibilities('101?')
        t1.sort()
        test.assert_equals(t1, ['1010', '1011'])

        t2 = possibilities('10??')
        t2.sort()
        test.assert_equals(t2, ['1000', '1001', '1010', '1011'])

        t3 = possibilities('1?1?')
        t3.sort()
        test.assert_equals(t3, ['1010', '1011', '1110', '1111'])


if __name__ == '__main__':
    run_tests()
