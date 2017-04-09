"""
Rail Fence Cipher: Encoding and Decoding

Create two functions to encode and then decode a string using the Rail
Fence Cipher. This cipher is used to encode a string by placing each
character successively in a diagonal along a set of "rails". First
start off moving diagonally and down. When you reach the bottom,
reverse direction and move diagonally and up until you reach the
top rail. Continue until you reach the end of the string. Each
"rail" is then read left to right to derive the encoded string.
You can optionally include or dis-include punctuation.

For example, this string: "WE ARE DISCOVERED. FLEE AT ONCE" would
be mapped to a three rail system as follows (omitting punctuation and spaces):

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .

The encoded string would be:
WECRLTEERDSOEEFEAOCAIVDEN

5 rails, same string (25 chars)

W . . . . . . . C . . . . . . . L . . . . . . . E
. E . . . . . S . O . . . . . F . E . . . . . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
. . . R . D . . . . . E . E . . . . . A . O . . .
. . . . E . . . . . . . R . . . . . . . T . . . .

Write a function/method that takes 2 arguments, a string and the number
of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and
the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that a
passing an empty string will return an empty string.
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def encode(string, rails):
    pass


def decode(string, rails):
    result = []
    length = len(string)
    per_line = length // rails
    first_line = per_line - 1
    last_line = per_line - 2
    middle_lines = rails - 2
    middle_line_len = int((length - first_line - last_line) / (rails - 2))

    import ipdb; ipdb.set_trace()

    result.extend(string[:first_line])

    pos = first_line

    for line in range(middle_lines):
        result.extend(string[pos: pos + middle_line_len])
        pos += middle_line_len

    result.extend(string[-last_line:])

    return ''.join(result)


def run_tests():
    with Test() as test:
        test.assert_equals(encode("WEAREDISCOVEREDFLEEATONCE", 3),
                           "WECRLTEERDSOEEFEAOCAIVDEN")
        test.assert_equals(decode("WECRLTEERDSOEEFEAOCAIVDEN", 3),
                           "WEAREDISCOVEREDFLEEATONCE")
        test.assert_equals(encode("Hello, World!", 3), "Hoo!el,Wrdl l")


if __name__ == '__main__':
    run_tests()
