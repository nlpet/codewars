u"""
Decode morse code.

In this kata you have to write a simple Morse code decoder. While the Morse code
is now mostly superceded by voice and digital data communication channels, it
still has its use in some applications around the world.
The Morse code encodes every character as a sequence of 'dots' and 'dashes'.
For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit
1 is coded as ·−−−. The Morse code is case-insensitive, traditionally capital
letters are used. When the message is written in Morse code, a single space is
used to separate the character codes and 3 spaces are used to separate words.
For example, the message HEY JUDE in Morse code is ···· · −·−− ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special
service codes, the most notorious of those is the international distress signal
SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes
are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function decodeMorse(morseCode), that would take the
morse code as input and return a decoded human-readable string.

For example:

decodeMorse('.... . -.--   .--- ..- -.. .')
should return 'HEY JUDE'
"""
import re
import sys

sys.path.append('..')
from helpers.test_wrapper import Test

TO_MORSE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ',': '--..--', ':': '---...', '?': '..--..',
    "'": '.----.', '-': '-....-', ' ': '-..-.',
    '@': '.--.-.', '=': '-...-',  '!': '-.-.--',
    '.': '.-.-.-', 'SOS': '...---...'
}

FROM_MORSE = {value: key for key, value in TO_MORSE.items()}


def to_morse(s):
    return ' '.join(TO_MORSE.get(i.upper()) for i in s)


def from_morse(m):
    result = []
    words = [w for w in re.split('(\s+)', m) if len(w) > 0]

    for word in words:
        if word in FROM_MORSE:
            result.append(FROM_MORSE[word].upper())
        if word.count(' ') > 1:
            result += ' '
    return ''.join(result).strip()


def run_tests():
    with Test() as test:
        test.describe('Example from description')
        test.assert_equals(from_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
        test.assert_equals(from_morse('...---...'), 'SOS')
        test.assert_equals(from_morse(
            '... --- ... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.  \
             ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .  \
             .-.. .- --.. -.--   -.. --- --. .-.-.-'),
            'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')
        test.assert_equals(to_morse('SOS'), '... --- ...')
        test.assert_equals(to_morse('HEY JUDE'), '.... . -.-- -..-. .--- ..- -.. .')


if __name__ == '__main__':
    run_tests()
