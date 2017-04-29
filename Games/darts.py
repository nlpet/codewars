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
from math import sqrt, degrees, atan2
import sys
sys.path.append('..')

from helpers.test_wrapper import Test

DISTANCES = [
    (lambda d: d <= 6.35, 'DB'),
    (lambda d: d <= 15.9, 'SB'),
    (lambda d: 15.9 < d < 99 or 107 < d < 162, ''),
    (lambda d: 99 <= d <= 107, 'T'),
    (lambda d: 162 <= d <= 170, 'D'),
    (lambda d:  170 < d, 'X')
]

ANGLES = [
    (lambda a:   9 < a <= 27,  13),
    (lambda a:  27 < a <= 45,  4),
    (lambda a:  45 < a <= 63,  18),
    (lambda a:  63 < a <= 81,  1),
    (lambda a:  81 < a <= 99,  20),
    (lambda a:  99 < a <= 117, 5),
    (lambda a: 117 < a <= 135, 12),
    (lambda a: 135 < a <= 153, 9),
    (lambda a: 153 < a <= 171, 14),
    (lambda a: 171 < a <= 189, 11),
    (lambda a: 189 < a <= 207, 8),
    (lambda a: 207 < a <= 225, 16),
    (lambda a: 225 < a <= 243, 7),
    (lambda a: 243 < a <= 261, 19),
    (lambda a: 261 < a <= 279, 3),
    (lambda a: 279 < a <= 297, 17),
    (lambda a: 297 < a <= 315, 2),
    (lambda a: 315 < a <= 333, 15),
    (lambda a: 333 < a <= 351, 10),
    (lambda a:   a < 9 or 351 < a <= 360, 6)
]


def get_distance_label(distance):
    for func, lbl in DISTANCES:
        if func(distance):
            return lbl


def get_angle_label(angle):
    for func, lbl in ANGLES:
        if func(angle):
            return lbl


def get_score(x, y):
    r = sqrt(x ** 2 + y ** 2)
    distance = get_distance_label(r)
    if distance in ['X', 'DB', 'SB']:
        return distance

    angle = degrees(atan2(y, x))

    if angle < 0:
        angle += 360

    return '{}{}'.format(distance, get_angle_label(angle))


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
        test.assert_equals(get_score(161, 0.71), "6",
                           "The score can be 6")
        test.assert_equals(get_score(-105, 19), "T14",
                           "The score can be T14")


if __name__ == '__main__':
    run_tests()
