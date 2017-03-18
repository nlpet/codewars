# Custom implementation of codewar's testing framework
# from collections import Iterable
from termcolor import colored
from time import time


class Test(object):
    """Test class for codewars."""

    def __init__(self):
        self.failures = 0
        self.successes = 0
        self.start = time()

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_value, tb):
        self.report()

    def describe(self, name):
        print(colored('\n--> {}'.format(name), 'blue'))

    def it(self, name):
        print('\n{}'.format(name))

    def _handle_success(self, msg):
        self.successes += 1
        print(colored('[✔] {}'.format(msg), 'green'))

    def _handle_failure(self, msg):
        self.failures += 1
        print(colored('[✘] {}'.format(msg), 'red'))

    def _format_msg(self, a, b, msg):
        if not msg:
            # a, b = map(lambda x: list(x) if isinstance(x, Iterable) else x, [a, b])
            msg = 'expect {} to equal {}'.format(a, b)
        return msg

    def _assert(self, func, a, b, msg):
        msg = self._format_msg(a, b, msg)
        if func(a, b):
            self._handle_success(msg)
        else:
            self._handle_failure(msg)

    def assert_equals(self, a, b, msg=None):
        eq = lambda a, b: a == b
        self._assert(eq, a, b, msg)

    def assert_not_equals(self, a, b, msg=None):
        neq = lambda a, b: a != b
        self._assert(neq, a, b, msg)

    def expect(self, expected, msg=None):
        if not msg:
            msg = 'OK' if expected else 'Not as expected'
        if expected:
            self._handle_success(msg)
        else:
            self._handle_failure(msg)

    def expect_error(self, msg, op, args=None):
        try:
            if args:
                op(*args)
            else:
                op()
            self._handle_failure(msg)
        except Exception:
            self._handle_success(msg)

    def report(self):
        print(colored('\nPassed: {}'.format(self.successes), 'green'))
        print(colored('Failed: {}'.format(self.failures), 'red'))
        print('\nTests took {:2f} seconds'.format(time() - self.start))
