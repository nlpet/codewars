"""
Running Average

Create a function running_average() that returns a callable function object.
Update the series with each given value and calculate the current average.

r_avg = running_average()
r_avg(10) = 10.0
r_avg(11) = 10.5
r_avg(12) = 11
All input values are valid. Round to two decimal places.

This Kata is based on a example from Fluent Python book.
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def running_average():
    cache = {'sum': 0, 'length': 0}

    def r_avg(n):
        cache['sum'] += n
        cache['length'] += 1
        return round(cache['sum'] / cache['length'], 2)

    return r_avg


def run_tests():
    with Test() as test:
        test.it('Basic tests')

        r_avg = running_average()

        test.assert_equals(r_avg(10), 10)
        test.assert_equals(r_avg(11), 10.5)
        test.assert_equals(r_avg(12), 11)

if __name__ == '__main__':
    run_tests()
