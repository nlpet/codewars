"""
John and Ann sign up for Codewars

John and his wife Ann have decided to go to Codewars.

On day 0 Ann will do one kata and John - he wants to know how it is working - 0.

Let us call a(n) the number of katas done by Ann at day n we have
a(0) = 1 and in the same manner j(0) = 0.

They have chosen the following rules:

On day n the number of katas done by Ann should be n minus the number of katas
done by John at day t, t being equal to the number of katas done by Ann
herself at day n - 1.
On day n the number of katas done by John should be n minus the number of katas
done by Ann at day t, t being equal to the number of katas done by John
himself at day n - 1.

Whoops! I think they need to lay out a little clearer exactly what
there're getting themselves into!

Could you write:

1) two functions ann and john (parameter n) giving the list of the
numbers of katas Ann and John should take on each day from day 0 to
day n - 1 (n days - see first example below)?
2) The total number of katas taken by ann (function sum_ann(n)) and john
(function sum_john(n)) from day 0 (inclusive) to day n (exclusive)?

Examples:

john(11) -->  [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]
ann(6) -->  [1, 1, 2, 2, 3, 3]

sum_john(75) -->  1720
sum_ann(150) -->  6930
Note: Keep an eye on performance.

WORK IN PROGRESS
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test

ANN = [1, 1]
JOHN = [0, 0]



def john(n):
    if n < 2:
        return 0
    else:
        return [] + [n - ann(john(n - 1))]

def ann(n):
    if n < 2:
        return 1
    else:
        return [] + [n - john(ann(n - 1))]


def sum_john(n):
    pass

def sum_ann(n):
    pass



def run_tests():
    with Test() as test:
        def testJohn(n, res):
            test.assert_equals(john(n), res)

        def testAnn(n, res):
            test.assert_equals(ann(n), res)

        def testSumJohn(n, res):
            test.assert_equals(sum_john(n), res)

        def testSumAnn(n, res):
            test.assert_equals(sum_ann(n), res)

        test.describe("john")
        test.it("Basic tests")
        testJohn(11, [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6])

        test.describe("ann")
        test.it("Basic tests")
        testAnn(6, [1, 1, 2, 2, 3, 3])

        test.describe("sum_ann")
        test.it("Basic tests")
        testSumAnn(115, 4070)

        test.describe("sum_john")
        test.it("Basic tests")
        testSumJohn(75, 1720)




if __name__ == '__main__':
    run_tests()
