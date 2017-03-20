u"""
Esolang Interpreters #1 - Introduction to Esolangs and My First Interpreter

The Language

MiniStringFuck is a derivative of the famous Brainfuck which contains a memory
cell as its only form of data storage as opposed to a memory tape of 30,000 cells
in Brainfuck. The memory cell in MiniStringFuck initially starts at 0.
MiniStringFuck contains only 2 commands as opposed to 8:

+ - Increment the memory cell. If it reaches 256, wrap to 0.
. - Output the ASCII value of the memory cell
"""
from collections import defaultdict
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def my_first_interpreter(tape):
    memory, ptr, res = defaultdict(int), 0, []
    for cmd in tape:
        if cmd == '+':
            memory[ptr] += 1
        elif cmd == '.':
            res.append(chr(memory[ptr] % 256))
    return ''.join(res)


def run_tests():
    with Test() as test:
        s = (
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '+++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '+++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++'
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++'
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.'
        )
        test.assert_equals(my_first_interpreter(s), 'Hello, World!')

        s = (
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.'
        )
        test.assert_equals(my_first_interpreter(s), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')


if __name__ == '__main__':
    run_tests()
