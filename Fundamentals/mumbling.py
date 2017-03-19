u"""
Mumbling

This time no story, no theory. The examples below show you how
to write function accum:

Examples:

accum('abcd')    # 'A-Bb-Ccc-Dddd'
accum('RqaEzty') # 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'
accum('cwAt')    # 'C-Ww-Aaa-Tttt'

The parameter of accum is a string which includes only letters from a..z and A..Z.
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def accum(s):
    return '-'.join([(s[i] * (i + 1)).title() for i in range(len(s))])


def run_tests():

    with Test() as test:
        test.describe('accum')
        test.it('Basic tests')

        s = 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu'
        test.assert_equals(accum('ZpglnRxqenU'), s)
        s = 'N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb'
        test.assert_equals(accum('NyffsGeyylB'), s)
        s = 'M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu'
        test.assert_equals(accum('MjtkuBovqrU'), s)
        s = 'E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm'
        test.assert_equals(accum('EvidjUnokmM'), s)
        s = 'H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc'
        test.assert_equals(accum('HbideVbxncC'), s)


if __name__ == '__main__':
    run_tests()
