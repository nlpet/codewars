"""
Sum Strings as Numbers

Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def sum_strings(a, b):
    lsta, lstb = list(a)[::-1], list(b)[::-1]
    lena, lenb = len(a) - 1, len(b) - 1
    result = []
    rem = 0

    for n, m in zip(lsta, lstb):
        sm = int(n) + int(m)
        if sm + rem > 9:
            rem, d = divmod(sm + rem, 10)
            result.append(d)
        else:
            result.append(sm + rem)
            rem = 0

    if lena > lenb:
        lst = lsta[lenb + 1:]
    else:
        lst = lstb[lena + 1:]

    for n in list(map(int, lst)):
        if n + rem > 9:
            rem, d = divmod(n + rem, 10)
            result.append(d)
        else:
            result.append(n + rem)
            rem = 0

    if rem > 0:
        result.append(rem)

    return ''.join([str(x) for x in reversed(result)])


def run_tests():
    with Test() as test:
        test.assert_equals(sum_strings('123', '456'), '579')
        test.assert_equals(sum_strings('376', '39544'), '39920')
        test.assert_equals(
            sum_strings('712569312664357328695151392',
                        '8100824045303269669937'),
            '712577413488402631964821329')

        test.assert_equals(
            sum_strings('50095301248058391139327916261',
                        '81055900096023504197206408605'),
            '131151201344081895336534324866')


if __name__ == '__main__':
    run_tests()
