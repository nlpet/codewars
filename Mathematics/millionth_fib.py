"""
The Millionth Fibonacci Kata

The year is 1214. One night, Pope Innocent III awakens to find the the archangel
Gabriel floating before him. Gabriel thunders to the pope:

Gather all of the learned men in Pisa, especially Leonardo Fibonacci.
In order for the crusades in the holy lands to be successful, these men must
calculate the millionth number in Fibonacci's recurrence. Fail to do this,
and your armies will never reclaim the holy land. It is His will.
The angel then vanishes in an explosion of white light.

Pope Innocent III sits in his bed in awe. How much is a million? he thinks to
himself. He never was very good at math.

He tries writing the number down, but because everyone in Europe is still
using Roman numerals at this moment in history, he cannot represent this number.
If he only knew about the invention of zero, it might make this sort of thing easier.

He decides to go back to bed. He consoles himself, The Lord would never challenge
me thus; this must have been some deceit by the devil. A pretty horrendous
nightmare, to be sure.

Pope Innocent III's armies would go on to conquer Constantinople
(now Istanbul), but they would never reclaim the holy land as he desired.

In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n where 1000000 ≤ n ≤ 1500000.
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def fib_helper(n):
    if n == 0:
        return (0, 1)

    div, rem = divmod(n, 2)
    fibn, fibnp1 = fib_helper(div)

    fib2n = 2 * fibn * fibnp1 - fibn * fibn
    fib2np1 = fibn * fibn + fibnp1 * fibnp1

    if rem:
        return (fib2np1, fib2n + fib2np1)
    return (fib2n, fib2np1)


def fib(n):
    if n < 0:
        if n % 2 == 0:
            return -fib_helper(-n)[0]
        return fib_helper(-n)[0]
    return fib_helper(n)[0]


def run_tests():
    with Test() as test:
        test.describe("Basic tests")
        test.it("Verifying that fib(0) == 0")
        test.assert_equals(fib(0), 0)

        test.it("Verifying that fib(1) == 1")
        test.assert_equals(fib(1), 1)

        test.it("Verifying that fib(2) == 1")
        test.assert_equals(fib(2), 1)

        test.it("Verifying that fib(3) == 2")
        test.assert_equals(fib(3), 2)

        test.it("Verifying that fib(4) == 3")
        test.assert_equals(fib(4), 3)

        test.it("Verifying that fib(5) == 5")
        test.assert_equals(fib(5), 5)

        test.it("Verifying that fib(-4) == -3")
        test.assert_equals(fib(-4), -3)

        test.it("Verifying that fib(-81) == -37889062373143906")
        test.assert_equals(fib(-81), 37889062373143906)


if __name__ == '__main__':
    run_tests()
