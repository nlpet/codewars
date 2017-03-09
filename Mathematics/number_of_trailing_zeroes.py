"""
Write a program that will calculate the number of trailing zeros in
a factorial of a given number.

N! = 1 * 2 * 3 * 4 ... N

zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600
that has 2 trailing zeros 4790016(00)
Be careful 1000! has length of 2568 digital numbers.
"""


def zeros(n):
    zeroes = 0
    pows = 5
    while n // pows > 0:
        zeroes += n // pows
        pows *= 5
    return zeroes


if __name__ == '__main__':
    assert(zeros(12) == 2)
    assert(zeros(13) == 2)
    assert(zeros(25) == 6)
