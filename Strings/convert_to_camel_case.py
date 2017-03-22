u"""
Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words
into camel casing. The first word within the output should be capitalized only
if the original word was capitalized.

Examples:

# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior")

# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")
"""
import re
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def to_camel_case(s):
    if not s:
        return ''

    res = []
    words = re.findall(r'([a-zA-Z]+)', s)
    word = words.pop(0)

    if word[0] == word[0].title():
        res.append(word[0] + word[1:].lower())
    else:
        res.append(word.lower())

    for word in words:
        res.append(word[0].upper() + word[1:].lower())

    return ''.join(res)


def run_tests():
    with Test() as test:
        test.describe("Testing function to_camel_case")
        test.it("Basic tests")
        msg = "An empty string was provided but not returned"
        test.assert_equals(to_camel_case(''), '', msg)
        msg = "to_camel_case('the_stealth_warrior') did not return correct value"
        test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", msg)
        msg = "to_camel_case('The-Stealth-Warrior') did not return correct value"
        test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", msg)
        msg = "to_camel_case('A-B-C') did not return correct value"
        test.assert_equals(to_camel_case("A-B-C"), "ABC", msg)


if __name__ == '__main__':
    run_tests()
