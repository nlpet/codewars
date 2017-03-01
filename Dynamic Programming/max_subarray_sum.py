"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous
subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum
is the sum of the whole array. If the list is made up of only negative numbers,
return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array
is also a valid sublist/subarray.
"""


def max_sequence(arr):
    if not arr or max(arr) < 0:
        return 0
    elif min(arr) >= 0:
        return sum(arr)
    else:
        max_sum, curr_max_sum = 0, arr[0]
        for i in range(1, len(arr)):
            curr_max_sum = max(arr[i], curr_max_sum + arr[i])
            if curr_max_sum > max_sum:
                max_sum = curr_max_sum
    return max_sum
