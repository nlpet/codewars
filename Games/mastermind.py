u"""
Mastermind

Rules

1. The Mastermind (computer) will select 4 colours. The colours are randomly
   selected from ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"].
   Colours can be duplicated but there will always be exactly 4.
2. The Mastermind will return an array back to you. For every correctly
   positioned colour in the array an element of “Black” is returned.
   For every correct colour but in the wrong position an element of “White”
   will be returned.
3. Passing the correct array will pass the Kata test.
4. Passing an invalid colour will fail the test with the error
   "Error: you have given an invalid colour!"
5. Passing an invalid array length will fail the test with the error "Error: you
   must pass 4 colours!"
6. Guessing more than 60 times will fail the test with the error "Error: you have
   had more than 60 tries!"
7. All colours are capitalised
8. The return array will be shuffled!


Task

Your task is to create a method called mastermind() that will take an object
called game. The object has already been preloaded so you do not need to worry
about it. Within your method you must pass an array into the game object
method .check(). This will evoke the object to check your array to see if it is correct.

Example

If the Mastermind selected the following colours

Then the array you are trying to solve is ["Red", "Blue", "Green", "Yellow"]

So you guess with

["Red", "Orange", "Yellow", "Orange"]

Your method would look like this.

def mastermind(game):
  answer = game.check(["Red", "Orange", "Yellow", "Orange"])

The element 0 => Red is at the correct index so Black is added to the return array.
Element 2 => Yellow is in the array but at the wrong index possition so White is
added to the return array.

The Mastermind would then return ["Black", "White"] (But not necessarily in that
order as the return array is shuffled my the Mastermind).

Keep guessing until you pass the correct solution which will pass the Kata.

Check result

To check the Masterminds return value

  answer = game.check(["Red", "Orange", "Yellow", "Orange"])
  print (answer)
Good luck and enjoy!
"""
from helpers.test_wrapper import Test
from itertools import permutations
from random import choice, shuffle
import sys
sys.path.append('..')


class MasterMind(object):
    """Mastermind game"""

    def __init__(self):
        self.size = 4
        self.tries = 0
        self.colors = ['Red', 'Blue', 'Green', 'Orange', 'Purple', 'Yellow']
        self.solution = [choice(self.colors) for _ in range(self.size)]

    def new(self):
        self.tries = 0
        self.solution = [choice(self.colors) for _ in range(self.size)]

    def check(self, array):
        attempt = set(array)
        if len(array) != self.size:
            raise Exception('Error: you must pass 4 colours')
        elif attempt.intersection(self.colors) != attempt:
            raise Exception('Error: you have given an invalid colour!')
        elif self.tries > 60:
            raise Exception('Error: you have had more than 60 tries!')
        else:
            result = []
            guess = list(array)
            solution = self.solution[:]
            start = 0
            while start < len(guess):
                if guess[start] == solution[start]:
                    result.append('Black')
                    del guess[start]
                    del solution[start]
                else:
                    start += 1

            while guess and solution:
                color = guess.pop()
                if color in solution:
                    result.append('White')
                    solution.remove(color)

            self.tries += 1
            shuffle(result)
            return result


class HackedMastermind(MasterMind):
    """Test version of Mastermind"""

    def __init__(self, solution):
        self.size = 4
        self.tries = 0
        self.colors = ['Red', 'Blue', 'Green', 'Orange', 'Purple', 'Yellow']
        self.solution = solution


def mastermind(game):
    colors = ['Red', 'Blue', 'Green', 'Orange', 'Purple', 'Yellow']
    answer = []
    for i in range(len(colors)):
        if len(answer) == 4:
            break
        result = game.check([colors[i]] * 4)
        answer.extend([colors[i]] * len(result))

    for perm in map(list, permutations(answer)):
        result = game.check(perm)
        if set(result) == {'Black'}:
            return perm


def run_tests():
    colors = ['Red', 'Blue', 'Green', 'Orange', 'Purple', 'Yellow']

    with Test() as test:
        test.describe('Mastermind randomly generated tests')
        for _ in range(10):
            solution = [choice(colors) for _ in range(4)]
            game = HackedMastermind(solution)
            test.assert_equals(mastermind(game), solution)


if __name__ == '__main__':
    run_tests()
