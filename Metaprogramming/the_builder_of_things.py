"""
The Builder of Things

For this kata you will be using some meta-programming magic to create a
new Thing object. This object will allow you to define things in a
descriptive sentence like format.

This challenge attempts to build on itself in an increasingly complex manner.

Examples of what can be done with "Thing":

jane = Thing('Jane')
jane.name # => 'Jane'

# can define boolean methods on an instance
jane.is_a.person
jane.is_a.woman
jane.is_not_a.man

jane.is_a_person # => True
jane.is_a_man # => False

# can define properties on a per instance level
jane.is_the.parent_of.joe
jane.parent_of # => 'joe'

# can define number of child things
# when more than 1, a tuple subclass is created
jane.has(2).legs
len(jane.legs) # => 2
isinstance(jane.legs[0], Thing) # => True

# can define single items
jane.has(1).head
isinstance(jane.head, Thing) # => True

# can define number of things in a chainable and natural format
>> Note: Python, unlike Ruby and Javascript, doesn't have a pretty syntax
for blocks of expressions and a forEach method for iterables. So you should
implement this behaviour yourself.
jane.has(2).arms.each.having(1).hand.having(5).fingers
len(jane.arms[0].hand.fingers) # => 5

# can define properties on nested items
jane.has(1).head.having(2).eyes.each.being_the.color.blue.having(1).
pupil.being_the.color.black

# can define methods: thing.can.verb(method, past='')
method = lambda phrase: "%s says: %s" % (name, phrase)
# or
def method(phrase):
  return "%s says: %s" % (name, phrase)
jane.can.speak(method, "spoke")

jane.speak("hello") # => "Jane says: hello"

# if past tense was provided then method calls are tracked
jane.spoke # => ["Jane says: hello"]

Note: Most of the test cases have already been provided for you so
that you can see how the Thing object is supposed to work.
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


class Thingness(type):
    """Thingness metaclass"""

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Thing(metaclass=Thingness):
    """Thing class"""

    def __init__(self, name=None):
        self.name = name


def run_tests():
    with Test() as test:
        jane = Thing('Jane')
        test.describe('jane =  Thing("Jane")')
        test.describe('jane.name')
        test.it('should be "Jane"')
        test.assert_equals(jane.name, 'Jane')

        test.describe('#is_a')
        test.describe('is_a.woman (dynamic key)')
        jane.is_a.woman
        test.it('jane.is_a_woman should return true')
        test.assert_equals(jane.is_a_woman, True)

        # test.describe('#is_not_a')
        # test.describe('is_not_a.man (dynamic key)')
        # jane.is_not_a.man
        # test.it('jane.is_a_man should return false')
        # test.assert_equals(jane.is_a_man, False)
        #
        # test.describe('#has')
        #
        # test.describe('jane.has(2).arms')
        # jane = Thing('Jane')
        # jane.has(2).arms
        # test.it('should define an arms method that is tuple subclass')
        # test.assert_equals(isinstance(jane.arms, tuple), True)
        # test.it('should populate 2 new Thing instances within the tuple subclass')
        # test.assert_equals(len(jane.arms), 2)
        # test.assert_equals(all(isinstance(v, Thing) for v in jane.arms), True)
        # test.it('should call each thing by its singular form (aka "arm")')
        # test.assert_equals(all(v.name == "arm" for v in jane.arms), True)
        # test.it('should have is_arm == true for each arm instance')
        # test.assert_equals(all(v.is_arm for v in jane.arms), True)
        #
        # test.describe('jane.having(2).arms (alias)')
        # test.it('should populate 2 new Thing instances within the tuple subclass')
        # jane = Thing('Jane')
        # jane.having(2).arms
        # test.assert_equals(len(jane.arms), 2)
        # test.assert_equals(all(isinstance(v, Thing) for v in jane.arms), True)
        #
        # test.describe('jane.has(1).head')
        # jane = Thing('Jane')
        # jane.has(1).head
        # test.it('should define head method that is a reference to a new Thing')
        # test.assert_equals(isinstance(jane.head, Thing), True)
        # test.it('should name the head thing "head"')
        # test.assert_equals(jane.head.name, "head")
        #
        # test.describe('jane.has(1).head.having(2).eyes')
        # jane = Thing('Jane')
        # jane.has(1).head.having(2).eyes
        # test.it('should create 2 new things on the head')
        # test.assert_equals(len(jane.head.eyes), 2)
        # test.assert_equals(all(isinstance(v, Thing)
        #                        for v in jane.head.eyes), True)
        # test.it('should name the eye things "eye"')
        # test.assert_equals(all(v.name == 'eye' for v in jane.head.eyes), True)
        #
        # test.describe('#each')
        # test.describe('jane.has(2).arms.each.having(5).fingers')
        # jane = Thing('Jane')
        # jane.has(2).arms.each.having(5).fingers
        # test.it('should cause 2 arms to be created each with 5 fingers')
        # test.assert_equals(all(len(v.fingers) == 5 for v in jane.arms), True)
        #
        # test.describe('#is_the')
        #
        # test.describe('jane.is_the.parent_of.joe')
        # jane = Thing('Jane')
        # jane.is_the.parent_of.joe
        # test.it('should set jane.parent_of == "joe"')
        # test.assert_equals(jane.parent_of, "joe")
        #
        # test.describe('#being_the')
        #
        # test.describe(
        #     'jane.has(1).head.having(2).eyes.each.being_the.color.blue')
        # test.it("jane's eyes should both be blue")
        # jane = Thing('Jane')
        # jane.has(1).head.having(2).eyes.each.being_the.color.blue
        # test.assert_equals(
        #     all(v.color == 'blue' for v in jane.head.eyes), True)
        #
        # test.describe(
        #     'jane.has(2).eyes.each.being_the.color.blue.and_the.shape.round')
        # test.it('should allow chaining via the and_the method')
        # jane = Thing('Jane')
        # jane.has(2).eyes.each.being_the.color.blue.and_the.shape.round
        # test.assert_equals(all(v.color == 'blue' for v in jane.eyes), True)
        # test.assert_equals(all(v.shape == 'round' for v in jane.eyes), True)
        #
        # it = 'jane.has(2).eyes.each.being_the.color.green.having(2).pupils.each.being_the.color.black'
        # test.describe(it)
        # test.it('should allow nesting by using having')
        # jane = Thing('Jane')
        # jane.has(2).eyes.each.being_the.color.green.having(
        #     1).pupil.being_the.color.black
        # test.assert_equals(all(v.color == 'green' for v in jane.eyes), True)
        # test.assert_equals(
        #     all(v.pupil.color == 'black' for v in jane.eyes), True)
        #
        # test.describe('#can')
        #
        # test.describe(
        #     'jane.can.speak(lambda phrase: "#%s says: #%s" % (name, phrase))')
        # jane = Thing('Jane')
        #
        # def fnc(phrase):
        #     return "%s says: %s" % (name, phrase)
        #
        # jane.can.speak(fnc)
        # test.it('should create a speak method on the instance')
        # test.assert_equals(jane.speak('hi'), "Jane says: hi")
        #
        # test.describe(
        #     'jane.can.speak(lambda phrase: "#%s says: #%s" % (name, phrase), "spoke")')
        # jane = Thing('Jane')
        #
        # jane.can.speak(fnc, 'spoke')
        # jane.speak('hi')
        # test.it('should add a "spoke" attribute that tracks all speak call results')
        # test.assert_equals(jane.spoke, ["Jane says: hi"])
        # jane.speak('goodbye')
        # test.assert_equals(jane.spoke, ["Jane says: hi", "Jane says: goodbye"])


if __name__ == '__main__':
    run_tests()
