"""
Matrix Determinant

Write a function that accepts a square matrix (n x n 2D array) and returns the
determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the
smallest cases: A 1x1 matrix |a| has determinant a. A 2x2 matrix [[a, b], [c, d]] or

|a b|
|c d|

has determinant ad - bc.

The determinant of an n x n sized matrix is calculated by reducing the problem
to the calculation of the determinants of n n-1 x n-1 matrices. For the 3x3
case, [[a, b, c], [d, e, f], [g, h, i]] or

|a b c|
|d e f|
|g h i|

the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor)
where det(a_minor) refers to taking the determinant of the 2x2 matrix created
by crossing out the row and column in which the element a occurs, or

|e f|
|h i|

Note the alternation of signs.

The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4
matrix with first row [a, b, c, d], det(M) = a * det(a_minor) - b * det(b_minor)
+ c * det(c_minor) - d * det(d_minor)
"""
from math import pow
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def determinant(mx, mul=1):
    n = len(mx)
    if n == 1:
        return mul * mx[0][0]
    else:
        total = 0
        for i in range(n):
            new_mx = [
                [mx[j][k] for k in range(n) if k != i]
                for j in range(1, n)
            ]
            total += mul * determinant(new_mx, pow(-1, i + 2) * mx[0][i])
        return total


def run_tests():
    with Test() as test:
        m1 = [[1, 3], [2, 5]]
        m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]

        msg = "Determinant of a 1 x 1 matrix yields the value of the one element"
        test.assert_equals(determinant([[1]]), 1, msg)
        test.assert_equals(determinant(m1), -1, "Should return 1 * 5 - 3 * 2, i.e., -1 ")
        test.expect(determinant(m2) == -20)


if __name__ == '__main__':
    run_tests()
