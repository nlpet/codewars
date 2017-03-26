"""
Roman Numerals helper

Create a RomanNumerals helper that can convert a roman numeral to
and from an integer value. The class should follow the API
demonstrated in the examples below. Multiple roman numeral
values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit
separately starting with the left most digit and skipping
any digit with a value of zero. In Roman numerals 1990 is
rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008
is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each
Roman symbol in descending order: MDCLXVI.

Examples:

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
"""
from collections import OrderedDict
import sys

sys.path.append('..')
from helpers.test_wrapper import Test


TO_ROMAN_NUMERALS = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
    (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

FROM_ROMAN_NUMERALS = {v: k for k, v in TO_ROMAN_NUMERALS}
ROMAN_NUMERALS = OrderedDict(TO_ROMAN_NUMERALS)


def to_roman(goal):
    result = []

    for num in ROMAN_NUMERALS.keys():
        if num > goal:
            continue
        div, goal = divmod(goal, num)
        result.append(ROMAN_NUMERALS[num] * div)
        if goal == 0:
            break

    return ''.join(result)


def from_roman(roman):
    result, l = 0, len(roman)

    for i in range(l):
        num = FROM_ROMAN_NUMERALS[roman[i]]
        if i + 1 < l and FROM_ROMAN_NUMERALS[roman[i + 1]] > num:
            result -= num
        else:
            result += num

    return result


def run_tests():
    with Test() as test:
        test.it('Should convert integers to roman numerals')
        test.assert_equals(to_roman(1000), 'M')
        test.assert_equals(to_roman(567), 'DLXVII')
        test.assert_equals(to_roman(1035), 'MXXXV')
        test.assert_equals(to_roman(653), 'DCLIII')
        test.assert_equals(to_roman(333), 'CCCXXXIII')
        test.assert_equals(to_roman(919), 'CMXIX')

        test.it('Should convert roman numerals to integers')
        test.assert_equals(from_roman('M'), 1000)
        test.assert_equals(from_roman('DLXVII'), 567)
        test.assert_equals(from_roman('MXXXV'), 1035)
        test.assert_equals(from_roman('DCLIII'), 653)
        test.assert_equals(from_roman('CCCXXXIII'), 333)
        test.assert_equals(from_roman('CMXIX'), 919)


if __name__ == '__main__':
    run_tests()
