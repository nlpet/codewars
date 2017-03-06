"""
Is my friend cheating?

https://www.codewars.com/kata/is-my-friend-cheating
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def removNb(n):
    solutions = []
    s = (n * (n + 1)) / 2
    l = ((n - 1) * n / 2) / (n + 1)
    h = (s + 1) ** .5 - 1

    for i in range(int(h), int(l - 1), -1):
        n = int((s - i) / (i + 1))
        if i * n + i + n == s:
            solutions.extend([(i, n), (n, i)])
    return sorted(solutions, key=lambda t: t[0])


def run_tests():
    with Test() as test:
        test.assert_equals(removNb(100), [])
        test.assert_equals(removNb(26), [(15, 21), (21, 15)])


if __name__ == '__main__':
    run_tests()
