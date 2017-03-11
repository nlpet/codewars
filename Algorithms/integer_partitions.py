"""
Getting along with Integer Partitions

From wikipedia https://en.wikipedia.org/wiki/Partition_(number_theory)

In number theory and combinatorics, a partition of a positive integer n,
also called an integer partition, is a way of writing n as a sum of positive
integers. Two sums that differ only in the order of their summands are
considered the same partition.

For example, 4 can be partitioned in five distinct ways:

4, 3 + 1, 2 + 2, 2 + 1 + 1, 1 + 1 + 1 + 1.

We can write:

enum(4) -> [[4],[3,1],[2,2],[2,1,1],[1,1,1,1]] and

enum(5) -> [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]].

The number of parts in a partition grows very fast. For n = 50 number of
parts is 204226, for 80 it is 15,796,476 It would be too long to tests answers
with arrays of such size. So our task is the following:

1 - n being given (n integer, 1 <= n <= 50) calculate enum(n) ie the partition
of n. We will obtain something like that:
enum(n) -> [[n],[n-1,1],[n-2,2],...,[1,1,...,1]] (order of array and sub-arrays
doesn't matter). This part is not tested.

2 - For each sub-array of enum(n) calculate its product. If n = 5 we'll obtain
after removing duplicates and sorting:

prod(5) -> [1,2,3,4,5,6]

prod(8) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 18]

If n = 40 prod(n) has a length of 2699 hence the tests will not verify
such arrays. Instead our task number 3 is:

3 - return the range, the average and the median of prod(n) in the following
form (example for n = 5):

"Range: 5 Average: 3.50 Median: 3.50"

Range is an integer, Average and Median are float numbers rounded to two
decimal places (".2f" in some languages).
"""
from functools import reduce
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def mean(arr, n):
    return sum(arr) / n


def median(arr, n):
    if n % 2 == 0:
        return (arr[(n - 1) // 2] + arr[n // 2]) / 2
    else:
        return arr[n // 2]


def prod(partitions):
    prods = set()
    prod = lambda x, y: x * y
    for sublist in partitions:
        prods.add(reduce(prod, sublist))
    return sorted(list(prods))


def calculate_stats(partitions):
    sprods = prod(partitions)
    l = len(sprods)
    template = 'Range: {:d} Average: {:.2f} Median: {:.2f}'
    return template.format(sprods[-1] - sprods[0], mean(sprods, l), median(sprods, l))


def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function


@memoize
def get_partitions(n):
    partitions = [[()], [(1,)]]
    for num in range(2, n + 1):
        parts = set()
        for i in range(num):
            for p in partitions[i]:
                parts.add(tuple(sorted((num - i, ) + p)))
        partitions.append(list(parts))
    return partitions[n]


def part(n):
    partitions = get_partitions(n)
    return calculate_stats(partitions)


def run_tests():
    with Test() as test:
        test.describe("Basic tests")
        test.it("Small numbers")

        test.assert_equals(part(1), "Range: 0 Average: 1.00 Median: 1.00")
        test.assert_equals(part(2), "Range: 1 Average: 1.50 Median: 1.50")
        test.assert_equals(part(3), "Range: 2 Average: 2.00 Median: 2.00")
        test.assert_equals(part(4), "Range: 3 Average: 2.50 Median: 2.50")
        test.assert_equals(part(5), "Range: 5 Average: 3.50 Median: 3.50")


if __name__ == '__main__':
    run_tests()
