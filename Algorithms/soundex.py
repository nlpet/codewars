"""
A History Lesson

Soundex is an interesting phonetic algorithm developed nearly 100 years ago
for indexing names as they are pronounced in English. The goal is for
homophones to be encoded to the same representation so that they can be
matched despite minor differences in spelling.

Reference: https://en.wikipedia.org/wiki/Soundex

Preface

I first read about Soundex over 30 years ago. At the time it seemed to me
almost like A.I. that you could just type in somebody's name the way it
sounded and there was still a pretty good chance it could match the correct
person record. That was about the same year as the first "Terminator" movie
so it was easy for me to put 2 and 2 together and conclude that Arnie must
have had some kind of futuristic Soundex chip in his titanium skull helping
him to locate Serah Coner... or was it Sarh Connor... or maybe Sayra Cunnarr...

:-)

Task

In this Kata you will encode strings using a Soundex variation called
"American Soundex" using the following steps:

* Save the first letter. Remove all occurrences of h and w except first letter.
* Replace all consonants (include the first letter) with digits as follows:
    - b, f, p, v = 1
    - c, g, j, k, q, s, x, z = 2
    - d, t = 3
    - l = 4
    - m, n = 5
    - r = 6
* Replace all adjacent same digits with one digit.
* Remove all occurrences of a, e, i, o, u, y except first letter.
* If first symbol is a digit replace it with letter saved on step 1.
* Append 3 zeros if result contains less than 3 digits. Remove all except
  first letter and 3 digits after it

Input

A space separated string of one or more names. E.g.

Sarah Connor

Output

Space separated string of equivalent Soundex codes (the first character of
each code must be uppercase). E.g.

S600 C560
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test

MAPPER = {
    'b': 1, 'f': 1, 'p': 1, 'v': 1,
    'c': 2, 'g': 2, 'j': 2, 'k': 2,
    'q': 2, 's': 2, 'x': 2, 'z': 2,
    'd': 3, 't': 3, 'l': 4, 'm': 5,
    'n': 5, 'r': 6
}


def soundex(s):
    ls = s.split(' ')
    result = []

    for s in ls:
        first, new = s[0], []
        s = s[0] + s[1:].lower().replace('h', '').replace('w', '')
        for ch in s:
            num = MAPPER.get(ch)
            if num and ((new and new[-1] != num) or not new):
                new.append(num)
        if new[0] in range(0, 9):
            new[0] = first
        if len(new) < 4:
            new.extend([0] * (4 - len(new)))
        result.append(''.join([str(x) for x in new]))
    return ' '.join(result)


def run_tests():
    with Test() as test:
        test.describe("Arnie")
        # test.assert_equals(soundex("Sarah Connor"),  "S600 C560")
        # test.assert_equals(soundex("Sara Conar"),    "S600 C560")
        # test.assert_equals(soundex("Serah Coner"),   "S600 C560")
        # test.assert_equals(soundex("Sarh Connor"),   "S600 C560")
        # test.assert_equals(soundex("Sayra Cunnarr"), "S600 C560")
        test.assert_equals(soundex("Bob"), "B100")


if __name__ == '__main__':
    run_tests()
