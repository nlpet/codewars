u"""
Square into Squares. Protect trees!

My little sister came back home from school with the following task: given
a squared sheet of paper she has to cut it in pieces which, when assembled,
give squares the sides of which form an increasing sequence of numbers. At
the beginning it was lot of fun but little by little we were tired of seeing
the pile of torn paper. So we decided to write a program that could help us
and protects trees.

Task

Given a positive integral number n, return a strictly increasing sequence
(list/array/string depending on the language) of numbers, so that the sum of
the squares is equal to n².

If there are multiple solutions (and there will be), return the result with
the largest possible values:

Examples

decompose(11) must return [1,2,4,10]. Note that there are actually two ways to
decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't
return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since
[1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

Note

Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists,
return nil, null, Nothing, None
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def subset_sum(nums, target, part=[], solutions=[]):
    s = sum(part)
    if s == target:
        solutions.append(list(map(lambda x: int(x ** .5), part)))
    if s >= target:
        return

    for i in range(len(nums)):
        remaining = nums[i + 1:]
        subset_sum(remaining, target, part + [nums[i]])

    return solutions


# very slow for larger n
def decompose2(n):
    squares = [x ** 2 for x in range(1, n)]
    subset_sums = subset_sum(squares, n ** 2)
    return max(subset_sums, key=lambda lst: lst[-1])


def decompose(n):
    def _decompose(sq, num):
        if sq < 0:
            return None
        elif sq == 0:
            return []
        for j in range(num - 1, 0, -1):
            sub = _decompose(sq - j ** 2, j)
            if sub is not None:
                return sub + [j]
    return _decompose(n ** 2, n)


def run_tests():
    with Test() as test:
        test.assert_equals(decompose(5), [3, 4])
        test.assert_equals(decompose(11), [1, 2, 4, 10])
        test.assert_equals(decompose(50), [1, 3, 5, 8, 49])

if __name__ == '__main__':
    run_tests()
