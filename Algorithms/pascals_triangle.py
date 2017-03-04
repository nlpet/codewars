"""
Here you will create the classic pascal's triangle. Your function will be
passed the depth of the triangle and you code has to return the corresponding
pascal triangle upto that depth

The triangle should be returned as a nested array.

for example:

pascal(5) # should return [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
To build the triangle, start with a single 1 at the top, for each number in
the next row you just take the two numbers above it and add them together
(except for the edges, which are all "1"). eg

          [1]
        [1   1]
       [1  2  1]
      [1  3  3  1]
here you get the 3 by adding the 2 and 1 above it.
"""
import math


def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))


def pascal(p):
    result = []
    for c in range(p):
        row = []
        for el in range(c + 1):
            row.append(combination(c, el))
        result.append(row)
    return result



if __name__ == '__main__':
    assert(pascal(1) == [[1]])
    assert(pascal(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
