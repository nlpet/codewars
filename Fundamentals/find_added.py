"""
Ease the Stockbroker

URL: https://www.codewars.com/kata/ease-the-stockbroker
"""
from collections import Counter
from helpers.test_wrapper import Test
import sys
sys.path.append('..')


def findAdded(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    result = []

    for num, c in c2.items():
        if num not in c1:
            result.extend([num] * c)
        elif c > c1[num]:
            result.extend([num] * (c - c1[num]))
    return ''.join(sorted(result))


def findAdded2(st1, st2):
    return ''.join(sorted((Counter(st2) - Counter(st1)).elements()))


def run_tests():
    with Test() as test:
        test.assert_equals(
            findAdded('44554466', '447554466'), '7', "Expected  '7'")
        test.assert_equals(findAdded('9876521', '9876543211'),
                           '134', "Expected  '134'")
        test.assert_equals(findAdded('4455446', '447555446666'),
                           '56667', "Expected  '56667'")
        test.assert_equals(findAdded('678', '876'), '', "Expected  ''")
        test.assert_equals(findAdded('678', '6'), '', "Expected  ''")


if __name__ == '__main__':
    run_tests()
