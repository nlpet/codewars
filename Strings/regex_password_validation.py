"""
Regex Password Validation

You need to write regex that will validate a password to make sure it
meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number

Valid passwords will only be alphanumeric characters.
"""
from re import search, compile, VERBOSE
import sys
sys.path.append('..')

from helpers.test_wrapper import Test

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?\d)      # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)


def run_tests():
    with Test() as test:
        test.describe("Basic tests")
        test.assert_equals(bool(search(regex, 'fjd3IR9')), True)
        test.assert_equals(bool(search(regex, 'ghdfj32')), False)
        test.assert_equals(bool(search(regex, 'DSJKHD23')), False)
        test.assert_equals(bool(search(regex, 'dsF43')), False)
        test.assert_equals(bool(search(regex, '4fdg5Fj3')), True)
        test.assert_equals(bool(search(regex, 'DHSJdhjsU')), False)
        test.assert_equals(bool(search(regex, 'fjd3IR9.;')), False)
        test.assert_equals(bool(search(regex, 'fjd3  IR9')), False)
        test.assert_equals(bool(search(regex, 'djI38D55')), True)
        test.assert_equals(bool(search(regex, 'a2.d412')), False)
        test.assert_equals(bool(search(regex, 'JHD5FJ53')), False)
        test.assert_equals(bool(search(regex, '!fdjn345')), False)
        test.assert_equals(bool(search(regex, 'jfkdfj3j')), False)
        test.assert_equals(bool(search(regex, '123')), False)
        test.assert_equals(bool(search(regex, 'abc')), False)
        test.assert_equals(bool(search(regex, '123abcABC')), True)
        test.assert_equals(bool(search(regex, 'ABC123abc')), True)
        test.assert_equals(bool(search(regex, 'Password123')), True)


if __name__ == '__main__':
    run_tests()
