"""
CamelCase Method

Write simple .camelcase method (camel_case function in PHP) for strings.
All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def camel_case(s):
    return ''.join([w.capitalize() for w in s.split(' ')])


def camel_case2(string):
    return string.title().replace(" ", "")


def run_tests():
    with Test() as test:
        test.describe("Basic tests")
        test.assert_equals(camel_case("test case"), "TestCase")
        test.assert_equals(camel_case("camel case method"), "CamelCaseMethod")
        test.assert_equals(camel_case("say hello "), "SayHello")
        test.assert_equals(camel_case(" camel case word"), "CamelCaseWord")
        test.assert_equals(camel_case(""), "")


if __name__ == '__main__':
    run_tests()
