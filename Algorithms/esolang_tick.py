u"""
Esolang: Tick

Task

Make a custom esolang interpreter for the language Tick. Tick is a descendant of
Ticker but also very different data and command-wise.

Syntax/Info

Commands are given in character format. Non-command characters should be ignored.
Tick has an potentially infinite memory as opposed to Ticker(which you have a
special command to add a new cell) and only has 4 commands(as opposed to 7).
Read about this esolang here.

Commands

>: Move data selector right

<: Move data selector left

+: Increment memory cell by 1. 255+1=0

*: Add ascii value of memory cell to the output tape.
"""
from collections import defaultdict
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def interpreter(tape):
    memory, ptr, res = defaultdict(int), 0, []
    for cmd in tape:
        if cmd == '+':
            memory[ptr] += 1
        elif cmd == '*':
            res.append(chr(memory[ptr] % 256))
        elif cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
    return ''.join(res)


def run_tests():
    with Test() as test:
        s = (
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++*>++++++++++++++++++++++++++++++++++++++++++++++'
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++*>+++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '+++++++++++++++++++++++++++++++++++++++++++++**>++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '+++++++++++++++++++++++++++++++++++++++*>+++++++++++++++++++'
            '+++++++++++++*>+++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++*<<*>>>+++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '+++++++++++++++*<<<<*>>>>>++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++*>+++++++++++++++++++++++++++++++++*'
        )
        test.assert_equals(interpreter(s), 'Hello world!')


if __name__ == '__main__':
    run_tests()
