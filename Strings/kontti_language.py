"""
Kontti Language

Kontti language is a finnish word play game, you add -kontti to the end of
a word and then switch their first letters until the first vowel (as in "aeiouy");
if no vowel is present, the word stays the same.

For example the word lamppu becomes komppu-lantti; aeiou becomes koeiou-antti and so on.

Write a string method that turns a sentence into a kontti sentence!
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def kontti(s):
    if not s:
        return ''

    res = []
    vowels = set(('aeiouyAEIOUY'))
    suffix = list('kontti')
    ls = len(suffix)

    for word in [list(w) for w in s.split(' ')]:
        vf, vs = -1, -1
        lw = len(word)
        for i in range(max(lw, 6)):
            if i < lw and word[i] in vowels and vf == -1:
                vf = i
            if i < ls and suffix[i] in vowels and vs == -1:
                vs = i
            if vf >= 0 and vs >= 0:
                break

        if vf == -1 or vs == -1:
            res.append(''.join(word))
        else:
            res.append(
                '{}-{}'.format(
                    ''.join(suffix[:vs + 1] + word[vf + 1:]),
                    ''.join(word[:vf + 1] + suffix[vs + 1:])
                )
            )

    return ' '.join(res)


def run_tests():
    with Test() as test:
        test.describe("Basic tests")
        test.assert_equals(kontti("lamppu"), "komppu-lantti")
        test.assert_equals(kontti("lamppu sofia"), "komppu-lantti kofia-sontti")
        test.assert_equals(kontti("silly game"), "kolly-sintti kome-gantti")
        test.assert_equals(kontti("aeiou"), "koeiou-antti")
        test.assert_equals(kontti("xyz lamppu"), "koz-xyntti komppu-lantti")
        test.assert_equals(kontti(""), "")
        test.assert_equals(kontti("lAmppU"), "komppU-lAntti")
        test.assert_equals(kontti("silly grrr"), "kolly-sintti grrr")


if __name__ == '__main__':
    run_tests()
