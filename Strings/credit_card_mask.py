"""
Credit Card Mask

Usually when you buy something, you're asked whether your credit card number,
phone number or answer to your most secret question is still correct. However,
since someone could look over your shoulder, you don't want that shown on your
screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.
"""
import sys

sys.path.append('..')
from helpers.test_wrapper import Test


def maskify(cc):
    return len(cc[:-4]) * '#' + cc[-4:]


def run_tests():
    with Test() as test:
        cc = ''
        r = maskify(cc)
        test.describe("masking: {0}".format(cc))
        test.it("{0}  matches  {1}".format(cc,r))
        test.assert_equals(cc, r)

        cc = '123'
        r = maskify(cc)
        test.describe("masking: {0}".format(cc))
        test.it("{0}  matches  {1}".format(cc, r))
        test.assert_equals(cc, r)

        cc = 'SF$SDfgsd2eA'
        r = maskify(cc)
        test.describe("masking: {0}".format(cc))
        test.it("{0}  matches  {1}".format('########d2eA', r))
        test.assert_equals('########d2eA', r)


if __name__ == '__main__':
    run_tests()
