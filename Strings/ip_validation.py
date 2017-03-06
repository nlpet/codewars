"""
IP Validation

Write an algorithm that will identify valid IPv4 addresses in dot-decimal
format. Input to the function is guaranteed to be a single string.

Examples of valid inputs: 1.2.3.4 123.45.67.89

Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def is_valid_IP(ip):
    success = 0

    for section in ip.split('.'):
        if section.isdigit():
            if section[0] == '0' or section.find(' ') >= 0:
                return False

            if 0 < int(section) <= 255:
                success += 1
    return success == 4


def run_tests():
    with Test() as test:
        test.assert_equals(is_valid_IP('12.255.56.1'),     True)
        test.assert_equals(is_valid_IP(''),                False)
        test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
        test.assert_equals(is_valid_IP('123.456.789.0'),   False)
        test.assert_equals(is_valid_IP('12.34.56'),        False)
        test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
        test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
        test.assert_equals(is_valid_IP('123.045.067.089'), False)


if __name__ == '__main__':
    run_tests()
