"""
Parse HTML/CSS Colors

Output
In this kata you parse RGB colors represented by strings. The formats are
primarily used in HTML and CSS. Your task is to implement a function which
takes a color as a string and returns the parsed color as a map (see Examples).

Input

The input string represents one of the following:

1. 6-digit hexadecimal

"#RRGGBB" - Each pair of digits represents a value of the channel in hexadecimal: 00 to FF

2. 3-digit hexadecimal

"#RGB" - Each digit represents a value 0 to F which translates to 2-digit
hexadecimal: 0->00, 1->11, 2->22, and so on.

3. Preset color name

You have to use the predefined map PRESET_COLORS (Ruby, Python, JavaScript)
or preset-colors (Clojure). The keys are the names of preset colors in lower-case
and the values are the corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test

PRESET_COLORS = {
    'limegreen': '#32CD32'
}


def parse_html_color(s):
    rgb = []
    if not s.startswith('#'):
        s = PRESET_COLORS[s.lower()]

    s = s[1:]
    if len(s) == 3:
        for ch in s:
            rgb.append(int(ch + ch, 16))
    elif len(s) == 6:
        for i in range(0, 6, 2):
            rgb.append(int(s[i:i + 2], 16))

    return dict(zip('rgb', rgb))


def run_tests():
    with Test() as test:
        test.describe('Example tests')
        test.assert_equals(parse_html_color('#80FFA0'),   {'r': 128, 'g': 255, 'b': 160})
        test.assert_equals(parse_html_color('#3B7'),      {'r': 51,  'g': 187, 'b': 119})
        test.assert_equals(parse_html_color('LimeGreen'), {'r': 50,  'g': 205, 'b': 50 })


if __name__ == '__main__':
    run_tests()
