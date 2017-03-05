"""
The Fibonacci sequence is traditionally used to explain tree recursion.

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

This algorithm serves welll its educative purpose but it's tremendously inefficient,
not only because of recursion, but because we invoke the fibonacci function twice,
and the right branch of recursion (i.e. fibonacci(n-2)) recalculates all the Fibonacci
numbers already calculated by the left branch (i.e. fibonacci(n-1)).

This algorithm is so inefficient that the time to calculate any Fibonacci number
over 50 is simply too much. You may go for a cup of coffee or go take a nap while
you wait for the answer. But if you try it here in Code Wars you will most likely
get a code timeout before any answers.

For this particular Kata we want to implement the memoization solution. This will
be cool because it will let us keep using the tree recursion algorithm while still
keeping it sufficiently optimized to get an answer very rapidly.

The trick of the memoized version is that we will keep a cache data structure
(most likely an associative array) where we will store the Fibonacci numbers as
we calculate them. When a Fibonacci number is calculated, we first look it up in
the cache, if it's not there, we calculate it and put it in the cache, otherwise
we returned the cached number.

Refactor the function into a recursive Fibonacci function that using a memoized
data structure avoids the deficiencies of tree recursion Can you make it so the
memoization cache is private to this function?
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


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
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Binet's formula
def fib_formula(n):
    sqf = 5 ** .5
    phip = (1 + sqf) / 2
    phim = (1 - sqf) / 2
    return int(((phip ** n) - (phim ** n)) / sqf)


def run_tests():
    with Test() as test:
        test.describe('Kata Test Suite')
        test.it('should calculate large Fibonacci numbers')
        test.assert_equals(fibonacci(50), 12586269025)
        test.assert_equals(fibonacci(60), 1548008755920)
        test.assert_equals(fibonacci(70), 190392490709135)
        test.assert_equals(fibonacci(80), 23416728348467685)
        test.assert_equals(fibonacci(90), 2880067194370816120)
        test.assert_equals(fibonacci(100), 354224848179261915075)
        test.assert_equals((fibonacci(150)), 9969216677189303386214405760200)
        f300 = 222232244629420445529739893461909967206666939096499764990979600
        test.assert_equals(fibonacci(300), f300)

        test.describe('Producing the fibonacci sequence with formula')
        test.it('should approximate large Fibonacci numbers')
        test.assert_equals(fib_formula(50), 12586269025)
        test.assert_equals(fib_formula(60), 1548008755920)
        test.assert_equals(fib_formula(70), 190392490709135)
        test.assert_equals(fib_formula(80), 23416728348467685)
        test.assert_equals(fib_formula(90), 2880067194370816120)
        test.assert_equals(fib_formula(100), 354224848179261915075)
        test.assert_equals((fib_formula(150)), 9969216677189303386214405760200)
        f300 = 222232244629420445529739893461909967206666939096499764990979600
        test.assert_equals(fib_formula(300), f300)


if __name__ == '__main__':
    run_tests()
