"""
Simple Fun #177: Rank Of Element

Task

Given an array arr, find the rank of the element at the ith position.

The rank of the arr[i] is a value equal to the number of elements less than or
equal to arr[i] standing before arr[i], plus the number of elements less than
arr[i] standing after arr[i].
Example

For arr = [2,1,2,1,2], i = 2, the result should be 3.

There are 2 elements less than or equal to arr[2] standing before arr[2]:

arr[0] <= arr[2]

arr[1] <= arr[2]

There is only 1 element less than arr[2] standing after arr[2]:

arr[3] <= arr[2]

So the result is 2 + 1 = 3.
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def rank_of_element(arr, i):
    lt = len(list(filter(lambda x: x <= arr[i], arr[:i])))
    gt = len(list(filter(lambda x: x < arr[i], arr[i + 1:])))
    return lt + gt


def run_tests():
    with Test() as test:
        test.describe("Basic tests")
        test.assert_equals(rank_of_element([2, 1, 2, 1, 2],2),3)
        test.assert_equals(rank_of_element([2, 1, 2, 2, 2],2),2)
        test.assert_equals(rank_of_element([3, 2, 3, 4, 1],0),2)
        test.assert_equals(rank_of_element([3, 2, 3, 4, 1],1),1)
        test.assert_equals(rank_of_element([3, 2, 3, 4, 1],2),3)


if __name__ == '__main__':
    run_tests()
