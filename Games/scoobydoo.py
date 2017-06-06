"""
Scooby Doo Puzzle


Introduction

Good one Shaggy! We all love to watch Scooby Doo, Shaggy Rogers, Fred Jones,
Daphne Blake and Velma Dinkley solve the clues and figure out who was the
villain. The story plot rarely differed from one episode to the next. Scooby
and his team followed the clue then unmasked the villain at the end.


Task

Your task is to initially solve the clues and then use those clues to
unmask the villain. You will be given a string of letters that you must
manipulate in a way that the clues guide you. You must then output the villain.

You will be given an Array of potential villains and you must only return
the correct masked villain.

Potential Villains for the example test cases
Black Knights, Puppet Master, Ghost Clowner, Witch Doctors, Waxed Phantom,
Manor Phantom, Ghost Bigfoot, Haunted Horse, Davy Crockett, Captain Injun,
Greens Gloobs, Ghostly Manor, Netty Crabbes, King Katazuma, Gators Ghouls,
Headless Jack, Mambas Wambas, Medicines Man, Demon Sharker, Kelpy Monster,
Gramps Vamper, Phantom Racer, Skeletons Men, Moon Monsters

There will be different villains for the main test cases!

Clue 1: The first clue is in a 'house' on 'String Class' Avenue.

Good luck!

Solution:

print(String().house())

Step 1: Rotate all letters to the right by 5
Clue: You are close to the monster so you may need to create a 'Disguise'
None

print(Disguise())

Step 2: Reverse the whole string
Clue: What is the length of Scooby Doo's favourite snack?
Try using the answer in the Integer Class

print(Integer().eleven())

Step 3: Add 5 letters onto every even letter in the Villans Name ie a=>f
Make sure after the letter z it goes round to a
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test
from string import ascii_lowercase


LETTERS_TO_NUMBERS = dict(zip(ascii_lowercase, range(0, 26)))
NUMBERS_TO_LETTERS = dict(zip(range(0, 26), ascii_lowercase))


def process_villains(villians):
    return dict(zip(
        map(lambda s: s.lower().replace(' ', ''), villians),
        villians))


def rotate_right(s, n):
    return s[-n:] + s[:-n]


def add_n_to_even_letters(s, n):
    new = [ch for ch in s]
    for i in range(1, len(s), 2):
        num = (LETTERS_TO_NUMBERS[s[i]] + 5) % 26
        new[i] = NUMBERS_TO_LETTERS[num]
    return ''.join(new)


def scoobydoo(s, villians):
    villians_dict = process_villains(villians)
    s = add_n_to_even_letters(rotate_right(s, 5)[::-1], 5)
    return villians_dict[s]


def run_tests():
    with Test() as test:
        villians = [
            "Black Knights", "Puppet Master", "Ghost Clowner", "Witch Doctors",
            "Waxed Phantom", "Manor Phantom", "Ghost Bigfoot", "Haunted Horse",
            "Davy Crockett", "Captain Injun", "Greens Gloobs", "Ghostly Manor",
            "Netty Crabbes", "King Katazuma", "Gators Ghouls", "Headless Jack",
            "Mambas Wambas", "Medicines Man", "Demon Sharker", "Kelpy Monster",
            "Gramps Vamper", "Phantom Racer", "Skeletons Men", "Moon Monsters"
        ]

        test.it("should return Medicines Man")
        test.assert_equals(scoobydoo("ndcddzmiahsz", villians), "Medicines Man")

        test.it("should return Skeletons Men")
        test.assert_equals(scoobydoo("ooegefsiehsi", villians), "Skeletons Men")

        test.it("should return Witch Doctors")
        test.assert_equals(scoobydoo("oyhxtdwnrjtx", villians), "Witch Doctors")


if __name__ == '__main__':
    run_tests()
