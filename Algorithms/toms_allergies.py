"""
Allergies

Write a program that, given a person's allergy score, can tell them whether or
not they're allergic to a given item, and their full list of allergies.

An allergy test produces a single numeric score which contains the information
about all the allergies the person has (that they were tested for).

The list of items (and their value) that were tested are:

eggs (1)
peanuts (2)
shellfish (4)
strawberries (8)
tomatoes (16)
chocolate (32)
pollen (64)
cats (128)
So if Tom is allergic to peanuts and chocolate, he gets a score of 34.

Now, given just that score of 34, your program should be able to say:

Whether Tom is allergic to any one of those allergens listed above.
All the allergens Tom is allergic to., sorted alphabetically
Example:

>>> allergies = Allergies(0)
>>> allergies.is_allergic_to('peanuts')
True
>>> sorted(Allergies(255).lst))
['cats', 'chocolate', 'eggs', 'peanuts', 'pollen', 'shellfish',
'strawberries', 'tomatoes']
>>> Allergies(259).allergies()
["eggs", "peanuts"]
You will be provided with a class Allergies which will have 2 methods

* is_allergic_to Checks if Tom is allergic to a particular allergen.
  Returns True if Tom is allergic, False otherwise
* allergies Returns a list of what Tom is allergic to. This list must
  be sorted alphabetically

Must Dos:

Ensure that your function throws a TypeError for invalid inputs such as None,
floats, strings, or any data type that is not an integer.

Hint: Use Bitwise ANDing
"""
from operator import and_
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


class Allergies(object):
    """Allergies class"""

    ALLERGY_SCORES = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        if not isinstance(score, int):
            raise TypeError('Score must be an integer')
        self.score = score

    def is_allergic_to(self, allergen):
        return bool(and_(Allergies.ALLERGY_SCORES.get(allergen, 0), self.score))

    def allergies(self):
        allergies_ = []
        for name, score in Allergies.ALLERGY_SCORES.items():
            if and_(self.score, score):
                allergies_.append(name)
        return sorted(allergies_)


def run_tests():
    with Test() as test:
        test.describe("no_allergies_means_not_allergic")
        allergies = Allergies(0)
        test.assert_equals(allergies.is_allergic_to('peanuts'), False)
        test.assert_equals(allergies.is_allergic_to('cats'), False)
        test.assert_equals(allergies.is_allergic_to('strawberries'), False)

        test.describe("is_allergic_to_eggs")
        test.assert_equals(Allergies(1).is_allergic_to('eggs'), True)



if __name__ == '__main__':
    run_tests()
