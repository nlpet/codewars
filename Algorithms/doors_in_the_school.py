u"""
Doors in the school challenge.

In the morning all the doors in the school are closed. The school is quite big:
there are N doors. Then pupils start coming. It might be hard to believe, but all
of them want to study! Also, there are exactly N children studying in this school,
and they come one by one.

When these strange children pass by some doors they change their status
(i.e. Open -> Closed, Closed -> Open). Each student has their number,
and each i-th student alters the status of every i-th door. For example:
when the first child comes to the schools, he changes every first door
(he opens all of them). The second one changes the status of every second door
(he closes some doors: the 2nd, the 4th and so on).
Finally, when the last one – the n-th – comes to the school, he changes the
status of each n-th door (there's only one such door, though).

You need to count how many doors are left opened after all the students have come.
"""
import sys

sys.path.append('..')
from helpers.test_wrapper import Test


def doors(n):
    doors = [False] * n
    for i in range(0, n):
        for j in range(i, n, i + 1):
            doors[j] = not doors[j]
    return doors.count(True)


def doors2(n):
    return int(n ** .5)


def doors3(n):
    doors = [0] * n
    for i in range(1, n + 1):
        doors[i - 1::i] = [x ^ 1 for x in doors[i - 1::i]]
    return sum(doors)


def run_tests():
    with Test() as test:
        test.describe("Basic tests")
        test.assert_equals(doors(5), 2)
        test.assert_equals(doors(10), 3)
        test.assert_equals(doors(100), 10)


if __name__ == '__main__':
    run_tests()
