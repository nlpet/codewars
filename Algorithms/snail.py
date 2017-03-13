"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def snail(arr):
    n = len(arr)
    unrolled = []

    st, fi = 0, n

    while fi - st > 1:
        forw, back = [], []
        forw.extend(arr[st][st: fi])

        for i in range(st + 1, fi - 1):
            forw.append(arr[i][fi - 1])
            back.append(arr[i][st])

        back += arr[fi - 1][st: fi]
        unrolled.extend(forw + list(reversed(back)))
        st, fi = st + 1, fi - 1

    return unrolled + arr[st][st: fi]


def run_tests():
    with Test() as test:
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        test.assert_equals(snail(array), expected)

        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        test.assert_equals(snail(array), expected)

        array = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]

        expected = [1, 2, 3, 4, 5, 10, 15, 20,
                    25, 24, 23, 22, 21, 16, 11, 6,
                    7, 8, 9, 14, 19, 18, 17, 12, 13]
        test.assert_equals(snail(array), expected)


if __name__ == '__main__':
    run_tests()
