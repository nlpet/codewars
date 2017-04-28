"""
Let's Play Darts

Create your own mechanical dartboard that gives back your score
based on the coordinates of your dart.

Task:

Use the scoring rules for a standard dartboard:

Finish method:
def get_score(x,y):

* The coordinates are (x, y) are always relative to the center of
  the board (0, 0). The unit is millimeters. If you throw your dart
  5 centimeters to the left and 3 centimeters below, it is written as:

* Possible scores are:
    Outside of the board: "X"
    Bull's eye: "DB"
    Bull: "SB"
    A single number, example: "10"
    A triple number: "T10"
    A double number: "D10"

* A throw that ends exactly on the border of two sections results
  in a bounce out. You can ignore this because all the given
  coordinates of the tests are within the sections.

* The diameters of the circles on the dartboard are:
    Bull's eye: 12.70 mm
    Bull: 31.8 mm
    Triple ring inner circle: 198 mm
    Triple ring outer circle: 214 mm
    Double ring inner circle: 324 mm
    Double ring outer circle: 340 mm
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def get_score(x, y):
    return None  # finish this


def run_tests():
    with Test() as test:
        test.it("With given coordinates")
        test.assert_equals(get_score(-133.69, -147.38), "X",
                           "The score can be 'No Score'")
        test.assert_equals(get_score(4.06, 0.71), "DB",
                           "The score can be 'Bull's Eye'")
        test.assert_equals(get_score(2.38, -6.06), "SB",
                           "The score can be 'Bull'")
        test.assert_equals(get_score(-5.43, 117.95),
                           "20", "The score can be 20")
        test.assert_equals(get_score(-73.905, -95.94),
                           "7", "The score can be 7")
        test.assert_equals(get_score(55.53, -87.95), "T2",
                           "The score can be a tripple")
        test.assert_equals(get_score(-145.19, 86.53), "D9",
                           "The score can be a double")


if __name__ == '__main__':
    run_tests()
