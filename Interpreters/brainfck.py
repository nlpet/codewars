"""
Brainf**k

Inspired from real-world Brainf**k, we want to create an interpreter of that
language which will support the following instructions (the machine memory or
'data' should behave like a potentially infinite array of bytes, initialized to 0):

> increment the data pointer (to point to the next cell to the right).
< decrement the data pointer (to point to the next cell to the left).
+ increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at
  the data pointer.
- decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the
  byte at the data pointer.
. output the byte at the data pointer.
, accept one byte of inp, storing its value in the byte at the data pointer.
[ if the byte at the data pointer is zero, then instead of moving the instruction
  pointer forward to the next command, jump it forward to the command after the
  matching ] command.
] if the byte at the data pointer is nonzero, then instead of moving the instruction
  pointer forward to the next command, jump it back to the command after the matching
  [ command.

The function will take in inp...

the program code, a string with the sequence of machine instructions,
the program inp, a string, eventually empty, that will be interpreted as an
array of bytes using each character's ASCII code and will be consumed by
the , instruction

... and will return ...

the output of the interpreted code (always as a string),
produced by the . instruction.
"""
from collections import defaultdict
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def get_loops(code):
    sf, sb, stack = {}, {}, []
    for i, ch in enumerate(code):
        if ch == '[':
            stack.append(i)
        elif ch == ']':
            el = stack.pop()
            sf[el] = i
            sb[i] = el
    return (sf, sb)


def brain_luck(code, inp):
    memory, ptr, res, pos, l = defaultdict(int), 0, [], 0, len(code)
    sf, sb = get_loops(code)

    while pos < l:
        if code[pos] == '>':
            ptr += 1
        elif code[pos] == '<':
            ptr -= 1
        elif code[pos] == '+':
            memory[ptr] = (memory[ptr] + 1) % 256
        elif code[pos] == '-':
            memory[ptr] = (memory[ptr] - 1) % 256
        elif code[pos] == '.':
            res.append(chr(memory[ptr]))
        elif code[pos] == ',':
            memory[ptr] = ord(inp[0])
            inp = inp[1:]
        elif code[pos] == '[':
            if memory[ptr] == 0:
                pos = sf[pos]
                continue
        elif code[pos] == ']':
            if memory[ptr] > 0:
                pos = sb[pos]
                continue
        pos += 1

    return ''.join(res)


def run_tests():
    with Test() as test:
        # Echo until byte(255) encountered
        test.assert_equals(
            brain_luck(',+[-.,+]', 'Codewars' + chr(255)), 'Codewars')

        # Echo until byte(0) encountered
        test.assert_equals(
            brain_luck(',[.[-],]', 'Codewars' + chr(0)), 'Codewars')

        # Two numbers multiplier
        test.assert_equals(
            brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)), chr(72))


if __name__ == '__main__':
    run_tests()
