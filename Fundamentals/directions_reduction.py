u"""
Directions Reduction

Once upon a time, on a way through the old wild west,……
a man was given directions to go from one point to another.
The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH"
and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction
and coming back the opposite direction is a needless effort. Since this
is the wild west, with dreadfull weather and not much water, it's
important to save yourself some energy, otherwise you might die of thirst!

How I crossed the desert the smart way.

The directions given to the man are, for example, the following:

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].

or

{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or (haskell)

[North, South, South, East, West, North, West]
You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable,
better stay to the same place! So the task is to give to the man a simplified
version of the plan. A better plan in this case is simply:

Other examples:

In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going
north and coming back right away. What a waste of time! Better to do nothing.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other,
therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are
not directly opposite but they become directly opposite after the reduction of
"EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task

Write a function dirReduc which will take an array of strings and returns an
array of strings with the needless directions removed (W<->E or S<->N side by side).
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test

OPPOSITES = {
    'EAST': 'WEST',
    'WEST': 'EAST',
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH'
}


def dirReduc(lst):
    if not lst:
        return []
    lst = [d.upper() for d in lst]
    stack = [lst.pop()]
    while len(lst):
        direction = lst.pop()
        if stack and stack[-1] == OPPOSITES[direction]:
            stack.pop()
        else:
            stack.append(direction)

    return stack[::-1]


def run_tests():
    with Test() as test:
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        test.assert_equals(dirReduc(a), ['WEST'])
        u = ["NORTH", "WEST", "SOUTH", "EAST"]
        test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
        q = ["WEST", "NORTH", "SOUTH", "EAST", "WEST", "EAST"]
        test.assert_equals(dirReduc(q), [])
        d = ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
        test.assert_equals(dirReduc(d), ["WEST", "WEST"])


if __name__ == '__main__':
    run_tests()
