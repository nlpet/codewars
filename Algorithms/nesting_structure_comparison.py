"""
Nesting Structure Comparison


Complete the method (or function in Python) to return true when its argument is
an array that has the same nesting structure as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


TYPE_LIST = lambda x: isinstance(x, list)
TYPE_NUM_OR_STR = lambda x: isinstance(x, (int, float, str))


def are_of_same_type(x, y):
    if (TYPE_LIST(x) and TYPE_LIST(y)) or (TYPE_NUM_OR_STR(x) and TYPE_NUM_OR_STR(y)):
        return True
    return False


def same_structure_as(lst1, lst2):
    for i in range(len(lst1)):

        if i >= len(lst2):
            return False

        if TYPE_LIST(lst1[i]) and TYPE_LIST(lst2[i]):
            if len(lst1) == len(lst2):
                return same_structure_as(lst1[i], lst2[i])
            else:
                return False
        else:
            if not (TYPE_NUM_OR_STR(lst1[i]) and TYPE_NUM_OR_STR(lst2[i])):
                return False

    if not are_of_same_type(lst1, lst2):
        return False

    return True


def run_tests():
    with Test() as test:
        test.assert_equals(same_structure_as(
            [1, [1, 1]],
            [2, [2, 2]]), True, "[1,[1,1]] same as [2,[2,2]]"
        )
        test.assert_equals(same_structure_as(
            [1, [1, 1]],
            [[2, 2], 2]), False, "[1,[1,1]] not same as [[2,2],2]")

        test.assert_equals(same_structure_as([1, 1, 1], [2, 2, 2]), True)


if __name__ == '__main__':
    run_tests()
