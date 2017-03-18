u"""
Maze Runner

Introduction

Welcome Adventurer. Your aim is to navigate the maze and reach the finish point
without touching any walls. Doing so will kill you instantly!

Task

You will be given a 2D array of the maze and an array of directions. Your
task is to follow the directions given. If you reach the end point before all
your moves have gone, you should return Finish. If you hit any walls or go
outside the maze border, you should return Dead. If you find yourself still
in the maze after using all the moves, you should return Lost.

The Maze array will look like

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

..with the following key

0 = Safe place to walk
1 = Wall
2 = Start Point
3 = Finish Point

The Maze array will always be square i.e. 7 x 7 but its size and content will
alter from test to test.

The directions array will always be in upper case and will be in the format of
N = North, E = East, W = West and S = South.

direction = ['N','N','N','N','N','E','E','E','E','E'] == 'Finish'

WIP
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


def find_starting_position(maze, height, width):
    for i in range(height):
        for j in range(width):
            if maze[i][j] == 2:
                return (i, j)


def maze_runner(maze, directions):
    h, w = len(maze), len(maze[0])
    si, sj = find_starting_position(maze, h, w)
    while directions:
        d = directions.pop(0)
        if d == 'N':
            si -= 1
        elif d == 'S':
            si += 1
        elif d == 'W':
            sj -= 1
        elif d == 'E':
            sj += 1
        else:
            raise Exception('Invalid direction')

        if (si == -1 or si == h - 1) or (sj == -1 or sj == w) or maze[si][sj] == 1:
            return 'Dead'

        if maze[si][sj] == 3:
            return 'Finish'

    return 'Lost'


def run_tests():

    with Test() as test:
        maze = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 3],
            [1, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 2, 1, 0, 1, 0, 1]]

        directions = ['N', 'N', 'N', 'N', 'N', 'E', 'E', 'E', 'E', 'E']
        test.assert_equals(maze_runner(maze, directions), 'Finish')

        directions = ['N', 'E', 'S', 'S']
        test.assert_equals(maze_runner(maze, directions), 'Dead')

        directions = ['N', 'E', 'W', 'N']
        test.assert_equals(maze_runner(maze, directions), 'Lost')

        directions = ['N', 'S', 'X', 'N']
        msg = 'Should raise error due to invalid direction'
        test.expect_error(msg, maze_runner(maze, directions))


if __name__ == '__main__':
    run_tests()
