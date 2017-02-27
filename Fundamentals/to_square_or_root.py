"""
To square(root) or not to square(root)

Write a method, that will get an integer array as parameter and will process
every number from this array.

Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

[4,3,9,7,2,1] -> [2,9,3,49,4,1]
"""
from math import sqrt


def square_or_square_root(arr):
    res = lambda n: int(sqrt(n)) if sqrt(n).is_integer() else n ** 2
    return [res(n) for n in arr]


if __name__ == '__main__':
    tests = [
        [[4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]],
        [[100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]],
        [[1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]],
    ]

    for inp, exp in tests:
        assert(square_or_square_root(inp) == exp)
