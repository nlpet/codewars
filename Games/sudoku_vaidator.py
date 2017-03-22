u"""
Validate Sudoku with size `NxN`

Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a
method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array(in Rust: Vec<Vec<u32>>) , ie:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


class Sudoku(object):
    """Sudoku board validator"""

    def __init__(self, board):
        self.board = board
        self.n = len(board)
        self.sqrtn = int(self.n ** 0.5)
        self.valid_range = list(range(1, self.n + 1))

    def valid_dimensions(self):
        for i in range(self.n):
            if len(self.board[i]) != self.n:
                return False
        return (self.n ** 0.5).is_integer()

    def valid_cols(self):
        for i in range(self.n):
            if self.valid_range != sorted([self.board[j][i] for j in range(self.n)]):
                return False
        return True

    def valid_rows(self):
        for i in range(self.n):
            if self.valid_range != sorted(self.board[i]):
                return False
        return True

    def valid_squares(self):
        for j in range(0, self.n, self.sqrtn):
            for i in range(0, self.n, self.sqrtn):
                square = []
                for k in range(self.sqrtn):
                    square += self.board[j + k][i: i + self.sqrtn]
                if self.valid_range != sorted(square):
                    return False
        return True

    def valid_type(self):
        for i in range(self.n):
            if not all(map(lambda x: type(x) == int, self.board[i])):
                return False
        return True

    def valid_board(self):
        return self.valid_cols() and self.valid_rows() and self.valid_squares()

    def is_valid(self):
        return self.valid_dimensions() and self.valid_board() and self.valid_type()


def run_tests():
    with Test() as test:
        # Valid Sudoku
        goodSudoku1 = Sudoku([
            [7, 8, 4, 1, 5, 9, 3, 2, 6],
            [5, 3, 9, 6, 7, 2, 8, 4, 1],
            [6, 1, 2, 4, 3, 8, 7, 5, 9],

            [9, 2, 8, 7, 1, 5, 4, 6, 3],
            [3, 5, 7, 8, 4, 6, 1, 9, 2],
            [4, 6, 1, 9, 2, 3, 5, 8, 7],

            [8, 7, 6, 3, 9, 4, 2, 1, 5],
            [2, 4, 3, 5, 6, 1, 9, 7, 8],
            [1, 9, 5, 2, 8, 7, 6, 3, 4]
        ])

        goodSudoku2 = Sudoku([
            [1, 4, 2, 3],
            [3, 2, 4, 1],

            [4, 1, 3, 2],
            [2, 3, 1, 4]
        ])

        # Invalid Sudoku
        badSudoku1 = Sudoku([
            [0, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],

            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],

            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ])

        badSudoku2 = Sudoku([
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1]
        ])

        test.it('should be valid')
        test.assert_equals(goodSudoku1.is_valid(), True, 'testing valid 9x9')
        test.assert_equals(goodSudoku2.is_valid(), True, 'testing valid 4x4')

        test.it('should be invalid')
        test.assert_equals(badSudoku1.is_valid(), False, 'Values in wrong order')
        test.assert_equals(badSudoku2.is_valid(), False, '4x5 (invalid dimension)')
        test.assert_equals(Sudoku([[True]]).is_valid(), False, 'Invalid type')


if __name__ == '__main__':
    run_tests()
